#!/usr/bin/env python3

"""A command line tool to look up geolocation data"""

import argparse
import ipaddress
import os
import sys

import requests


def get_ip_data(ip_address: str, key: str):
    """A basic function to get information from ipstack.com
    :param ip_address: The IP address to search for
    :param key: the API Key to use
    """
    data = requests.get(
        f'http://api.ipstack.com/{ip_address}?access_key={key}'
    )
    return data.json()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='IP Address Coordinate reported',
        description='Reports the coordinates of an IP address approximately'
        'the first response is the lattitude the second response is the '
        'longitude'
    )

    parser.add_argument('ipaddress')
    args = parser.parse_args()

    if not os.path.exists('.apikey'):
        print('No API key found in .apikey')
        sys.exit(1)

    with open('.apikey', 'r') as fh:
        api_key = fh.read()

    ip_text = args.ipaddress
    try:
        ip_address = ipaddress.ip_address(ip_text)
    except ValueError:
        print(f'the ip address {ip_text} isnt valid')
        sys.exit(2)

    if not ip_address.is_global:
        print(
            f'{ip_text} is not geographic only global not local or private'
            ' ip addresses are valid for lookup'
        )
        sys.exit(3)

    info = get_ip_data(ip_text, api_key)

    if 'error' in info:
        ec = info['error']['code']
        print(f"error {ec} from ipstack.com: {info['error']['info']}")
        sys.exit(ec)

    print(info['latitude'])
    print(info['longitude'])
