import requests


def get_axie_brief_list(from_, size, sort, auctionType):
  '''
  Fetch axies with certain criterias
  Params:
    from_ : axie id to search from
    size : how many axies to grep
    sort : sorting criterias
    auctionType : auction type
  '''

  payload = {  
  "operationName": "GetAxieBriefList",
    "variables": {
      "from": from_,
      "size": size,
      "sort": sort,
      "auctionType": auctionType,
      "criteria": {}
    },
    "query": "query GetAxieBriefList($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {\n    total\n    results {\n      ...AxieBrief\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieBrief on Axie {\n  id\n  name\n  stage\n  class\n  breedCount\n  image\n  title\n  battleInfo {\n    banned\n    __typename\n  }\n  auction {\n    currentPrice\n    currentPriceUSD\n    __typename\n  }\n  parts {\n    id\n    name\n    class\n    type\n    specialGenes\n    __typename\n  }\n  __typename\n}\n"
  }

  endpoint = "https://graphql-gateway.axieinfinity.com/graphql"

  r = requests.post(endpoint, data=payload)
  
  return r.text

  