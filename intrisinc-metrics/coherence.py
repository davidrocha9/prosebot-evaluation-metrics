import spacy
import nltk

nlp = spacy.load('pt_core_news_md')

class CoherenceMetrics:
    # constructor
    def __init__(self, text):
        self.text = text
        self.average_similarity_score = self.average_similarity_score(text)

    # Average similarity score
    def average_similarity_score(self, text):
        """
        Calculates the average similarity score between the sentences in the given text.
        Higher scores indicate greater coherence.
        Taking into account zerozero.pt's target audience, a score of 0.5 or higher is considered "coherent".
        """
        # split text into sentences using nltk
        sentences = nltk.sent_tokenize(text)

        # compute the cosine similarity between each pair of sentences
        similarity_scores = []
        for i in range(len(sentences)):
            for j in range(i+1, len(sentences)):
                similarity = nlp(sentences[i]).similarity(nlp(sentences[j]))
                similarity_scores.append(similarity)

        # compute the average similarity score
        avg_similarity_score = sum(similarity_scores) / len(similarity_scores)

        return avg_similarity_score
    
    # print override
    def __str__(self):
        return f'Coherence score:\n   Average similarity score: {self.average_similarity_score}\n\n'