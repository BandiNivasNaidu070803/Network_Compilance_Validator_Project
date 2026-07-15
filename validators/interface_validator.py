import re
class InterfaceValidator:
    def validate(self,config):
        results = []
        interfaces = re.findall(r"interface (.+?)(?=\ninterface|\Z)",config,re.S)
        for interface in interfaces:
            lines = interface.strip().splitlines()
            interface_name = lines[0].strip()
            interface_text = "\n".join(lines)
            errors =[]
            if "description" not in interface_text:
                errors.append("Missing description")
            if "ip address" not in interface_text:
                errors.append("Missing Ip address")
            if "shutdown" in interface_text and "no shutdown" not in interface_text:
                errors.append("Interface is shutdown")
            if errors:
                results.append({"interface":interface_name,"status":"FAIL","ip address":ip_errors":errors})
            else:
                results.append({"interface":interface_name,"status":"PASS"})
        return results
        
