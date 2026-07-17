#We are extracting hostname, 
import re

class ConfigParser:
    def __init__(self, config_text):
        self.config_text = config_text
    def paser(self):
        
        extracted_details ={
            "Host Name" : None,
            "Interfaces": [],
            "OSPF" : {
                "process_id" : None,
                "Networks" : None
            }
        }

        #Extracting Hostname.
        match = re.search(r"^hostname\s+(\S+)", self.config_text, re.MULTILINE)
        extracted_details["Host Name"] = match.group(1)

        #Extracting Interface Block.
        interface_block = re.findall(r"^interface\s+(\S+)([\s\S]*?)(?=!)",self.config_text,re.MULTILINE)

        #Creating Interface Block.
        for name, discrption in interface_block:
            #Extracting IP address.
            discrption = discrption.strip()
            ip_address = re.search(r"ip address\s(\S+\s+\S+)", discrption)
            if ip_address:
                ip = ip_address.group(1)
            else:
                ip = None
            
            #Extract Status of interface.
            shutdown_status = re.search(r"shutdown", discrption, re.MULTILINE)
            if shutdown_status:
                shutdown = shutdown_status.group(0)
            else:
                shutdown = None
    
            #Adding elements to the block

            interface_block = {
                "Name" : name,
                "IP Address" : ip,
                "Link Status" : shutdown
            }
        #Insert block into extracted_details only which are having ip address.   
            if interface_block["IP Address"]:
                extracted_details["Interfaces"].append(interface_block)

        #Extract OSPF.
        processor_id = re.findall(r"router ospf (\S+)", self.config_text, re.MULTILINE)
        
        if len(processor_id)==1:
            extracted_details["OSPF"]["process_id"] = int(processor_id[0])
        else:
            extracted_details["OSPF"]["process_id"] = None
        
        #Extract Network_Block.
        Network_block = re.findall(r"^\s*network\s+(\S+\s+\S+\s+area\s+\d+)", self.config_text, re.MULTILINE)
        
        #Insert Network_Block into extracted_details.
        extracted_details["OSPF"]["Networks"] = Network_block

        return extracted_details
        #print(extracted_details)
