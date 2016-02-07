[Documentation](.) > [Administration](Administration) > [Authentication](Authentication) > Anonymous Authentication

# Anonymous Authentication

Strictly speaking, Anonymous Authentication is not authentication - it is about what to do in the absence of authentication

You need to explicitly define Anonymous Authentication for a particular transport - as a default this is not allowed, e.g. here for a WebSocket endpoint on a Web transport

```javascript
"transports": [
   {
      "type": "web",
      "endpoint": {
         "type": "tcp",
         "port": 8080
      },
      "paths": {
         "/": {
            "type": "static",
            "directory": "../web"
         },
         "ws": {
            "type": "websocket",
            "auth": {
               "anonymous": {
                  "type": "static",
                  "role": "public"
               }
            }
         }
      }
   }
```

Any client using Anonymous Authentication on this endpoint is then assigned the role `public`.

The permissions for this role are configured just like for any other role.

For a full working example of Anonymous Authentication using static configuration, see [Crossbarexamples](https://github.com/crossbario/crossbarexamples/tree/master/authentication/anonymous/static).

## Dynamic authentication

Just as for other authentication methods, you can define a dynamic authenticator component for Anonymous Authentication:

```javascript
"auth": {
   "anonymous": {
      "type": "dynamic",
      "authenticator": "com.example.authenticate"
   }
}
```

Here the authenticator function which is registered for `com.example.authenticate` is called for each attempted Anonymout Authentication.

For a full working example of Anonymous Authentication using a dynamic authenticator, see [Crossbarexamples](https://github.com/crossbario/crossbarexamples/tree/master/authentication/anonymous/dynamic).
