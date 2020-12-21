import xmltodict
from pprint import pprint as pp

with open('show_ntp_peer_status.xml') as file:
    xml_doc = file.read()

xml_json = xmltodict.parse(xml_doc)

pp(xml_json)

