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


from buildbot.interfaces import IRenderable
from zope.interface import implementer

@implementer(IRenderable)
class MakeUser(object):
    """Render the contents for Julia's `Make.user` file.

    This takes a single dictionary argument `config` containing the variable name and
    setting for each entry to be put in a `Make.user` file.
    """
    def __init__(self, config):
        self.config = config

    def getRenderingFor(self, props):
        d = props.render(self.settings)

        @d.addCallback
        def flat(config):
            lines = []
            for k,v in config.items():
                lines.append("override %s=%s" % (k, v))
            return "\n".join(lines)
        return d
