Redis Session Store
===================

This module allows you to use a Redis database to manage sessions,
instead of classic filesystem storage.

Redis is an open source, in-memory data structure store, used as a database, cache and message broker.

It is useful for load balancing because session's directory may not be shared.

Requirements
============

You need to install and to start a Redis server to use this module.
Documentation is available on `Redis website`_.

You need to install package `redis`::

    pip3 install redis

.. _`Redis website`: http://redis.io/topics/quickstart


Usage
=====

To use Redis, install this module and please add `enable_redis = True` option
in configuration file.

Available options (odoo.conf)
-----------------

* `redis_host` (default: localhost): Redis host
* `redis_port` (default: 6379): Redis port
* `redis_dbindex` (default: 1): Redis database index
* `redis_password` (default: None): Redis password
* `enable_redis` (default: False)
* `redis_expiration` (default: 60*60*24*7) One Week


Bug Tracker
===========

Bugs are tracked on `GitHub Issues

Credits
=======

Contributors
------------

* Mackilem Van der Laan Soares

Maintainer
----------

This module is maintained by Goiaba Intelligence
