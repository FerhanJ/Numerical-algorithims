import random 

#takes a text file and converts it into a list of words
def file2list(filename):
    fp = open(filename)
    total_words = []
    for line in fp:
        word_list = line.split()
        total_words = total_words + word_list
    return total_words

#get n consecutive words from a list starting from index i in the list
def getWords(word_list, i, n=1): 
    words = ''
    for x in range(n):
        if x < n - 1:
            words += word_list[i + x] + ' '
        else:
            words += word_list[i + x]
    return words

#takes a list of words and returns a dictionary, d, with prefix keys and n sufixes as values
def return_suffix(all_words, n): 
    d = {} 
    i = 0
    for word in all_words:
        i += 1
        if i <= len(all_words) - n:
            d.setdefault(word, []).append(getWords(all_words, i, n))
    return d

#takes the dictionary d from previous function, a starting suffix called word and creates a sentence of length n
def markov(d, word, n=10):
    print(word, end=' ')
    for i in range(n):
        selected = random.choice(d[word])
        word = selected.split()[-1]
        print(selected, end=' ')