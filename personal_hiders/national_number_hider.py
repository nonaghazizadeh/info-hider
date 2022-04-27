import re
from static.enums import HidingText


class NationalNumberHider:
    def __init__(self):
        self.pre_keywords = ['شماره‌ملی', 'شماره‌شناسنامه', 'کد‌ملی']
        self.en_national_number_regex = "[01223456789]{1,10}"
        self.persian_national_number_regex = "[\u06F0-\u06F9]{1,10}"

    @staticmethod
    def find_keyword(text, keywords):
        for keyword in keywords:
            if keyword in text:
                return True
        return False

    def is_national_code_exists(self, text):
        if re.search(self.persian_national_number_regex, text) is not None:
            return True, re.search(self.persian_national_number_regex, text).span()
        elif re.search(self.en_national_number_regex, text) is not None:
            return True, re.search(self.en_national_number_regex, text).span()
        return False, ''

    def find_national_code(self, text):
        founded, span = self.is_national_code_exists(text)
        if founded:
            start_idx = span[0]
            end_idx = span[1]
            prev_text = text[:start_idx]
            for keyword in self.pre_keywords:
                if keyword in prev_text:
                    return start_idx, end_idx
            return
        return

    def hide_national_code(self, text):
        res = self.find_national_code(text)
        if res is not None:
            return text.replace(text[res[0]:res[1]], HidingText.NATIONAL_NUMBER_HIDING_TEXT.value)
        return text
