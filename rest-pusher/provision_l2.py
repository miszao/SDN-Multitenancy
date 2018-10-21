import json

class Provision_l2:
    def __init__(self):
        self.paths_jsons = [
            ('operations/vtn:update-vtn', {"input":{"tenant-name":"VTN_test"}}),
            ('operations/vtn-vbridge:update-vbridge', {"input":{"tenant-name":"VTN_test", "bridge-name":"VirtBr1"}}),
            ('operations/vtn-vinterface:update-vinterface', {"input":{"tenant-name":"VTN_test", "bridge-name":"VirtBr1", "interface-name":"int1"}}),
            ('operations/vtn-vinterface:update-vinterface', {"input":{"tenant-name":"VTN_test", "bridge-name":"VirtBr1", "interface-name":"int2"}}),
            ('operations/vtn-port-map:set-port-map', {"input":{"tenant-name":"VTN_test", "bridge-name":"VirtBr1", "interface-name":"int1", "node":"openflow:3", "port-name":"s3-eth1"}}),
            ('operations/vtn-port-map:set-port-map', {"input":{"tenant-name":"VTN_test", "bridge-name":"VirtBr1", "interface-name":"int2", "node":"openflow:7", "port-name":"s7-eth1"}})
        ]