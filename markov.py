import random 

#takes a text file and converts it into a list of words
def file2list(filename):
    fp = open(filename)
    total_words = []
    for line in fp:
        word_list = line.split()
        total_words = total_words + word_list
    return total_words

#string n consecutive words from word_list, a list, starting from index i in the list
def getWords(word_list, i, n=1): 
    words = '' #words is a string to hold our list elements
    for x in range(n):
        if x < n - 1:
            words += word_list[i + x] + ' ' #add the (i + x)th word to our string and repeat n times
        else:
            words += word_list[i + x]
    return words

#takes a list of words and returns a dictionary, d, with prefix keys and n sufixes as values
def return_suffix(all_words, n): 
    d = {} 
    i = 0 #i is the index of the word after our chosen prefix
    for word in all_words: #word is our dictionary key, ie our prefix
        i += 1
        if i <= len(all_words) - n: #this stops index out of range errors
            d.setdefault(word, []).append(getWords(all_words, i, n)) #append a string of n words to our list of suffix values for d[word]
    return d

#takes the dictionary d from previous function, a starting prefix called word and creates a sentence of length n
def markov(d, prefix, n=10):
    print(prefix, end=' ') #print our prefix to start the sentence
    for i in range(n):
        selected = random.choice(d[prefix]) #d[prefix] returns a list of suffixes. This code picks a random value from that list
        prefix = selected.split()[-1] #our new prefix is the last word of our suffix
        print(selected, end=' ') #print the selected suffixes
