import re
class Interfacevalidator:
    #assigning interfaces in routers.
    def __init__(self, interfaces):
        self.interfaces = interfaces
    #validation of interface.
    def validate_interface(self):
        for interface in self.interfaces:
            re.findall(r"interface ")
            

