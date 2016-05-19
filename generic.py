import StringIO
from buildbot.steps.transfer import _TransferBuildStep, makeStatusRemoteCommand
import os.path
from twisted.python import log
from twisted.spread import pb

class _DataReader(pb.Referenceable):

    """
    Helper class that acts as a file-object with read access given a string
    """

    def __init__(self, data=""):
        self.data = data
        self.i = 0

    def remote_read(self, maxlength):
        """
        Called from remote slave to read at most L{maxlength} bytes of data

        @type  maxlength: C{integer}
        @param maxlength: Maximum number of data bytes that can be returned

        @return: Data read from L{fp}
        @rtype: C{string} of bytes read from file
        """

        if self.i >= len(self.data):
            return ''

        j = self.i + maxlength
        if j >= len(self.data):
            j = len(self.data)

        substr = self.data[self.i:j]
        self.i = j
        return substr

    def remote_close(self):
        """
        Called by remote slave to state that no more data will be transfered
        """
        self.i = len(self.data)


class FileCreate(_TransferBuildStep):

    name = 'create'

    renderables = ['data', 'slavedest']

    def __init__(self, data, slavedest,
                 workdir=None, maxsize=None, blocksize=16 * 1024, mode=None,
                 **buildstep_kwargs):
        _TransferBuildStep.__init__(self, workdir=workdir, **buildstep_kwargs)

        self.data = data
        self.slavedest = slavedest
        self.maxsize = maxsize
        self.blocksize = blocksize
        if not isinstance(mode, (int, type(None))):
            config.error(
                'mode must be an integer or None')
        self.mode = mode

    def start(self):
        self.checkSlaveVersion("downloadFile")

        # we are currently in the buildmaster's basedir, so any non-absolute
        # paths will be interpreted relative to that
        data = self.data
        slavedest = self.slavedest
        log.msg("FileCreate started, creating slave %r" %
                (slavedest))
        log.msg("FileCreate data %s" %
                (data))

        self.descriptionDone = "creating %s" % os.path.basename(slavedest)

        # setup structures for reading the datas
        dataReader = _DataReader(data)

        # default arguments
        args = {
            'slavedest': slavedest,
            'maxsize': self.maxsize,
            'reader': dataReader,
            'blocksize': self.blocksize,
            'workdir': self._getWorkdir(),
            'mode': self.mode,
        }

        cmd = makeStatusRemoteCommand(self, 'downloadFile', args)
        d = self.runTransferCommand(cmd)
        d.addCallback(self.finished).addErrback(self.failed)

def strMakeUser(config):
    lines = []
    for k,v in config.items():
        lines.append("%s=%s" % (k, v))
    return "\n".join(lines)

# TODO: merging PATH env var shouldn't use space as separator
def merge(*dicts):
    keys = set().union(*dicts)

    merged = {}
    for k in keys:
        values = []
        for dic in dicts:
            if k in dic:
                values.append(dic[k])
        if len(values) == 1:
            merged[k] = values[0]
        else:
            merged[k] = " ".join(values)

    return merged
