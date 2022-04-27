from enum import Enum


class HidingText(Enum):
    EMAIL_HIDING_TEXT = " <#email_address#> "
    ADDRESS_HIDING_TEXT = " <#address#> "
    DATE_HIDING_TEXT = " <#date#> "
    PERSON_NAME_HIDING_TEXT = " <#person_name#> "
    PHONE_HIDING_TEXT = " <#phone#> "
    NATIONAL_NUMBER_HIDING_TEXT = " <#national_number#> "
    COMPANY_HIDING_TEXT = " <#company_name#> "


class Regex(Enum):
    EMAIL_REGEX = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"


class Path(Enum):
    FIRST_NAME_PATH = 'data/first_names.json'
    LAST_NAME_PATH = 'data/last_names.json'
    COMPANIES_PATH = 'data/companies.json'


class CrawlUrl(Enum):
    BASE_URL = ''
    FIRST_NAME_URL = ''
    LAST_NAME_URL = ''
