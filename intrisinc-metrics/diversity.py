import nltk
import math
from nltk.metrics import edit_distance

class DiversityMetrics:
    #constructor
    def __init__(self, text):
        self.text = text
        self.tokens = self.tokenize(text)
        self.type_token_ratio = self.type_token_ratio()
        self.hapax_legomena_ratio = self.hapax_legomena_ratio()
        self.simpson_index = self.simpson_index()
        self.entropy = self.entropy()
        self.mean_edit_distance = self.mean_edit_distance()

    def tokenize(self, text):
        tokens = nltk.word_tokenize(self.text)
        return tokens
    
    def type_token_ratio(self):
        """
        Calculates the Type-Token Ratio for the given text, which is calculated by dividing the number of unique words (types) in a text by the total number of words (tokens) in that text. 
        Higher scores indicate greater diversity.
        Scores between 0.2 and 0.4 are considered "low", 0.4 to 0.6 is "moderate" and 0.6 and above is "high".
        """
        self.type_token_ratio = len(set(self.tokens)) / len(self.tokens)
        return self.type_token_ratio
    
    def hapax_legomena_ratio(self):
        """
        Calculates the Hapax Legomena Ratio for the given text, which measures the ratio of the number of unique words (i.e., hapax legomena) to the total number of words in a text.
        Higher scores indicate greater diversity.
        In general, a HLR score of around 50% is considered average for most types of texts.
        """
        self.hapax_legomena_ratio = sum([1 for freq in nltk.FreqDist(self.tokens).values() if freq == 1]) / len(self.tokens)
        return self.hapax_legomena_ratio
    
    def simpson_index(self):
        """
        Calculates the Simpson Index for the given text.
        Higher scores indicate greater diversity.
        """
        self.simpson_index = sum([(freq/len(self.tokens)) * ((freq-1)/(len(self.tokens)-1)) for freq in nltk.FreqDist(self.tokens).values()])
        return self.simpson_index
    
    def entropy(self):
        """
        Calculates the Entropy for the given text.
        Higher scores indicate greater diversity.
        """
        self.entropy = -sum([(freq/len(self.tokens)) * math.log(freq/len(self.tokens)) for freq in nltk.FreqDist(self.tokens).values()])
        return self.entropy
    
    def mean_edit_distance(self):
        """
        Calculates the Mean Edit Distance for the given text.
        Higher scores indicate greater diversity.
        """
        self.mean_edit_distance = sum([edit_distance(w1, w2) for i, w1 in enumerate(self.tokens) for w2 in self.tokens[i+1:]]) / (len(self.tokens) * (len(self.tokens) - 1) / 2)
        return self.mean_edit_distance
    
    def herdans_c(self):
        ttr = math.log(len(nltk.FreqDist(self.tokens)) / math.sqrt(len(self.tokens)))
        return ttr
    
    # print override
    def __str__(self):
        return f'Diversity scores:\n   Type-Token Ratio: {self.type_token_ratio}\n   Hapax Legomena Ratio: {self.hapax_legomena_ratio}\n   Simpson Index: {self.simpson_index}\n   Entropy: {self.entropy}\n   Mean Edit Distance: {self.mean_edit_distance}\n\n'