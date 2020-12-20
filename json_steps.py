import json
from pprint import pprint as pp

with open('show_ip_ospf.json') as file:
    # read in as tuple of strings
    blob = file.read()

json_dict = json.loads(blob)

pp(json_dict)
