import pprint
from agp_py import AxieGene

# 1. getGeneticsHexCode()
#   - Develop a function specifically for getting hex decimal code 
#     using axie id.
# 2. parseGeneticHexCode()
#   - Parse the output of getGeneticsHexCode() to dictionary
hex_string = '0x11c642400a028ca14a428c20cc011080c61180a0820180604233082'
hex_type = 256
gene = AxieGene(hex_string, hex_type)
pprint.pprint(gene.genes)
