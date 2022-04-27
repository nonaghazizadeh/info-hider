from personal_hiders.address_hider import AddressHider
from personal_hiders.email_hider import EmailHider
from personal_hiders.date_hider import DateHider
from personal_hiders.name_hider import NameHider
from personal_hiders.phone_number_hider import PhoneNumberHider
from personal_hiders.company_hider import CompanyHider
from personal_hiders.national_number_hider import NationalNumberHider
from personal_hiders.gender_hider import GenderHider
from static.enums import Path
from hazm import *

file = open(Path.INPUT_FILE.value, 'r', encoding="utf-8")
text = file.read()
file.close()

text = EmailHider().hide_emails(text)
text = GenderHider().hide_gender(text)
normalizer = Normalizer()
text = normalizer.normalize(text)
text = CompanyHider().hide_company_name(text)
text = DateHider().hide_dates(text)
text = AddressHider().hide_address(text)
text = NameHider().hide_person_name(text)
text = NationalNumberHider().hide_national_code(text)
text = PhoneNumberHider().hide_phones(text)
text = GenderHider().hide_gender(text)

with open(Path.OUTPUT_FILE.value, 'w', encoding="utf-8") as file:
    file.write(text)
