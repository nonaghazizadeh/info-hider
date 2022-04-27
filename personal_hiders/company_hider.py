import json
from static.enums import Path, HidingText


class CompanyHider:
    def __init__(self):
        self.companies = self.open_read_files(Path.COMPANIES_PATH.value)
        self.pre_keywords = ['شرکت', 'سازمان', 'موسسه']

    @staticmethod
    def open_read_files(path):
        file = open(path, 'r', encoding="utf-8")
        ans = json.loads(file.read())
        file.close()
        return ans

    def is_company_name_exist(self, text):
        for name in self.companies:
            if name in text:
                return True, name
        return False, ''

    def find_company_name(self, inp):
        founded, company_name = self.is_company_name_exist(inp)
        if founded:
            start_idx = inp.find(company_name)
            end_idx = start_idx + len(company_name)
            prev_text = inp[:start_idx]
            for keyword in self.pre_keywords:
                if keyword in prev_text:
                    return start_idx, end_idx
            return
        return

    def hide_company_name(self, text):
        res = self.find_company_name(text)
        if res is not None:
            return text.replace(text[res[0]:res[1]], HidingText.COMPANY_HIDING_TEXT.value)
        return text
