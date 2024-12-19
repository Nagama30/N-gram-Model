# N-gram Model

1. Clean the data
- In clean_content function, it checks each character in the text and replaces 
any non-letter characters with underscores to mark the spaces between words.

2. Construct the vocabulary.  
- In get_words function, it goes through the cleaned content and splits words 
based on underscores, collecting them as lowercase words in a list words. 
The vocab list contains all unique words, arranged in alphabetical order.

3. Compute the probabilities p(word) and p(word | context). We assume the 1-Markov 
assumption.
- The prob matrix is a square matrix of size [N, N], where N is the number of 
unique words. Each entry prob[i, j] holds the probability of word j following 
word i. The program counts how often each word follows another, then 
converts these counts into probabilities by dividing each row by its total, 
assuming only the previous word affects the next.

4. Generate sentences with length L = 100 autoregressively with the following first 
words:  
• Romeo  
• Juliet  
• Love 
- In generate_sentence function, it generates a sentence starting with 
start_word. In each iteration, it samples the next word based on the 
probability distribution in prob[idx, :]. If the row sum is zero (indicating no 
known follow-up words), it stops generating the sentence.

![image](https://github.com/user-attachments/assets/91e9f4b5-111a-48d9-803f-b82984a750de)



