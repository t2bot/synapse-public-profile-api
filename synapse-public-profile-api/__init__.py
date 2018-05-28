import json


class ProfileRequestHandler(object):
    def __init__(self, config, module_api):
        self._config = config
        self._module_api = module_api

    def handle_request(self, request):
        request.responseHeaders.addRawHeader(b"content-type", b"application/json")
        if 'user_id' not in request.args:
            request.setResponseCode(400)
            request.write('{"errcode":"M_BAD_REQUEST","error":"Missing user_id query param"}')
        else:
            request.write(request.args['user_id'])
        request.finish()

    @staticmethod
    def parse_config(config):
        if "allowed_users" not in config:
            raise ValueError("Missing allowed_users")
        return config
