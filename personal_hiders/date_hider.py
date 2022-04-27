from parstdex import Parstdex
from static.enums import HidingText,Keywords


class DateHider:
    hiding_text = HidingText.DATE_HIDING_TEXT.value

    def __init__(self):
        self.model = Parstdex()
        self.pre_keywords = Keywords.DATE_PRE_KEYWORDS.value
        self.post_keywords = Keywords.DATE_POST_KEYWORDS.value

    @staticmethod
    def find_keyword(text, keywords):
        for keyword in keywords:
            if keyword in text:
                return True
        return False

    @staticmethod
    def anonymous_text(text, spans):
        ans = ""
        last_span = 0
        for span in spans:
            if text[span[0]:span[1]] == HidingText.DATE_HIDING_TEXT.value:
                continue
            ans += text[last_span:span[0]] + HidingText.DATE_HIDING_TEXT.value
            last_span = span[1]
        return ans + text[last_span:]

    def extract_day_spans(self, text, spans):
        final_spans = []
        for span in spans:
            if self.find_keyword(text[max(0, span[0] - 25):span[0]], self.pre_keywords) or self.find_keyword(
                    text[span[1]: min(len(text), span[1] + 25)],
                    self.post_keywords):
                final_spans.append(span)
        return final_spans

    def hide_dates(self, text):
        return self.anonymous_text(text, self.extract_day_spans(text, self.model.extract_span(text)['datetime']))
