import json
import requests
import pprint
#from agp_py import AxieGene

def get_gene_hexcode(axie_id):
  '''
  Fetches the gene info of the Axie
  Params:
    AxieId: ID of the Axie
  '''
  
  payload = {
    "operationName": "GetAxieDetail",
    "variables": {
      "axieId": f"{axie_id}"
    },
    "query": "query GetAxieDetail($axieId: ID!) {\n  axie(axieId: $axieId) {\n    ...AxieDetail\n    __typename\n  }\n}\n\nfragment AxieDetail on Axie {\n  id\n  image\n  class\n  chain\n  name\n  genes\n  owner\n  birthDate\n  bodyShape\n  class\n  sireId\n  sireClass\n  matronId\n  matronClass\n  stage\n  title\n  breedCount\n  level\n  figure {\n    atlas\n    model\n    image\n    __typename\n  }\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  ownerProfile {\n    name\n    __typename\n  }\n  battleInfo {\n    ...AxieBattleInfo\n    __typename\n  }\n  children {\n    id\n    name\n    class\n    image\n    title\n    stage\n    __typename\n  }\n  __typename\n}\n\nfragment AxieBattleInfo on AxieBattleInfo {\n  banned\n  banUntil\n  level\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"
  }

  endpoint = "https://graphql-gateway.axieinfinity.com/graphql"

  r = requests.post(endpoint, json=payload, headers={"Content-Type" : "application/json"})
  
  return r.text

#def parseGeneticHexCode():
  '''
  
  '''
  #hex_string = '0x11c642400a028ca14a428c20cc011080c61180a0820180604233082'
  #hex_type = 256
  #gene = AxieGene(hex_string, hex_type)
  
  #pprint.pprint(gene.genes)

axie_details = json.loads(get_gene_hexcode(1621247))
pprint.pprint(axie_details)

def cal_breeding_prob(parent1, parent2, target):
  '''
    Calculate the probability of breeding a target axie given 2 parent axies.
    Params:
      - parent1 : axie id for parent #1
      - parent2 : axie id for parent #2 
      - target : axie id for the target
  '''

  # Get genes info from both parents and target

  # Check if the gene pool of both parents include all genes from target

  # If the genes of target is inclusive
  # 1. Extract the probability of each gene

  # 2. Calculate the probablity (product of all probabilities).
