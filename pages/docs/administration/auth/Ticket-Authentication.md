[Documentation](.) > [Administration](Administration) > [Authentication](Authentication) > Ticket Authentication

# Ticket Authentication

## Examples

* [Static Ticket Authentication](https://github.com/crossbario/crossbarexamples/tree/master/authenticate/ticket)
* [Dynamic/Custom Ticket Authentication](https://github.com/crossbario/crossbarexamples/tree/master/authenticate/ticketdynamic)

## Configuration

```json
{
    "auth": {
        "ticket": {
            "type": "static",
            "principals": {
                "device23": {
                    "ticket": "Xy$h2l-D",
                    "role": "frontend"
                }
            }
        }
    }
}
```

### Static

parameter | description
---|---
**`type`** | `"static"`
**`principals`** | A dictionary of names mapping to values being dictionaries as below.

Each principal has this associated dictionary:

attribute | description
---|---
**`ticket`** | Arbitrary text value for authenticating ticket (**required**).
**`role`** | Optional `authrole` a client using this ticket will be authenticated under.

### Dynamic

parameter | description
---|---
**`type`** | `"dynamic"`
**`authenticator`** | URI of custom authenticator to call.
