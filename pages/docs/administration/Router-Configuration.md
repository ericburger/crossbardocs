[Documentation](.) > [Administration](Administration) > Router Configuration

# Router Configuration

*Routers* are the core facilities of Crossbar.io, responsible for routing WAMP remote procedure calls between *Callers* and *Callees*, as well as routing WAMP publish-subscribe events between *Publishers* and *Subscribers*.

A Crossbar.io instance will usually be running at least one *Router*, unless is used solely to run application components in *Workers* or *Guests*.

A *Router* is configured as a *Worker*, more precisely a *Native Worker*, process of `type == "router"`:

```javascript
{
   "workers": [
      {
         "type": "router",
         "options": {
            // router options go here
         },
         "realms": [
            // realms managed by this router
         ],
         "transports": [
            // transports run by this router
         ],
         "components": [
            // app components running side-by-side with this router
         ],
         "manhole": {
            // debugging access
         }
      }
   ]
}
```

For the available `options` with *Routers*, please see

* [[Native Worker Options]]
* [[Process Environments]]

For configuration of `realms`, `transports` and `components`, have a look here

* [[Router Realms]]
* [[Router Transports]]
* [[Router Components]]

For the configuration of `manhole`, see

* [[Manhole]]
