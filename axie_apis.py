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


def get_axie_latest(from_, size, sort, auctionType):
    '''
    Fetches a list of the latest Axie listing.
    Parameters:
      from_ : axie id to search from
      size : how many axies to grep
      sort : sorting criterias
      auctionType : auction type
    '''

    payload = {
        "operationName": "GetAxieLatest",
        "variables": {
            "from": from_,
            "size": size,
            "sort": sort,
            "auctionType": auctionType,
            "criteria": {}
        },
        "query": "query GetAxieLatest($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {\n    total\n    results {\n      ...AxieRowData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieRowData on Axie {\n  id\n  image\n  class\n  name\n  genes\n  owner\n  class\n  stage\n  title\n  breedCount\n  level\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"
    }

    # endpoint is api_url
    endpoint = "https://graphql-gateway.axieinfinity.com/graphql"

    # send API call and assign response to variable
    response = requests.post(endpoint, data=payload)
