import json
import requests
import sys
import multi_vlan
import provision_l2
import rest_pusher_config

def usage():
    print 'This is trivial REST API json pusher. Supported arguments:\n-p to push Provision L2 ODL configuration\n-m to push Multi Vlan ODL configuration\n-c to push clean up request'

def push_POSTs(template):
    headers = rest_pusher_config.headers
    url_core = rest_pusher_config.url
    for element in template.paths_jsons:
        specific_url = url_core + element[0]
        data = element[1]
        response = requests.post(specific_url, json=data, headers=headers, auth=(rest_pusher_config.username, rest_pusher_config.password))
        print response.status_code
        print response.text
    

def main():
    if len(sys.argv) < 2:
        usage()
    elif sys.argv[1] == '-p':
        template = provision_l2.Provision_l2()
        push_POSTs(template)
    elif sys.argv[1] == '-m':
        template = multi_vlan.Multi_vlan()
        push_POSTs(template)
    else:
        usage()

main()
