[Documentation](.) > Administration

# Administration

* [Router Transports](Router Transports)
* [HTTP Bridge Services](HTTP Bridge Services)
* [Web Services](Web Services)
* []()
* []()
* []()

## Configuration

The Configuration section covers configuring the basics of Crossbar.io, e.g. realms, transports and workers.

* [Configuration Overview](Configuration Overview)
  - [Endpoints](Endpoints)
  - [Native Worker Options](Native Worker Options)
  - [Process Enviroments](Process Environments)
* [Controller Configuration](Controller Configuration)
* [Router Configuration](Router Configuration)
  - [Router Realms](Router Realms)
  - [Router Transports](Router Transports)
     - [WebSocket Transport](WebSocket Transport)
        - [Cookie Tracking](Cookie-Tracking)
     - [RawSocket Transport](RawSocket Transport)
     - [Web Transport and Services](Web Transport and Services)
        - [Static Web Service](Static Web Service)
        - [Web Redirection Service](Web Redirection Service)
        - [JSON Value Service](JSON Value Service)
        - [CGI Script Service](CGI Script Service)
        - [WSGI Host Service](WSGI Host Service)
        - [Long-Poll Service](Long Poll Service)
        - [File Upload Service](File-Upload-Service)
        - [HTTP Bridge Services](HTTP Bridge Services)
           - [HTTP Publisher](HTTP Bridge Services Publisher)
           - [HTTP Caller](HTTP Bridge Services Caller)
           - [HTTP Subscriber](HTTP Bridge Services Subscriber)
           - [HTTP Callee](HTTP Bridge Services Callee)
           - [HTTP Webhooks](HTTP Bridge Services Webhook)
     - [Flash Policy Transport](Flash-Policy-Transport)
  - [Router Components](Router-Components)
  - [Authentication](Authentication)
     - [Anonymous Authentication](Anonymous Authentication)
     - [WAMP Challenge-Response Authentication)](WAMP-CRA-Authentication)
     - [Cookie-based Authentication](Cookie-Authentication)
  - [Authorization](Authorization)
     * [URI Format](URI Format)
* [Container Configuration](Container Configuration)
* [Guest Configuration](Guest Configuration)
* [Database Integration](Database Integration)
  - [PostgreSQL-Integration](PostgreSQL-Integration)

## Going to Production

This section covers security issues and fine-tuning of advanced options. Tips for a performant and secure production configuration.

* [Running on privileged ports](Running on privileged ports)
* [Secure WebSocket and HTTPS](Secure WebSocket and HTTPS)
* [WebSocket Options](WebSocket Options)
* [WebSocket Compression](WebSocket Compression)
* [Automatic startup and restart](Automatic startup and restart)
* [Network Tuning](Network Tuning)
* [Reverse Proxies](Reverse Proxies)
* [SSL/TLS Interception Proxies](SSL-TLS-Interception-Proxies)
* [General IoT Security](Security)

## Compliance and Performance

Testing your instance & browser support.

* [Browser Support](Browser Support)
* [WebSocket Compliance Testing](WebSocket Compliance Testing)
* [Stream Testee](Stream Testee)
