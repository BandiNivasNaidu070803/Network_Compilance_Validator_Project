import re
class IPAddressvalidation:

    def __init__(self, interfaces):
        self.interfaces = interfaces

    def validate_ipaddress(self):
        result = ""
        pattern = r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b"
        for i in range(0,len(self.interfaces)):
            extract_ip_address = re.search(pattern,self.interfaces[i]["IP Address"].split(" ")[0])
            if extract_ip_address ==  None:
                result = result + self.interfaces[i]["IP Address"] + " Incorrect IP address. "
            else:
                result = result
        return result 