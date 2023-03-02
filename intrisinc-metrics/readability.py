import textstat

class ReadabilityMetrics:
    # constructor
    def __init__(self, text):
        self.text = text
        self.flesch_reading_ease = self.flesch_reading_ease(text)
        self.gunning_fog = self.gunning_fog(text)
        self.coleman_liau_index = self.coleman_liau_index(text)
        self.automated_readability_index = self.automated_readability_index(text)

    # Flesch Reading Ease
    def flesch_reading_ease(self, text):
        """
        Calculates the Flesch Reading Ease score for the given text.
        Higher scores indicate greater readability.
        Taking into account zerozero.pt's target audience, a score of 50 or lower is considered "difficult to read".
        """
        return textstat.flesch_reading_ease(text)

    # Gunning Fog Index
    def gunning_fog(self, text):
        """
        Calculates the Gunning Fog Index score for the given text.
        Higher scores indicate greater difficulty.
        Taking into account zerozero.pt's target audience, a score of 16 or higher is considered "difficult to read".
        """
        return textstat.gunning_fog(text)

    # Coleman-Liau Index
    def coleman_liau_index(self, text):
        """
        Calculates the Coleman-Liau Index score for the given text.
        Higher scores indicate greater difficulty.
        Taking into account zerozero.pt's target audience, a score of 12 or higher is considered "difficult to read".
        """
        return textstat.coleman_liau_index(text)

    # Automated Readability Index (ARI)
    def automated_readability_index(self, text):
        """
        Calculates the Automated Readability Index (ARI) score for the given text.
        Higher scores indicate greater difficulty.
        Taking into account zerozero.pt's target audience, a score of 12 or higher is considered "difficult to read".
        """
        return textstat.automated_readability_index(text)
    
    # print override
    def __str__(self):
        return f'Readibility scores:\n   Flesch Reading Ease: {self.flesch_reading_ease}\n   Gunning Fog Index: {self.gunning_fog}\n   Coleman-Liau Index: {self.coleman_liau_index}\n   Automated Readability Index: {self.automated_readability_index}\n\n'
