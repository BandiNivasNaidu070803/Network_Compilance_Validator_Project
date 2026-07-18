from validators.ipaddress_validation import IPAddressvalidation
import pytest

def test_valid_ipaddress():
    #Test Valid ipaddress 10.0.2.2
    validator = IPAddressvalidation([{
            "Name" : "FastEthernet0/1",
            "IP Address" : "10.0.2.2 255.255.255.252",
            "Link Status" : "shutdown"
        }])
    result = validator.validate_ipaddress()
    assert result == ""


def test_invalid_ipaddress():
    #Test inValid ipaddress 256.0.2.2
    validator = IPAddressvalidation([{
            "Name" : "FastEthernet0/1",
            "IP Address" : "256.0.2.2 255.255.255.252",
            "Link Status" : "shutdown"
        }])
    result = validator.validate_ipaddress()
    assert result == "256.0.2.2 255.255.255.252 Incorrect IP address. "


def test_wrong_format_ipaddress():
#Test inValid ipaddress 256.0.2.2
    validator = IPAddressvalidation([{
            "Name" : "FastEthernet0/1",
            "IP Address" : "10.0.2.2255.255.255.252",
            "Link Status" : "shutdown"
        }])
    result = validator.validate_ipaddress()
    assert result == "10.0.2.2255.255.255.252 Incorrect IP address. "


def test_include_char_in_ipaddress():
#Test invalid ipaddress with char A.0.2.2
    validator = IPAddressvalidation([{
            "Name" : "FastEthernet0/1",
            "IP Address" : "A.0.2.2 255.255.255.252",
            "Link Status" : "shutdown"
        }])
    result = validator.validate_ipaddress()
    assert result == "A.0.2.2 255.255.255.252 Incorrect IP address. "


def test_include_splchar_in_ipaddress():
#Test invalid ipaddress with splchar $.0.2.2
    validator = IPAddressvalidation([{
            "Name" : "FastEthernet0/1",
            "IP Address" : "$.0.2.2 255.255.255.252",
            "Link Status" : "shutdown"
        }])
    result = validator.validate_ipaddress()
    assert result == "$.0.2.2 255.255.255.252 Incorrect IP address. "


def test_incomplete_ipaddress():
    #Test incomplete ipaddress 10.0.2
    validator = IPAddressvalidation([{
            "Name" : "FastEthernet0/1",
            "IP Address" : "10.0.2 255.255.255.252",
            "Link Status" : "shutdown"
        }])
    result = validator.validate_ipaddress()
    assert result == "10.0.2 255.255.255.252 Incorrect IP address. "


def test_allzero_ipaddress():
    #Test ipaddress 0.0.0.0
    validator = IPAddressvalidation([{
            "Name" : "FastEthernet0/1",
            "IP Address" : "0.0.0.0 255.255.255.252",
            "Link Status" : "shutdown"
        }])
    result = validator.validate_ipaddress()
    assert result == "0.0.0.0 255.255.255.252 Incorrect IP address. "


def test_incomplete_octate_ipaddress():
    #Test if ipaddress having incomplete octate
    validator = IPAddressvalidation([{
            "Name" : "FastEthernet0/1",
            "IP Address" : "10.0.2. 255.255.255.252",
            "Link Status" : "shutdown"
        }])
    result = validator.validate_ipaddress()
    assert result == "10.0.2. 255.255.255.252 Incorrect IP address. "







