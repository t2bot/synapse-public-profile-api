from twisted.internet import defer


class ProfileRequestHandler(object):
    def __init__(self, config, module_api):
        self._config = config
        self._module_api = module_api

    @defer.inlineCallbacks
    def handle_request(self, request):
        defer.returnValue((200, {self._config}))

    @staticmethod
    def parse_config(config):
        if "allowed_users" not in config:
            raise ValueError("Missing allowed_users")
        return config