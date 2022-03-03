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
      "axieId": "1621247"
    },
    "query": "query GetAxieDetail($axieId: ID!) {\n  axie(axieId: $axieId) {\n    ...AxieDetail\n  }\n}\n\nfragment AxieDetail on Axie {\n  genes\n  breedCount\n}\n"
  }

  endpoint = "https://graphql-gateway.axieinfinity.com/graphql"

  r = requests.post(endpoint, json=payload, headers={"Content-Type" : "application/json"})
  dict = r.text 
  dict2 = json.loads(dict)
  
  return dict2.get('data').get('axie').get('genes')
  #return dict
  #return dict[26:-20]

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
  
  #pprint.pprint(gene.genes)
  return gene.genes

def cal_breeding_prob(parent1, parent2):
  '''
    Calculate the probability of breeding a target axie given 2 parent axies.
    Params:
      - parent1 : axie id for parent #1
      - parent2 : axie id for parent #2 
      - target : list of genes for target axie
  '''

  p1_code = get_gene_hexcode(parent1)
  p2_code = get_gene_hexcode(parent2)

  p1_gene = parse_gene_hexcode(p1_code)
  p2_gene = parse_gene_hexcode(p2_code)    
  
  # p1_dict = json.loads(p1_gene)
  # p2_dict = json.loads(p2_gene)
  
  p1_list = p1_gene.get('back','ears').get('d')
  p2_list = p2_gene.get('back').get('d')
  
  print(p1_list,p2_list)


#print(get_gene_hexcode(1621247))
#parse_gene_hexcode('0x61c7200044110820080200800651006002410080060180600401002')
cal_breeding_prob(123,122)