from parsi_io.modules.address_extractions import AddressExtraction
from static.enums import HidingText


class AddressHider:

    def __init__(self):
        self.extractor = AddressExtraction()

    @staticmethod
    def anonymous_text(text, data):
        ans = ""
        last_span = 0
        spans = data['address_span']
        for idx, address in enumerate(data['address']):
            span = (spans[2 * idx], spans[(2 * idx) + 1])
            if text[span[0]:span[1]] == HidingText.ADDRESS_HIDING_TEXT.value:
                continue
            ans += text[last_span:span[0]] + HidingText.ADDRESS_HIDING_TEXT.value
            last_span = span[1]
        return ans + text[last_span:]

    def hide_address(self, text):
        return self.anonymous_text(text, self.extractor.run(text))
