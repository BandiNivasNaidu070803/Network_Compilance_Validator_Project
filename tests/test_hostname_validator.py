import pytest
from validators.hostname_validation import HostnameValidator

def test_valid_hostname():
    #Test that a valid hostname passes validation.
    validator = HostnameValidator("R1")

    result = validator.validate_hostname()

    assert result == "Host Name is valid"

def test_valid_hostname_Router():
    validator = HostnameValidator("Router")

    result = validator.validate_hostname()

    assert result == "Host Name is valid"

def test_unavailable_hostname():
    #Test the is hostname empty.
    validator = HostnameValidator(" ")
    result = validator.validate_hostname()

    assert result == "Host Name Unavailable"

def test_hostname_starting_with_lowercase():
    #Test the invalid hostname.
    validator = HostnameValidator("r1")
    result = validator.validate_hostname()

    assert result == "Host Name should start with 'R'"

def test_hostname_StartingWithNumber():
    #Testing hostname starts with number.
    validator = HostnameValidator("1R")
    result = validator.validate_hostname()

    assert result == "Host Name should start with 'R'"

def test_hostname_StartingWithChar():
    #Testing hostname starts with number.
    validator = HostnameValidator("$R")
    result = validator.validate_hostname()

    assert result == "Host Name should start with 'R'"



