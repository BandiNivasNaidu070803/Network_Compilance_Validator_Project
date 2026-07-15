from utils.file_reader import FileReader
from parser.config_parser import ConfigParser
from validators.hostname_validation import HostnameValidator
from validators.interface_validator import InterfaceValidator

reader = FileReader("configs/R1.txt")
config = reader.read_config()
parser = ConfigParser(config)
hostname = parser.get_hostname()
interface = parser.get_interface()
ospf = parser.get_ospf()
validate_hostname = HostnameValidator(hostname)
print(hostname)
hostname_validation = validate_hostname.validate_hostname()
validate_interface = InterfaceValidator()
interface_validation = validate_interface.validate(config)

print("\n========== Interface Validation Report ==========")

for result in interface_validation:
    print(f"\nInterface : {result['interface']}")
    print(f"Status    : {result['status']}")
    print(f"Ip address : {result['ip address']}")

    if result["errors"]:
        print("Errors:")
        for error in result["errors"]:
            print(f"  - {error}")
    else:
        print("Errors    : None")
