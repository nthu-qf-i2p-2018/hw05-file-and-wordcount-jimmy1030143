
# coding: utf-8

# In[1]:

import csv
import json
import pickle
from collections import Counter
import string

def main(filename):
    lines = open(filename).readlines()

    all_words = []

    for line in lines:
        words = line.split()     
        for word in words:
            for a in string.punctuation:
                if a in word:
                    if((word.index(a) == len(word) - 1) | (word.index(a) == 0)):
                        word = word.replace(a, "")
                 
            if word:
                all_words.append(word)

    counter = Counter(all_words)

    with open("wordcount.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file)        
        writer.writerow(['word', 'count'])
        writer.writerows(counter.most_common())

    with open("wordcount.json", "w") as json_file:
        writer = json.dump(counter.most_common(), json_file)
  
    with open("wordcount.pkl", "wb") as pkl_file:
        writer = pickle.dump(counter.most_common(), pkl_file)

if __name__ == '__main__':
    main("i_have_a_dream.txt")
