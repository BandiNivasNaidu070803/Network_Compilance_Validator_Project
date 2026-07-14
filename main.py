from utils.file_reader import FileReader
from parser.config_parser import ConfigParser
from validators.hostname_validation import HostnameValidator


reader = FileReader("configs/R1.txt")
config = reader.read_config()
parser = ConfigParser(config)
hostname = parser.get_hostname()
interface = parser.get_interface()
ospf = parser.get_ospf()
validate_hostname = HostnameValidator(hostname)
print(hostname)
hostname_validation = validate_hostname.validate_hostname()
