class HostnameValidator:
    def __init__(self,hostname):
        self.hostname = hostname

    def validate_hostname(self):
        if self.hostname[0] == " ":
            print("Host Name Unavailable")
            
        else:
            if self.hostname[0][0] == "R" :
                print("Host Name is valid")
            else:
                print("Host Name should start with 'R'")
        