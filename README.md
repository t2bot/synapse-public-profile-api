# synapse-plugin-relate-groups
A synapse extension to provide routes for accessing profile information of given users publicly. For help setting this up, please visit [#help:t2bot.io](https://matrix.to/#/#help:t2bot.io).

# Install

In the same virtualenv as synapse: `pip install https://github.com/t2bot/synapse-public-profile-api/tarball/master`

# Usage

Add this to your synapse `homeserver.yaml` under one of your listeners:

```yaml
listeners:
  - port: 8008
    bind_addresses: ['::', '0.0.0.0']
    type: http
    tls: true
    x_forwarded: false
    resources:
      - names: ['client', 'webclient']
        compress: true
      - names: ['federation']
        compress: false
    additional_resources:
      "/_matrix/t2bot/user_profile":
        module: synapse-public-profile-api.ProfileRequestHandler
        config:
          # The users that are allowed to be exposed from this API. Must belong to your server.
          allowed_users: ['@travis:t2l.io']
```