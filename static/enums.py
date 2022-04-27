from enum import Enum


class HidingText(Enum):
    EMAIL_HIDING_TEXT = " <#email_address#> "
    ADDRESS_HIDING_TEXT = " <#address#> "
    DATE_HIDING_TEXT = " <#date#> "
    PERSON_NAME_HIDING_TEXT = " <#person_name#> "
    PHONE_HIDING_TEXT = " <#phone#> "
    NATIONAL_NUMBER_HIDING_TEXT = " <#national_number#> "
    COMPANY_HIDING_TEXT = " <#company_name#> "
    GENDER_HIDING_TEXT = " <#gender_name> "


class Keywords(Enum):
    COMPANY_PRE_KEYWORDS = ['بنیاد', 'نهاد', 'شرکت', 'سازمان', 'اداره', 'موسسه']
    GENDERS_KEYWORDS = ['همجنس‌گرا', 'دوحنس‌گرا', 'تراجنس‌گرا', 'پسر', 'مرد', 'دختر', 'زن']
    NATIONAL_NUMBER_PRE_KEYWORDS = ['شماره‌ملی', 'شماره‌شناسنامه', 'کد‌‌ملی']
    DATE_PRE_KEYWORDS = ['ولادت', 'مرگ', 'تولد', 'متولد']
    DATE_POST_KEYWORDS = ['به دنیا', 'چشم به جهان گشود', 'مرد', 'چشم از دنیا بست', 'زاده', 'متولد شد']
    PHONE_NUMBER_PRE_KEYWORDS = ['شماره منزل', 'شماره همراه', 'تلفن منزل', 'تلفن همراه', 'تلفن', 'موبایل',
                                 'شماره موبایل']


class Regex(Enum):
    EMAIL_REGEX = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    EN_NATIONAL_NUMBER_REGEX = "[01223456789]{1,10}"
    FA_NATIONAL_NUMBER_REGEX = "[\u06F0-\u06F9]{1,10}"


class Path(Enum):
    FIRST_NAME_PATH_READ = 'data/first_names.json'
    LAST_NAME_PATH_READ = 'data/last_names.json'
    COMPANIES_PATH_READ = 'data/companies.json'
    FIRST_NAME_PATH_WRITE = '../data/first_names.json'
    LAST_NAME_PATH_WRITE = '../data/last_names.json'
    COMPANIES_PATH_WRITE = '../data/companies.json'
    INPUT_FILE = "input.txt"
    OUTPUT_FILE = "output.txt"


class CrawlUrl(Enum):
    BASE_URL = 'https://fa.wikipedia.org'
    FIRST_NAME_URL = 'https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D9%86%D8%A7%D9%85%E2%80%8C%D9%87%D8%A7%DB%8C_%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%DB%8C'
    LAST_NAME_URL = 'https://fa.wikipedia.org/w/index.php?title=%D8%B1%D8%AF%D9%87:%D9%86%D8%A7%D9%85%E2%80%8C%D9%87%D8%A7%DB%8C_%D8%AE%D8%A7%D9%86%D9%88%D8%A7%D8%AF%DA%AF%DB%8C&pageuntil=%D8%AA%D8%B1%DB%8C%D8%A7%D9%86#mw-pages'
    IRANIAN_FIRST_COMPANY_URL = "http://ircreative.isti.ir/contents.php?cntid=112"
    IRANIAN_SECOND_COMPANY_URL = "http://ircreative.isti.ir/contents.php?cntid=853"
    OTHERS_COMPANY_URL = "https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D8%B1%DA%A9%D8%AA%E2%80%8C%D9%87%D8%A7%DB%8C_%D8%A2%D9%85%D8%B1%DB%8C%DA%A9%D8%A7%DB%8C%DB%8C"
