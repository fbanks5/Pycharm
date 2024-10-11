import sys
import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Request to {url} failed with status {res.status_code}')
    return res
def pwned_api_key_checker(password):
    #Check if pw exists in api response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    return sha1password

pwned_api_key_checker('123')