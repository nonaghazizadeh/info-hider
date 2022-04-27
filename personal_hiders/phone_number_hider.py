from parsi_io.modules.address_extractions import AddressExtraction
from static.enums import HidingText
import convert_numbers


class PhoneNumberHider:

    def __init__(self):
        self.extractor = AddressExtraction()

    def hide_phones(self, text):
        phone_list = self.extractor.run(text)['number']
        for phone in phone_list:
            text = text.replace(phone, HidingText.PHONE_HIDING_TEXT.value, 1)
            text = text.replace(convert_numbers.english_to_persian(phone), HidingText.PHONE_HIDING_TEXT.value, 1)
        return text
