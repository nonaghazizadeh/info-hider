from static.enums import HidingText,Keywords


class GenderHider:
    def __init__(self):
        self.genders = Keywords.GENDERS_KEYWORDS.value

    def check_gender(self, inp):
        for gender in self.genders:
            if gender in inp:
                return True, gender
        return False, ''

    def hide_gender(self, text):
        founded, gender = self.check_gender(text)
        if founded:
            return text.replace(gender, HidingText.GENDER_HIDING_TEXT.value)
        return text
