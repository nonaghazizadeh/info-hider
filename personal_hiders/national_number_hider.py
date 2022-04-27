import re
from static.enums import HidingText,Keywords,Regex


class NationalNumberHider:
    def __init__(self):
        self.pre_keywords = Keywords.NATIONAL_NUMBER_PRE_KEYWORDS.value
        self.en_national_number_regex = Regex.EN_NATIONAL_NUMBER_REGEX.value
        self.fa_national_number_regex = Regex.FA_NATIONAL_NUMBER_REGEX.value

    @staticmethod
    def find_keyword(text, keywords):
        for keyword in keywords:
            if keyword in text:
                return True
        return False

    def is_national_code_exists(self, text):
        if re.search(self.fa_national_number_regex, text) is not None:
            return True, re.search(self.fa_national_number_regex, text).span()
        elif re.search(self.en_national_number_regex, text) is not None:
            return True, re.search(self.en_national_number_regex, text).span()
        return False, ''

    def find_national_code(self, inp):
        founded, span = self.is_national_code_exists(inp)
        if founded:
            start_idx = span[0]
            end_idx = span[1]
            prev_text = inp[:start_idx]
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
