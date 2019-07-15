from nltk.corpus import stopwords
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

#Import summarizers
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.kl import KLSummarizer

class OriginalTextHandler:
    def __init__(self, original_text):
        #Cache stopwords in set to improve lookup time
        self.stop_words = set(stopwords.words('english'))
        self.stop_words.update(["’", ",", "—"])
        #Initialize parser
        self.original_text = original_text
        self.parser = PlaintextParser.from_string(original_text, Tokenizer("english"))

    def luhn_summarize(self):
        summarizer = LuhnSummarizer()
        summarizer.stop_words = self.stop_words
        summary_tuple = (summarizer(self.parser.document, 4))
        luhn_summary = " ".join(map(str, summary_tuple))
        return luhn_summary

    def lsa_summarize(self):
        summarizer = LsaSummarizer()
        summarizer.stop_words = self.stop_words
        summary_tuple = (summarizer(self.parser.document, 4))
        lsa_summary = " ".join(map(str, summary_tuple))
        return lsa_summary
    
    def lex_rank_summarize(self):
        summarizer = LexRankSummarizer()
        summarizer.stop_words = self.stop_words
        summary_tuple = (summarizer(self.parser.document, 4))
        lex_rank_summary = " ".join(map(str, summary_tuple))
        return lex_rank_summary

    def kl_summarize(self):
        summarizer = KLSummarizer()
        summarizer.stop_words = self.stop_words
        summary_tuple = (summarizer(self.parser.document, 4))
        kl_summary = " ".join(map(str, summary_tuple))
        return kl_summary        

    def summarize(self):
        return [self.luhn_summarize(), self.lsa_summarize(), self.lex_rank_summarize(), self.kl_summarize()]



        

