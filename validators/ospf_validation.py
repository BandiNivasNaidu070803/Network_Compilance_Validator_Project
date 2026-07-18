#OSPF Validation.
import re
class OSPFValidation:

    def __init__(self, ospf):
        self.ospf = ospf
    
    def validate_ospf(self):
        #print(self.ospf)
        result = ""
        if self.ospf["process_id"] == None :
            result = result + " Poccess id Missing"
        elif type(self.ospf["process_id"]) == int:
            result = result
        for i in range(0, len(self.ospf["Networks"])):
            extract_network_id = re.search(r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b",self.ospf["Networks"][i].split(" ")[0])
            if extract_network_id:
                result = result
            else:
                result = result + self.ospf["Networks"][i] +  " Network Is Incorrect. "
            
        return result
    
