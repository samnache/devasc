import json
from pprint import pprint as pp

with open('show_ip_ospf.json') as file:
    # read in as tuple of strings
    blob = file.read()

json_dict = json.loads(blob)

pp(json_dict)

json_dict['TABLE_ctx']['ROW_ctx']['TABLE_area']['ROW_area']['age'] = 'NO_AGE'

json_dump = json.dumps(json_dict)

json_dict = json.loads(json_dump)

pp(json_dict)
