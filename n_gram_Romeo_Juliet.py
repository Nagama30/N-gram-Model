import numpy as np
import random

def read_data(file_name):
	file = open(file_name, "r")
	content = file.read()
	file.close()
	return content

def is_alphabet(ch):
	if ch >= 'a' and ch <= 'z':
		return True
	return ch >= 'A' and ch <= 'Z'

def clean_content(content):
	for idx in range(len(content)):
		if not is_alphabet(content[idx]):
			content[idx] = '_'
	return content

def get_words(content):
	words = []
	i = 0
	while i < len(content):
		if content[i] == '_':
			i += 1
			continue
		word = ''
		j = i
		while j < len(content):
			if content[j] != '_':
				word += content[j]
				j += 1
			else:
				break
		i += len(word)
		words.append(word.lower())
	return words

content = list(read_data("Romeo_and_Juliet.txt"))
content = clean_content(content)
words = get_words(content)
vocab = list(set(words))
vocab.sort()

# print('Vocabulary:', vocab)
print('Size of vocabulary:', len(vocab))

N = len(vocab)

# This is a matrix capturing the conditional probability p(word | context).
# We apply the 1-Markov assumption so that the context is only a single word.
prob = np.zeros((N, N))

for i in range(len(words) - 1):
	idx_1 = vocab.index(words[i])
	idx_2 = vocab.index(words[i + 1])
	prob[idx_1, idx_2] += 1

# Note: The ChatGPT works in the same manner - Autoregressive.
# Generate a new sentence with a starting word.

# Convert counts to probabilities
for i in range(N):
    row_sum = np.sum(prob[i, :])
    if row_sum > 0:
        prob[i, :] /= row_sum

# Sentence generation with sampling
def generate_sentence(start_word, L=100):
    current = start_word.lower()
    if current not in vocab:
        print(f"Word '{start_word}' not in vocabulary.")
        return ""
    
    sentence = current + ' '
    
    for _ in range(L - 1):
        idx = vocab.index(current)
        
        # Sample the next word based on probabilities
        if np.sum(prob[idx, :]) == 0:
            print("No following words.")
            break
            
        next_idx = np.random.choice(N, p=prob[idx, :])
        next_word = vocab[next_idx]
        
        sentence += next_word + ' '
        current = next_word
    
    return sentence

# Generate sentences with different starting words
for start_word in ["Romeo", "Juliet", "Love"]:
    sentence = generate_sentence(start_word, L=100)
    print(f"\nSentence starting with '{start_word}':\n{sentence}")

print('Done')