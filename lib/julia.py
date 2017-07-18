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
        d = props.render(self.config)

        @d.addCallback
        def flat(config):
            lines = []
            for k,v in config.items():
                lines.append("override %s=%s" % (k, v))
            return "\n".join(lines)
        return d
