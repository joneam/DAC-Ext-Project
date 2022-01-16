import requests


def get_axie_transfer_history(axieId, from_, size):
    '''
    Fetches transfer history of an axie
    Params:
    axieId: axie ID
    from_ : axie id to search from
    size : how many axies to grep
    '''

    payload = {
        "operationName": "GetAxieTransferHistory",
         "variables": {
            "axieId": axieId,
            "from": from_,
            "size": size
  },
  "query": "query GetAxieTransferHistory($axieId: ID!, $from: Int!, $size: Int!) {\n  axie(axieId: $axieId) {\n    id\n    transferHistory(from: $from, size: $size) {\n      ...TransferRecords\n      __typename\n    }\n    ethereumTransferHistory(from: $from, size: $size) {\n      ...TransferRecords\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment TransferRecords on TransferRecords {\n  total\n  results {\n    from\n    to\n    timestamp\n    txHash\n    withPrice\n    __typename\n  }\n  __typename\n}\n"
}

    endpoint = "https://graphql-gateway.axieinfinity.com/graphql"
    r = requests.post(endpoint, data = payload)

    return r.text
func_get_axie_transfer_history = get_axie_transfer_history(5, 1, 1)
print(func_get_axie_transfer_history)

  
