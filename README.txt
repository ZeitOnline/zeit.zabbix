===========
zeit.zabbix
===========

This package provides helper scripts for dealing with the `Zabbix`_ monitoring
system.

.. _`Zabbix`: http://www.zabbix.com


Creating maintenance periods
============================

To create a maintenance period of 30 minutes for hosts ``one`` and ``two``,
run::

  $ zabbixmaintenance -H http://zabbix.example.org/zabbix/ -u USER -p PASS \
      -d 30 -m "Reboot for kernel upgrade" one.example.org two.example.org

Note that the user must be of type "Zabbix admin" to be able to read/write
maintenance periods, and in a user group that has read/write access to the
given hosts.
