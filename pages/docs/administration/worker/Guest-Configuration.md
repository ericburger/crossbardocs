**Guest workers** are worker processes spawned by Crossbar.io which runapplication components written in languages other than Python (the language which Crossbar.io is written in), or in Python 3.x (Crossbar.io is currently on Python 2.7).

This makes deployment of WAMP applications easier, since you can start an entire application backend just by starting Crossbar.io.

Guest workers are configured under `workers`, as type `guest`.

For example, here is a **Guest Worker** configuration which starts a JavaScript component using Node.js:

```javascript
{
   "type": "guest",
   "executable": "node",
   "arguments": ["hello.js"],
   "options": {
      "workdir": "../node",
      "watch": {
         "directories": ["../node"],
         "action": "restart"
      }
   }
}
```

The worker itself has the options

1. `type`: must be `"guest"` (*required*)
2. `executable`: the path to the executable (*required*)
3. `arguments`: an array of arguments to pass to the executable
4. `options`: a dictionary of options to use

In the above example, the name of the JavaScript component to execute with Node.js is passed as an argument.

The `options` are:

1. `env`: A dictionary of environment variables to set for the executable, with the possible keys `inherit` and `vars
2. `workdir`: The `working directory for the executable.
3. `watch`: Watch directories and carry out an action based on changes in these. Takes a dict with keys `directories` (a list of path-names) and `action` (only `restart` accepted).
4. `stdin`: Dictionary of data to pass in on standard in, or the string 'close`. The dictionary should contain a key `type` (value `json` or `msgpack`) and a key `value` which is the data to JSON/msgpack encode. Optionally, `close` can be a key (value `true`) as well, causing stdin to be closed after the data is written.
5. `stdout`: Action on signal on standard out, can be `close`, `log` or `drop`
6. `stderr`: Action on signal on standard error, can be `close`, `log` or `drop`

## Executable Path

The argument `executable` provides the path to the executable that Crossbar.io uses when starting the worker. 

Crossbar.io first parses this as an absolute path as well as a relative path (relative to the `workdir` in `options`). If no executable is found there, then it considers it an environment variable and attempts to use the path stored there.

> **Note**: Python defaults to unbuffered stdout, so you probably want to [pass the -u option](https://docs.python.org/3/using/cmdline.html#cmdoption-u) when configuring Python guest workers.