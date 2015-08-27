[Documentation](.) > [Administration](Administration) > [Web Services](Web Services) > Resource Service

# Resource Service

Allows to hook any Twisted Web resource into the service tree.

## Configuration

option | description
---|---
**`type`** | must be `"resource"`
**`classname`** | Fully qualified Python class of the Twisted Web resource to expose.
**`extra`** | Arbitrary extra data provided to the constructor of the Twisted Web resource.

