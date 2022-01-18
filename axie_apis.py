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

def get_overview_today():
  '''
  Fetches the state of the market today
  No params required
  '''

  payload = {
  "operationName": "GetOverviewToday",
    "query": "query GetOverviewToday {\n  marketStats {\n    last24Hours {\n      ...OverviewFragment\n      __typename\n    }\n    last7Days {\n      ...OverviewFragment\n      __typename\n    }\n    last30Days {\n      ...OverviewFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment OverviewFragment on SettlementStats {\n  count\n  axieCount\n  volume\n  volumeUsd\n  __typename\n}\n"
  }
  
  endpoint = "https://graphql-gateway.axieinfinity.com/graphql"

  r = requests.post(endpoint, data=payload)
  
  return r.text

def get_parents_brief(matronId, sireId):
  '''
  Fetches the details of 2 parent Axies
  Params:
    matronId : id of the matron Axie
    sireId : id of the sire Axie
  '''
  
  payload = {
  "operationName": "GetParentsBrief",
    "variables": {
      "matronId": matronId,
      "sireId": sireId
    },
    "query": "query GetParentsBrief($matronId: ID!, $sireId: ID!) {\n  matron: axie(axieId: $matronId) {\n    ...AxieBrief\n    __typename\n  }\n  sire: axie(axieId: $sireId) {\n    ...AxieBrief\n    __typename\n  }\n}\n\nfragment AxieBrief on Axie {\n  id\n  name\n  stage\n  class\n  breedCount\n  image\n  title\n  battleInfo {\n    banned\n    __typename\n  }\n  auction {\n    currentPrice\n    currentPriceUSD\n    __typename\n  }\n  parts {\n    id\n    name\n    class\n    type\n    specialGenes\n    __typename\n  }\n  __typename\n}\n"
  }
  
  endpoint = "https://graphql-gateway.axieinfinity.com/graphql"

  r = requests.post(endpoint, data=payload)
  
  return r.text

def new_eth_exchange_rate():
  '''
  Fetches the current USD value of Ether. 
  No params needed
  '''

  payload = {
  "operationName": "NewEthExchangeRate",
    "query": "query NewEthExchangeRate {\n  exchangeRate {\n    eth {\n      usd\n    }\n      }\n}\n"
  }
  
  endpoint = "https://graphql-gateway.axieinfinity.com/graphql"

  r = requests.post(endpoint, data=payload)
  
  return r.text

print(get_overview_today())