import requests

def get_axie_detail():
  '''
  Params: 
  '''    
  
  payload = {
  "operationName": "GetAxieDetail",
    "variables": {
      "axieId": "1621247"
    },
    "query": "query GetAxieDetail($axieId: ID!) {\n  axie(axieId: $axieId) {\n    ...AxieDetail\n    __typename\n  }\n}\n\nfragment AxieDetail on Axie {\n  id\n  image\n  class\n  chain\n  name\n  genes\n  owner\n  birthDate\n  bodyShape\n  class\n  sireId\n  sireClass\n  matronId\n  matronClass\n  stage\n  title\n  breedCount\n  level\n  figure {\n    atlas\n    model\n    image\n    __typename\n  }\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  ownerProfile {\n    name\n    __typename\n  }\n  battleInfo {\n    ...AxieBattleInfo\n    __typename\n  }\n  children {\n    id\n    name\n    class\n    image\n    title\n    stage\n    __typename\n  }\n  __typename\n}\n\nfragment AxieBattleInfo on AxieBattleInfo {\n  banned\n  banUntil\n  level\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"
  }
  
  endpoint = "https://graphql-gateway.axieinfinity.com/graphql"

  r = requests.post(endpoint, data=payload)
  
  return r.text

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
  dict = r.text
  
  return dict[32:-5]

print(new_eth_exchange_rate())
