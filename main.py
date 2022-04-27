from personal_hiders.address_hider import AddressHider
from personal_hiders.email_hider import EmailHider
from personal_hiders.date_hider import DateHider
from personal_hiders.name_hider import NameHider
from personal_hiders.phone_number_hider import PhoneNumberHider
from personal_hiders.company_hider import CompanyHider
from personal_hiders.national_number_hider import NationalNumberHider
import convert_numbers

text = NationalNumberHider().hide_national_code('شماره‌ملی من 09312')
print(text)
