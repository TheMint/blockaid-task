"""
Usage:
    my_approvals.py --address=<address>

Options:
    --address=<address>  Blockchain address.
"""

import json

import requests
from docopt import docopt

key = "c8eab58d57dc4cc4bcd3791333bfc1ac"
url = f"https://mainnet.infura.io/v3/{key}"


def get_approvals(address: str) -> list:
    approvals = []
    payload = {"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1}
    headers = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    print(response)
    return approvals


def main() -> None:
    args = docopt(__doc__)
    address = args["--address"]
    approvals = get_approvals(address)


if __name__ == "__main__":
    main()
