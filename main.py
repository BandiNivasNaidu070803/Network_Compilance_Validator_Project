from utils.file_reader import FileReader
from parser.config_parser import ConfigParser
from validators.hostname_validation import HostnameValidator
from validators.interface_validator import Interfacevalidator
from validators.ipaddress_validation import IPAddressvalidation
from validators.ospf_validation import OSPFValidation

files = [
    "R1.txt",
    "R2.txt",
    "R3.txt",
    "R4.txt",
    "R5.txt",
    "R6.txt",
    "R7.txt"
]
for router in files:
    reader = FileReader(f"configs/{router}")
    config = reader.read_config()
    parser = ConfigParser(config)
    extracted_details = parser.parser()

    #Hostname validation.
    hostname = HostnameValidator(extracted_details["Host Name"])
    hostname_status = hostname.validate_hostname()
    #check the status of hostname.
    if hostname_status == "Host Name is valid":
        hostname_result = "PASS"
    else:
        hostname_result = "FAIL " + hostname_status


    #Interface validation.
    interface = Interfacevalidator(extracted_details["Interfaces"])
    interface_status = interface.validate_interface()
    #check the status if interface
    if interface_status is None:
        interface_result = "PASS"
    else:
        interface_result = "FAIL " + interface_status




    #IP Address validation.
    ip_address_result = ""
    if extracted_details["Interfaces"] == []:
        ip_address_result = "FAIL No ip address"
    else:
        ip_address = IPAddressvalidation(extracted_details["Interfaces"])
        ip_address_status = ip_address.validate_ipaddress()
        print(ip_address_status)
        if ip_address_status == "":
            ip_address_result = "PASS"
        else:
            ip_address_result = "FAIL " + ip_address_status

    #OSPF validation.
    ospf = OSPFValidation(extracted_details["OSPF"])
    ospf_status = ospf.validate_ospf()
    if ospf_status == "":
        ospf_result = "PASS"
    else:
        ospf_result = "FAIL " + ospf_status


    #Overall Status.
    overall_status = ""
    if hostname_result == "PASS" and  interface_result == "PASS" and ip_address_result == "PASS" and ospf_result == "PASS":
        overall_status = "PASS"
    else:
        overall_status = "FAIL"

    #compilance score.
    passed = 0

    if hostname_result == "PASS":
        passed += 1

    if interface_result == "PASS":
        passed += 1

    if ip_address_result == "PASS":
        passed += 1

    if ospf_result == "PASS":
        passed += 1

    compliance_score = f"{int((passed / 4) * 100)} %"


    print("============================================================================")
    print("                    Network Compliance Validation Report                    ")
    print("============================================================================")
    print(" Router : ",extracted_details["Host Name"])
    print("\n")
    print(" Hostname Validation     :   ",hostname_result)
    print(" Interface Validation    :   ",interface_result)
    print(" IP Address validation   :   ",ip_address_result)
    print(" OSPF validation         :   ",ospf_result)
    print()
    print(" Overall Status          :   ",overall_status)
    print(" Compilance Score        :   ",compliance_score)
    print("============================================================================")


