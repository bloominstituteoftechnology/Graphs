# Bokeh

bokeh (pronounced boh-kay) is a simple, scalable and blazing-fast task queue built on [Node.js](http://nodejs.org) and [ZeroMQ](http://zeromq.org). It allows you to offload tasks from your main application process and distribute them among a pool of workers. Workers can be running on the same host as your application, or scaled out onto multiple machines for greater processing power.

When you want a worker to run a task, just submit it to the broker using the client API. A task is simply any class in your application which responds to the `run` method.

Bokeh consists of three components:

1. The client library which your application uses to submit tasks to the broker.
2. The broker process which manages the pool of workers.
3. The worker processes which are responsible for running tasks.

![](bokeh/raw/master/doc/bokeh.png)

## Installation

### ZeroMQ

The only prerequisite is that you have ZeroMQ installed.

**OS X**

Install ZeroMQ using brew:

    $ brew install zeromq

**Ubuntu 10.04 LTS**

Install ZeroMQ using [Chris Lea's PPA](https://launchpad.net/~chris-lea/+archive/zeromq):

    $ sudo add-apt-repository ppa:chris-lea/zeromq
    $ sudo apt-get update
    $ sudo apt-get install libzmq-dbg libzmq-dev libzmq1

### Bokeh

Install Bokeh using npm:

    $ npm install bokeh

## Overview

### Task

A task is a class which responds to the `run` method. A task is dealt to a worker and executed.

Once the task has been completed, you must call the callback with any data you want to pass back to your application.

    class Reverse
      run: (data, callback) -> callback null, data.split("").reverse().join("")

### Client

The client is used by your application to submit tasks to the broker and monitor their progress.

    bokeh = require "bokeh"
    handle = bokeh.getClient().submitTask "Reverse", "hello world"
    handle.on "complete", (data) -> console.log "Task %s completed: %s", handle.id, data
    handle.on "error", (error) -> console.error "Task %s failed: %s", handle.id, error

### Broker

The broker is responsible for routing messages from clients, persisting them to the data store and dealing them to workers.

    bokeh = require "bokeh"
    broker = new bokeh.Broker

Bokeh supports pluggable data stores for persisting tasks, currently in-memory, [Redis](http://redis.io/) and [Riak](http://basho.com/products/riak-overview/) are supported.

### Worker

A worker is a process which receives tasks from a broker and executes them. You must register all your task classes with the worker.

    bokeh = require "bokeh"
    worker = new bokeh.Worker
    worker.registerTask "Reverse", require("./tasks/reverse")

## Example

Check out the [example application](bokeh/tree/master/example).

## License

Bokeh is released under the [MIT license](bokeh/blob/master/LICENSE).
