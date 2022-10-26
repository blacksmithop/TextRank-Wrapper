from re import sub
from typing import List


class TextRank:
    def __init__(self, insights: List[str]):
        self.text = self.process_text(insights)

        self.stopwords_file = "./stopwords.txt"
        self.stopwords = self.load_stopwords()  # load stopwords

    def __str__(self):
        limit = 200
        text = self.text[:limit] + ".." * (len(self.text) > limit)

        return text

    def __repr__(self):
        limit = 200
        text = self.text[:limit] + ".." * (len(self.text) > limit)

        return text

    def load_stopwords(self) -> List[str]:
        stopwords: List[str] = []
        with open(self.stopwords_file, "r") as stopwords_file:
            for stopword in stopwords_file.splitlines():  # type: ignore
                stopwords.append(stopword.strip())

        return stopwords

    def process_text(self, insights) -> str:
        _text = " ".join(insights)
        text: str = sub(r"[ ]{2,}", " ", _text)

        return text

    def summarize(self):
        pass
