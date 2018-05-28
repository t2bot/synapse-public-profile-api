import json

from twisted.internet import defer


class ProfileRequestHandler(object):
    def __init__(self, config, module_api):
        self._config = config
        self._module_api = module_api

    @defer.inlineCallbacks
    def handle_request(self, request):
        request.responseHeaders.addRawHeader(b"content-type", b"application/json")
        if 'user_id' not in request.args or len(request.args['user_id']) != 1:
            request.setResponseCode(400)
            request.write('{"errcode":"IO.T2BOT.PROFILE_MISSING_USER_ID","error":"Missing user_id query param"}')
        else:
            user_id = request.args['user_id'][0]
            if user_id not in self._config["allowed_users"]:
                request.setResponseCode(400)
                request.write('{"errcode":"IO.T2BOT.PROFILE_USER_BLACKLISTED","error":"That user is not allowed"}')
            else:
                hs_name = self._module_api.hs.config.server_name
                if not user_id.endswith(":" + hs_name):
                    request.setResponseCode(400)
                    request.write('{"errcode":"IO.T2BOT.PROFILE_WRONG_DOMAIN","error":"That user is not allowed"}')
                else:
                    profile = yield self._module_api.hs.get_profile_handler().get_profile(user_id)
                    request.write(json.dumps(profile))
        request.finish()

    @staticmethod
    def parse_config(config):
        if "allowed_users" not in config:
            raise ValueError("Missing allowed_users")
        return config
