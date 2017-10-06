import requests

BASE_URL = 'https://dev-575201-admin.oktapreview.com'


def login(username, password):
    data = {
        "username": username,
        "password": password,
        "options": {
            "multiOptionalFactorEnroll": True,
            "warnBeforePasswordExpired": True
        }
    }

    r = requests.post('{url}/api/v1/authn'.format(url=BASE_URL), data=data).json()
    if r['status'] != 'SUCCESS':
        print ('Authentication was unsuccessful!')
        return

    return r['sessionToken']
