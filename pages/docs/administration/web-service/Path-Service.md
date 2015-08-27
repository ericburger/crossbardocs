[Documentation](.) > [Administration](Administration) > [Web Services](Web Services) > Path Service

# Path Service

Provides nesting of Web path services.

## Configuration

option | description
---|---
**`type`** | must be `"path"`
**`paths`** | A dictionary for configuring services on subpaths (*required* - see below).

Web transport `paths`:

* must match the regular expression `^([a-z0-9A-Z_\-]+|/)$`
* must contain a root path `/`
