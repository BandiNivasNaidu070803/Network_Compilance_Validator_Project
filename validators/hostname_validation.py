class HostnameValidator:
    def __init__(self,hostname):
        self.hostname = hostname

    def validate_hostname(self):
        if self.hostname[0] == " ":
            return "Host Name Unavailable"
            
        else:
            if self.hostname[0][0] == "R" :
                return "Host Name is valid"
            else:
                return "Host Name should start with 'R'"
        