[Documentation](.) > [Administration](Administration) > [Web Services](Web Services) > WebSocket Service

# WebSocket Service

## Configuration

option | description
---|---
**`type`** | Must be `"websocket"`.
**`url`** | The WebSocket URL to use.
**`serializers`** | List of WAMP serializers to announce/speak, must be from `json` and `msgpack` (default: **all available**)
**`options`** | Please see [WebSocket Options](WebSocket Options)
**`debug`** | Enable transport level debug output. (default: **`false`**)
**`auth`** | Authentication to be used for this *Endpoint* - see [[Authentication]]
**`cookie`** | See [Cookie Tracking](Cookie-Tracking)
