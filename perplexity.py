import nltk
from nltk.lm import MLE, Vocabulary

# Generate a list of sentences from the generated text
generated_text = "This is a sample sentence. This is another sample sentence."
sentences = generated_text.split(". ")

# Tokenize each sentence and add the resulting list of tokens to a new list
corpus = [nltk.word_tokenize(sentence.lower()) for sentence in sentences]

# Generate a vocabulary from the corpus
words = [word for sentence in corpus for word in sentence]
vocab = Vocabulary(words, unk_cutoff=1)

# Train a unigram language model using the maximum likelihood estimation method
unigram_model = MLE(1, vocab)
unigram_model.fit(corpus)

# Generate a test sentence to calculate perplexity
test_sentence = "This is a test sentence."

# Convert the test sentence to a list of tokens
test_tokens = nltk.word_tokenize(test_sentence.lower())

# Calculate perplexity for the test sentence
perplexity = unigram_model.perplexity(test_tokens)

print("Perplexity:", perplexity)