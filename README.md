## Requirements

You will need Python 2. Necessary Python packages can then be installed by doing:

```console
make deps
```

## Serving

To serve the documentation:

```console
make test
```

## Authors guide

### Code blocks

Allowed language tags for syntax highlighted code blocks:

* `shell` - an actual shell script (eg bash), NOT a console log, and NOT a (plain) series of commands
* `console` - a log of a terminal session
* `text` - a plain text block, eg from a Unix config file
* `javascript`
* `json`
* `python`

Note that a plain series of commands should NOT be marked up as a syntax highlighted a code block, but a regular Markdown code block: indented by 4 spaces!

### Images

All images MUST be formatted as

    ![..Image Title..](..Image URL..)

Also note that an image title is REQUIRED (that's good in general, but otherwise some rendering stuff breaks).

# Headers

The document MUST start with a top level heading (a single `#`) and the document MUST only contain one top level heading.
