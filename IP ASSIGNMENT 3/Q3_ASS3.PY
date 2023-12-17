
import random
import string

word_count = {}
words = []

def score_assignment(s):
    sentence_count = s.count('.') + s.count('!') + s.count('?')
    word_count = len(s.split())
    short_sentences = len([sentence for sentence in s.split('.') if len(sentence.split()) < 5])
    long_sentences = len([sentence for sentence in s.split('.') if len(sentence.split()) >= 20])
    punctuation_count = sum(1 for c in s if c in string.punctuation)
    
    f1_score = f1(len(words), word_count)
    f2_score = f2(sum(word_count[word] for word in words[:5]), word_count)
    f3_score = f3(short_sentences, long_sentences, sentence_count)
    f4_score = f4(punctuation_count, word_count)
    
    return (0.25 * f1_score + 0.25 * f2_score + 0.25 * f3_score + 0.25 * f4_score) * 100

def f1(unique_words, total_words):
    return unique_words / total_words

def f2(top_five_count, total_words):
    return top_five_count / total_words

def f3(short_sentences, long_sentences, total_sentences):
    return (short_sentences + long_sentences) / total_sentences

def f4(punctuation_count, total_words):
    return punctuation_count / total_words

def count_unique_words(s):
    s = s.lower()
    for word in s.split():
        if word not in words:
            words.append(word)
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

n = int(input("Enter the number of files: "))

for i in range(1, n+1):
    filename = "FILE" + str(i) + ".txt"
    with open(filename, "r") as file:
        s = file.read()
        score = score_assignment(s)
        with open("scores.txt", "a") as out:
            out.write(filename + "\n")
            out.write("score: " + str(score) + "\n")
            
            count_unique_words(s)
            words.sort(key=lambda x: word_count[x], reverse=True)
            
            out.write("Top 5 most used words: \n")
            for j in range(5):
                if j >= len(words):
                    break
                out.write(words[j] + ": " + str(word_count[words[j]]) + "\n")
                
            random.shuffle(words)
            out.write("Random 5 words: \n")
            for j in range(5):
                if j >= len(words):
                    break
                out






