from parsi_io.modules.address_extractions import AddressExtraction
from static.enums import HidingText


class EmailHider:

    def __init__(self):
        self.extractor = AddressExtraction()

    def hide_emails(self, text):
        email_list = self.extractor.run(text)['email']
        for email in email_list:
            text = text.replace(email, HidingText.EMAIL_HIDING_TEXT.value, 1)
        return text
