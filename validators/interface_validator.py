import re
class Interfacevalidator:
    #assigning interfaces in routers.
    def __init__(self, interfaces):
        self.interfaces = interfaces
    #validation of interface.
    
    def validate_interface(self):
        #print(self.interfaces)
        
        #print(len(self.interfaces))
        result = ""
        for i in range(0,len(self.interfaces)):
            #To Validate interface name.
            if self.interfaces[i]["Name"]:
                result = result
            else:
                result = result  + " Interface name not found. "
            #To validate Link Status.
            
            if self.interfaces[i]["Link Status"] ==  None:
                result = result
            elif self.interfaces[i]["Link Status"] ==  "shutdown" and self.interfaces[i]["Name"] == None:
                result = result + " Link Status is DOWN. " 
            elif self.interfaces[i]["Link Status"] ==  "shutdown":
                result = result + self.interfaces[i]["Name"] + " Link Status is DOWN. "
            

        if result == "":
            return None
        else:
            return result
            

                
                        
        
    