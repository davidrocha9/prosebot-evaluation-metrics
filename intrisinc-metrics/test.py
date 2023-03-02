from readability import ReadabilityMetrics
from diversity import DiversityMetrics
from coherence import CoherenceMetrics

# read file text.txt and store it on new variable text
with open('text.txt', 'r') as file:
    text = file.read()

# create a new instance of ReadabilityMetrics
readability_metrics = ReadabilityMetrics(text)
diversity_metrics = DiversityMetrics(text)
coherence_metrics = CoherenceMetrics(text)


# print the results
print(readability_metrics)
print(diversity_metrics)
print(coherence_metrics)