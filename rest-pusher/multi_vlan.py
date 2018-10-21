import json

class Multi_vlan:
    def __init__(self):
        self.paths_jsons = [
            ('operations/vtn:update-vtn',{"input":{"tenant-name":"VTN_multi_vlan"}}),
            ('operations/vtn-vbridge:update-vbridge', {"input":{"tenant-name":"VTN_multi_vlan","bridge-name":"VirtBr1"}}),
            ('operations/vtn-vlan-map:add-vlan-map', {"input":{"vlan-id":200,"tenant-name":"VTN_multi_vlan","bridge-name":"VirtBr1"}}),
            ('operations/vtn-vbridge:update-vbridge', {"input":{"tenant-name":"VTN_multi_vlan","bridge-name":"VirtBr2"}}),
            ('operations/vtn-vlan-map:add-vlan-map', {"input":{"vlan-id":300,"tenant-name":"VTN_multi_vlan","bridge-name":"VirtBr2"}})
        ]