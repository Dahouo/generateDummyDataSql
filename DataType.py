from enum import Enum


class DataType(Enum):
    """Enum for data types."""
    NAME = 0
    PHONE = 1
    EMAIL = 2
    ADDRESS = 3
    POSTAL_CODE = 4
    REGION = 5
    COUNTRY = 6
    WORD = 7
    TEXT = 8
    NUMBER = 9
    CURRENCY_CODE = 10
    ALPHA_NUMERIC = 11
    UUID = 12
    DATE = 13
    DATE_TIME = 14
    BOOLEAN = 15
    BINARY = 16
    BIT = 17
    UNIQUE_ID = 18
    AMOUNT = 19
    UUID_WITHOUT_HYPHEN = 20
