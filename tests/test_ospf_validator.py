from validators.ospf_validation import OSPFValidation
import pytest

def test_valid_process_id():
    validator = OSPFValidation({
                "process_id" : 1,
                "Networks" : ["10.0.1.0"]
            })
    result = validator.validate_ospf()
    assert result == ""

def test_missing_process_id():
    validator = OSPFValidation({
                "process_id" : None,
                "Networks" : ["10.0.1.0"]
            })
    result = validator.validate_ospf()
    assert result == " Poccess id Missing"

def test_valid_network():
    validator = OSPFValidation({
                "process_id" : 1,
                "Networks" : ["10.0.1.0"]
            })
    result = validator.validate_ospf()
    assert result == ""

def test_wrong_network():
    validator = OSPFValidation({
                "process_id" : 1,
                "Networks" : ["256.0.1.0"]
            })
    result = validator.validate_ospf()
    assert result == "256.0.1.0 Network Is Incorrect. "

def test_char_network():
    validator = OSPFValidation({
                "process_id" : 1,
                "Networks" : ["A.0.1.0"]
            })
    result = validator.validate_ospf()
    assert result == "A.0.1.0 Network Is Incorrect. "

def test_splchar_network():
    validator = OSPFValidation({
                "process_id" : 1,
                "Networks" : ["$.0.1.0"]
            })
    result = validator.validate_ospf()
    assert result == "$.0.1.0 Network Is Incorrect. "

def test_incomplete_network():
    validator = OSPFValidation({
                "process_id" : 1,
                "Networks" : ["20.0.0"]
            })
    result = validator.validate_ospf()
    assert result == "20.0.0 Network Is Incorrect. "

def test_valid_two_network():
    validator = OSPFValidation({
                "process_id" : 1,
                "Networks" : ["10.0.1.0","10.0.2.0"]
            })
    result = validator.validate_ospf()
    assert result == ""

def test_second_network_is_invalid():
    validator = OSPFValidation({
                "process_id" : 1,
                "Networks" : ["10.0.1.0","256.0.2.0"]
            })
    result = validator.validate_ospf()
    assert result == "256.0.2.0 Network Is Incorrect. "

    