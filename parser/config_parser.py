#We are extracting hostname, 
import re
class ConfigParser:
    def __init__(self, config_text):
        self.config_text = config_text

    def get_hostname(self):
        return re.findall(r"hostname (\S+)", self.config_text)
        
    
    def get_interface(self):
        
        return re.findall(r"interface (\S+)\n ip address",self.config_text)

    def get_ospf(self):

        return re.findall(r"router ospf (\S+)",self.config_text)