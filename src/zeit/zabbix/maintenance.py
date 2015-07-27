from datetime import datetime
import argparse
import pyzabbix
import time


def date_to_seconds(timestamp):
    return time.mktime(timestamp.timetuple())


def time_to_seconds(timestamp):
    return timestamp.hour * 60 + timestamp.minute


def add_maintenance_period(url, user, password, message, duration, hostnames):
    pass


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Configure Zabbix maintenance period')
    parser.add_argument(
        '-H', '--host',
        help='Zabbix URL, e.g. http://zabbix.example.com/zabbix/')
    parser.add_argument('-u', '--username', help='Username ')
    parser.add_argument('-p', '--password', help='Password')
    parser.add_argument('-m', '--message', help='Message')
    parser.add_argument(
        '-d', '--duration', type=int, default=30,
        help='Duration of maintenance in minutes')
    parser.add_argument('hostnames', nargs='*')

    options = parser.parse_args(argv)
    if not all([options.host, options.username, options.password,
                options.hostnames]):
        parser.print_help()
        raise SystemExit(1)

    add_maintenance_period(
        options.host, options.user, options.password,
        options.message, options.duration, options.hostnames)
