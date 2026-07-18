import pytest
from validators.interface_validator import Interfacevalidator

def test_interface_exist_and_Link_Status_None():
    #Test weather interface exist and lInk status is none.

    validator = Interfacevalidator([{
                "Name" : "FastEthernet0/1",
                "IP Address" : "10.0.2.2 255.255.255.252",
                "Link Status" : None
            }])
    result = validator.validate_interface()
    assert result == None


def test_interface_not_exist_and_Link_Status_None():
    #Test weather interface not exist and link status none.

    validator = Interfacevalidator([{
            "Name" : None,
            "IP Address" : "10.0.2.2 255.255.255.252",
            "Link Status" : None
        }])
    result = validator.validate_interface()
    assert result == " Interface name not found. "

def test_interface_exist_and_Link_Status_Shutdown():
    #Test weather interface exist and link status down.
    validator = Interfacevalidator([{
            "Name" : "FastEthernet0/1",
            "IP Address" : "10.0.2.2 255.255.255.252",
            "Link Status" : "shutdown"
        }])
    result = validator.validate_interface()
    assert result == "FastEthernet0/1 Link Status is DOWN. "

def test_interfcae_not_exist_and_Link_Status_Shutdown():
     #Test weather interface not exist and link status down.

    validator = Interfacevalidator([{
            "Name" : None,
            "IP Address" : "10.0.2.2 255.255.255.252",
            "Link Status" : "shutdown"
        }])
    result = validator.validate_interface()
    assert result == " Interface name not found.  Link Status is DOWN. "

