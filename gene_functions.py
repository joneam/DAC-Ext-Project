import json 
import requests
import pprint
from agp_py import AxieGene


def get_gene_hexcode(axie_id):
  '''
  Fetches the gene info of the Axie
  Params:
    axie_id: ID of the Axie
  '''
  
  payload = {
  "operationName": "GetAxieDetail",
    "variables": {
      "axieId": f"{axie_id}"
    },
    "query": "query GetAxieDetail($axieId: ID!) {\n  axie(axieId: $axieId) {\n    ...AxieDetail\n  }\n}\n\nfragment AxieDetail on Axie {\n  class\n  chain\n  genes\n  class\n  breedCount\n}\n"
  }

  endpoint = "https://graphql-gateway.axieinfinity.com/graphql"

  r = requests.post(endpoint, json=payload, headers={"Content-Type" : "application/json"})
  dict = r.text 
  
  return dict
  #return dict[57:-20]

def parse_gene_hexcode(gene_hex):
  '''
  Parses the gene details from gene hexcode input
  Params:
    gene_hex: Gene info of Axie in hexadecimal form 
  '''
  #hex_string = '0x11c642400a028ca14a428c20cc011080c61180a0820180604233082'
  hex_string = gene_hex
  hex_type = 256
  gene = AxieGene(hex_string, hex_type)
  
  pprint.pprint(gene.genes)

#print(get_gene_hexcode())
axie_details = json.loads(get_gene_hexcode(1621247))
pprint.pprint(axie_details)
#parse_gene_hexcode('0x61c7200044110820080200800651006002410080060180600401002')