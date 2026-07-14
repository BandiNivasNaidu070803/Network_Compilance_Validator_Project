from utils.file_reader import FileReader
from parser.config_parser import ConfigParser

reader = FileReader("configs/R1.txt")
config = reader.read_config()
parser = ConfigParser(config)
print("Hostname :",parser.get_hostname())
print("Interface :",parser.get_interface())
print("OSPF :",parser.get_ospf())