from twisted.internet import defer


class ProfileRequestHandler(object):
    def __init__(self, config, module_api):
        self._config = config
        self._module_api = module_api

    def handle_request(self, request):
        return 200, {"config": self._config}

    @staticmethod
    def parse_config(config):
        if "allowed_users" not in config:
            raise ValueError("Missing allowed_users")
        return config
