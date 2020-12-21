import yaml
from pprint import pprint as pp

try:
    filename = input('Enter the name of the file')

    with open(filename) as file:
        yaml_doc = file.read()
except BaseException:
    print('file not found ending')
    raise BaseException('ENDING NOW')
else:
    yaml_dict = yaml.safe_load(yaml_doc)

    for status in yaml_dict['TABLE_peersstatus']['ROW_peersstatus']:
        pp(status)

    yaml_dict['TABLE_peersstatus']['ROW_peersstatus'].append({'appended_to':'peer_status_row'})

    pp(yaml_dict)

    yaml_doc = yaml.dump(yaml_dict)

    pp(yaml_doc)
