import textstat

class ReadabilityMetrics:
    # Flesch Reading Ease
    def flesch_reading_ease(self, text):
        """
        Calculates the Flesch Reading Ease score for the given text.
        Higher scores indicate greater readability.
        Taking into account zerozero.pt's target audience, a score of 50 or lowe is considered "difficult to read".
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


text = "No futebol, há determinados momentos que, passe o tempo que passar, são impossíveis de esquecer. O golo de Kelvin, no final da época de 12/13, é, claramente, um deles. Numa altura em que o Benfica estava perto de segurar um empate que quase lhe dava o título, o extremo apareceu para decidir uma Liga, numa história hollywoodesca."

metrics = ReadabilityMetrics()

print(metrics.flesch_reading_ease(text))
print(metrics.gunning_fog(text))
print(metrics.coleman_liau_index(text))
print(metrics.automated_readability_index(text))
