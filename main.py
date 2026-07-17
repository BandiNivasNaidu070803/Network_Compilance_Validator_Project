from utils.file_reader import FileReader
from parser.config_parser import ConfigParser
from validators.hostname_validation import HostnameValidator
from validators.interface_validator import Interfacevalidator
from validators.ipaddress_validation import IPAddressvalidation

reader = FileReader("configs/R1.txt")
config = reader.read_config()
parser = ConfigParser(config)
extracted_details = parser.paser()
#print(extracted_details)


#Hostname validation.
hostname = HostnameValidator(extracted_details["Host Name"])
hostname_status = hostname.validate_hostname()
#check the status of hostname.
if hostname_status == "Host Name is valid":
    hostname_result = "PASS"
else:
    hostname = "FAIL" + hostname_status


#Interface validation.

interface = Interfacevalidator(extracted_details["Interfaces"])
interface_status = interface.validate_interface()
#check the status if interface
if interface_status == None:
    interface_result = "PASS"
else:
    interface_result = "FAIL " + interface_status




#IP Address validation.

ip_address = IPAddressvalidation(extracted_details["Interfaces"])
ip_address_status = ip_address.validate_ipaddress()
print(ip_address_status)
if ip_address_status == None:
    ip_address_result = "PASS"
else:
    ip_address_result = "FAIL " + ip_address_status


print("============================================================================\n")
print("                    Network Compliance Validation Report                    \n")
print("============================================================================\n")
print(" Router : ",extracted_details["Host Name"])
print("\n")
print(" Hostname Validation     :   ",hostname_result)
print(" Interface Validation    :   ",interface_result)
print(" IP Address validation   :   ",ip_address_result)

