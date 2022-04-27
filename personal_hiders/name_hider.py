import json
import re
from static.enums import HidingText, Path


class NameHider:
    def __init__(self):
        self.last_names = self.convert_list_to_regex(self.open_read_files(Path.LAST_NAME_PATH_READ.value))
        self.first_names = self.convert_list_to_regex(self.open_read_files(Path.FIRST_NAME_PATH_READ.value))
        self.name_regex = f"(^|\W)(((({self.first_names})(\W+))+({self.last_names}))|({self.last_names})|({self.first_names}))($|\W)"

    @staticmethod
    def convert_list_to_regex(inp_list):
        ans = ''
        for inp in inp_list:
            ans += inp + "|"
        ans = ans[:-1]
        return ans

    @staticmethod
    def open_read_files(path):
        file = open(path, 'r', encoding="utf-8")
        ans = json.loads(file.read())
        file.close()
        return ans

    def find_name(self, inp):
        ans = []
        for keyword_count in range(10, 0, -1):
            for matched in re.finditer(self.name_regex.format(), inp):
                inp = inp[:matched.span()[0]] + '' * (matched.span()[1] - matched.span()[0]) + inp[matched.span()[1]:]
                ans.append(matched)
        return ans

    def hide_person_name(self, text):
        for i in self.find_name(text):
            text = text.replace(i.group(), HidingText.PERSON_NAME_HIDING_TEXT.value)
        return text
