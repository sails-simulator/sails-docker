sails-docker
============

A ready to go sails-simulator environment.

## Usage

    $ docker-compose up

In another terminal verify the stack is running ok:

    # Verify boatd
    $ curl localhost:2222
      {"boatd": {"version": 1.3}}

    # Verify sailsd
    $ echo '{"request": ["version"]}' | nc localhost 3333
      {"version": "1.0"}

    # Verify ui-web
    $ open http://localhost:8080

You can optionally run the stack in the background (detached) via: 

    $ docker-compose up -d

## Developing

The `src` directory is mapped to the `boatd` server, so developing is as simple as editing the existing files and updating the configuration as necessary.

## Where to go from here

- [boatd documentation](https://boatd.readthedocs.io/en/latest/)
- [sailsd documentation](https://github.com/sails-simulator/sailsd)