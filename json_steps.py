import json
from pprint import pprint as pp

with open('show_ntp_peer_status.json') as file:
    # read in as tuple of strings
    blob = file.read()

json_dict = json.loads(blob)

pp(json_dict)

json_dict['TABLE_peersstatus']['ROW_peersstatus'].append({'appended_to':'peer_status_row'})

json_dump = json.dumps(json_dict)

json_dict = json.loads(json_dump)

pp(json_dict)
