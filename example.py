import json

from pyex.api import PyexAPIBuilder, Exchange

if __name__ == "__main__":
    with open('api.json', 'r', encoding='utf-8') as f:
        obj = json.loads(f.read())
    api_key = obj['api_key']
    secret_key = obj['secret_key']
    passphrase = obj['passphrase']

    api = PyexAPIBuilder().api_key(api_key) \
                        .secret_key(secret_key) \
                        .passphrase(passphrase) \
                        .build(Exchange.OKEX)

    
