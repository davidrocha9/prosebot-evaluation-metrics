import nltk

# Define the generated text
generated_text = "Lionel Messi scored two goals in Barcelona's victory over Real Madrid. The Argentinian striker was in top form and dominated the match."

# Tokenize the generated text
tokens = nltk.word_tokenize(generated_text)

# Calculate the type-token ratio
type_token_ratio = len(set(tokens)) / len(tokens)

# Print the type-token ratio
print("Type-token ratio:", type_token_ratio)






import nltk

# Define the generated text
generated_text = "Lionel Messi scored two goals in Barcelona's victory over Real Madrid. The Argentinian striker was in top form and dominated the match."

# Tokenize the generated text
tokens = nltk.word_tokenize(generated_text)

# Calculate the Hapax Legomena Ratio (HLR)
frequencies = nltk.FreqDist(tokens)
hapax_legomena = sum([1 for freq in frequencies.values() if freq == 1])
hlr = hapax_legomena / len(tokens)

# Print the HLR
print("HLR:", hlr)







import nltk

# Define the generated text
generated_text = "Lionel Messi scored two goals in Barcelona's victory over Real Madrid. The Argentinian striker was in top form and dominated the match."

# Tokenize the generated text
tokens = nltk.word_tokenize(generated_text)

# Calculate the Simpson's Index
frequencies = nltk.FreqDist(tokens)
word_count = len(tokens)
s_index = sum([(freq/word_count) * ((freq-1)/(word_count-1)) for freq in frequencies.values()])

# Print the Simpson's Index
print("Simpson's Index:", s_index)








import nltk
import math

# Define the generated text
generated_text = "Lionel Messi scored two goals in Barcelona's victory over Real Madrid. The Argentinian striker was in top form and dominated the match."

# Tokenize the generated text
tokens = nltk.word_tokenize(generated_text)

# Calculate the Entropy
frequencies = nltk.FreqDist(tokens)
word_count = len(tokens)
entropy = -sum([(freq/word_count) * math.log(freq/word_count) for freq in frequencies.values()])

# Print the Entropy
print("Entropy:", entropy)










from nltk.metrics import edit_distance

# Define the generated text
generated_text = "Lionel Messi scored two goals in Barcelona's victory over Real Madrid. The Argentinian striker was in top form and dominated the match."

# Tokenize the generated text
tokens = nltk.word_tokenize(generated_text)

# Calculate the Mean Edit Distance
med_sum = sum([edit_distance(w1, w2) for i, w1 in enumerate(tokens) for w2 in tokens[i+1:]])
med = med_sum / (len(tokens) * (len(tokens) - 1) / 2)

# Print the Mean Edit Distance
print("Mean Edit Distance:", med)








import nltk
import math

# Define the generated text
generated_text = "Lionel Messi scored two goals in Barcelona's victory over Real Madrid. The Argentinian striker was in top form and dominated the match."

# Tokenize the generated text
tokens = nltk.word_tokenize(generated_text)

# Calculate the TTR-based metric using Herdan's C
frequencies = nltk.FreqDist(tokens)
word_count = len(tokens)
ttr = len(frequencies) / math.sqrt(word_count)
herdan_c = math.log(ttr)

# Print Herdan's C
print("Herdan's C:", herdan_c)
