from utils.file_reader import FileReader
from parser.config_parser import ConfigParser
from validators.hostname_validation import HostnameValidator
from validators.interface_validator import Interfacevalidator


reader = FileReader("configs/R1.txt")
config = reader.read_config()
parser = ConfigParser(config)
extracted_details = parser.paser()
#print(extracted_details)

#Hostname validation.
hostname = HostnameValidator(extracted_details["Host Name"])
hostname_status = hostname.validate_hostname()
print(hostname_status)

#Interface validation.
interface = Interfacevalidator(extracted_details["Interfaces"])
inteface_status = interface.validate_interface()
