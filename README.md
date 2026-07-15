# Network_Compilance_Validator_Project
Network Compliance and Configuration Validation Framework

# Extracted details format.
extracted_details ={
            "Host Name" : None,
            "Interfaces": [],
            "OSPF" : {
                "process_id" : None,
                "Networks" : None
            }
        }

# Final output.

==========================================
 Network Compliance Validation Report
==========================================

Router : R1

Hostname Validation       : PASS
Interface Validation      : PASS
IP Validation             : PASS
OSPF Validation           : PASS
Duplicate IP Validation   : PASS

Overall Status            : PASS
Compliance Score          : 100%
------------------------------------------

Router : R2

Hostname Validation       : PASS
Interface Validation      : FAIL
    - FastEthernet0/1 : Description Missing

IP Validation             : PASS
OSPF Validation           : PASS
Duplicate IP Validation   : PASS

Overall Status            : FAIL
Compliance Score          : 80%
------------------------------------------