import json


class ProfileRequestHandler(object):
    def __init__(self, config, module_api):
        self._config = config
        self._module_api = module_api

    def handle_request(self, request):
        request.responseHeaders.addRawHeader(b"content-type", b"application/json")
        request.write(json.dumps({"config", self._config}))
        request.finish()

    @staticmethod
    def parse_config(config):
        if "allowed_users" not in config:
            raise ValueError("Missing allowed_users")
        return config
