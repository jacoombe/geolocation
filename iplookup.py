import argparse
import requests
KEY_URL = 'http://api.ipstack.com/'

def get_ip_data(ip_address: str, key: str):
    data = requests.get(f'http://api.ipstack.com/{ip_address}?access_key={key}')
    return data.json()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                    prog='IP Address Coordinate reported',
                    description='Reports the coordinates of an IP address approximately')

    parser.add_argument('ipaddress')
    args = parser.parse_args()

    with open('.apikey', 'r') as fh:
        api_key = fh.read()
    
    

    print(api_key)