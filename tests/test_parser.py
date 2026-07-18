import pytest
from parser.config_parser import ConfigParser

sample_config = """Building configuration...

Current configuration : 811 bytes
!
version 12.2
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname R1
!
!
!
!
!
!
!
!
ip cef
no ipv6 cef
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
interface FastEthernet0/0
 ip address 10.0.1.1 255.255.255.252
 duplex auto
 speed auto
!
interface FastEthernet1/0
 ip address 10.0.2.1 255.255.255.252
 shutdown
!
interface Serial2/0
 no ip address
 shutdown
!
interface Serial3/0
 no ip address
 shutdown
!
interface FastEthernet4/0
 no ip address
 shutdown
!
interface FastEthernet5/0
 no ip address
 shutdown
!
router ospf 1
 log-adjacency-changes
 network 10.0.1.0 0.0.0.3 area 0
 network 10.0.2.0 0.0.0.3 area 0
!
ip classless
!
ip flow-export version 9
!
!
!
!
!
!
!
!
line con 0
!
line aux 0
!
line vty 0 4
 login
!
!
!
end"""

def test_hostname_parser():
    parser = ConfigParser(sample_config)
    result = parser.parser()
    assert result["Host Name"] == "R1"

def test_interface_paser():
    parser = ConfigParser(sample_config)
    result = parser.parser()
    assert result["Interfaces"][0]["Name"] == "FastEthernet0/0"
    assert result["Interfaces"][1]["Name"] == "FastEthernet1/0"

def test_IPaddress_parser():
    parser = ConfigParser(sample_config)
    result = parser.parser()
    assert result["Interfaces"][0]["IP Address"] == "10.0.1.1 255.255.255.252"
    assert result["Interfaces"][1]["IP Address"] == "10.0.2.1 255.255.255.252"

def test_Status():
    parser = ConfigParser(sample_config)
    result = parser.parser()
    assert result["Interfaces"][0]["Link Status"] == None
    assert result["Interfaces"][1]["Link Status"] == "shutdown"

def test_ospf_process_id():
    parser = ConfigParser(sample_config)
    result = parser.parser()
    assert result["OSPF"]["process_id"] == 1

def test_ospf_networks():
    parser = ConfigParser(sample_config)
    result = parser.parser()
    assert result["OSPF"]["Networks"][0] == "10.0.1.0 0.0.0.3 area 0"
    assert result["OSPF"]["Networks"][1] == "10.0.2.0 0.0.0.3 area 0"

    