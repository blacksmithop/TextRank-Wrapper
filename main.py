from re import sub
from typing import Dict, List, Tuple
from nltk import sent_tokenize
import spacy
import pytextrank

class TextRank:
    def __init__(self, insights: List[str]):
        self.text = self.process_text(insights)

        self.stopwords_file = "./stopwords.txt"
        self.stopwords = self.load_stopwords()  # load stopwords

        self.load() # load Spacy nlp model

    def __str__(self):
        limit = 200
        text = self.text[:limit] + ".." * (len(self.text) > limit)

        return text

    def __repr__(self):
        limit = 200
        text = self.text[:limit] + ".." * (len(self.text) > limit)

        return text
    
    def load(self) -> None:
        self.nlp = spacy.load("en_core_web_sm")

        stopword_dict = {k: ["NOUN"] for k in self.stopwords}

        self.nlp.add_pipe("textrank", last=True, config={ "stopwords":stopword_dict})

    def load_stopwords(self) -> List[str]:
        stopwords: List[str] = []
        with open(self.stopwords_file, "r") as stopwords_file:
            for stopword in stopwords_file.read().splitlines():  # type: ignore
                stopwords.append(stopword.strip())

        return stopwords

    def process_text(self, insights) -> str:
        _text = " ".join(insights)
        text: str = sub(r"[ ]{2,}", " ", _text)

        return text
    
    def tokenize(self) -> List[str]:
        # _text = sub(r"(\.)[A-Z][a-z]+", " . ", self.text)
        sentences: List[str] = sent_tokenize(self.text) 
        sentences = [i.capitalize() for i in sentences if len(i.split()) <= 35]
        sentences = [sentence.replace("[^a-zA-Z0-9]"," ") for sentence in sentences]

        return sentences

    def summarize(self) -> Tuple[List[str], Dict[str, str]]:
        _text = "".join(self.tokenize())

        doc = self.nlp(_text)

        keyword_score = [(round(p.rank, 2), p.text) for p in doc._.phrases]
        keywords_topn = sorted(keyword_score, reverse=True)[:10]

        keywords = {v:k for k,v in keywords_topn if k>0}

        tr = doc._.textrank

        summaries = [str(sent).capitalize() for sent in tr.summary(limit_phrases=15, limit_sentences=5)]
        summaries = sorted(summaries, reverse=True)
            
        return summaries, keywords
    

if __name__ == "__main__":

    insights: List[str] = ['50%, if &lt;50%, I use Pembrolizumab combo even if PD-L1 negative.', 'Academic SL expressed that KN048 PFS2 data confirmed the use of Pembrolizumab monotherapy and Pembrolizumab + Chemo Therapy as 1st line therapy in RM HNSCC.', 'While P + A and N + I are considered SoC in 1L RCC, A + A is not at the same level.', '1L RCC: based in the published data, the Avelumab + Axitinib combination is not considered as a therapeutic option for the SL.', 'The treatment for adenocarcinoma with IO in combination with Chemo Therapy, would be for patients selected by PD-L1 expression (considering the results of CM649 and KN590)', 'It is going to impact my patients who I would have included in the clinical trials like LEAP 002 study (Pembrolizumab plus Lenvatinib).', 'I look at PD-L1 and make sure I have NGS in patients.', 'HCC, KN - 524 SL agrees that the combination of Lenvatinib and Pembrolizumab (KN - 524) looks promising in HCC and it could play a major role across GI cancers.', 'KN426_The efficacy results in the favorable risk group are not enough to make P + A the SoC in 1L for this patients population.', 'It might indicate that there might not be a survival benefit in this patient group for Pembrolizumab + Chemo arm.']

    tr = TextRank(insights=insights)
    print(tr.summarize())

