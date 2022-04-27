from parsi_io.modules.address_extractions import AddressExtraction
from static.enums import HidingText,Keywords
import convert_numbers


class PhoneNumberHider:

    def __init__(self):
        self.extractor = AddressExtraction()
        self.keywords = Keywords.PHONE_NUMBER_PRE_KEYWORDS.value

    def check_keywords(self, text):
        for keyword in self.keywords:
            if keyword in text:
                return True
        return False

    def hide_phones(self, inp):
        phone_list = self.extractor.run(inp)['number']
        prev_idx = 0
        if len(phone_list) != 0:
            spans = self.extractor.run(inp)['number_span']
            it = iter(spans)
            tuple_span = list(zip(it, it))
            for i, span in enumerate(tuple_span):
                if i != 0:
                    prev_idx = tuple_span[i - 1][1]
                start_idx = span[0]
                end_idx = span[1]
                if self.check_keywords(inp[prev_idx:start_idx]):
                    inp = inp.replace(inp[start_idx:end_idx], HidingText.PHONE_HIDING_TEXT.value)

        return inp
