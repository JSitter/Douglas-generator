from flask import Flask
import sys
from random import random
import time

app = Flask(__name__)
@app.route('/')
def start():
    return stochastic_sample("douglas1.txt", 10)

def stochastic_sample(filename, sentence_length):
    words = get_words_from_text(filename)
    histogram = create_histogram(words)
    total_words = len(words)
    place_holder = 0

    

    for item in histogram:
        place_holder += histogram[item]/total_words
        histogram[item] = place_holder
        
    count = 0
    sentence = ""
    for count in range(sentence_length):
        random_number = random()
        
        for item in histogram:
            
            if  random_number <= histogram[item]:
                sentence = sentence + item + " "
                break
    return sentence

 

def create_histogram(word_list):
    '''
        Create Histogram of word frequency in file
    '''
    histogram = {}

    for word in word_list:
        word = sanitize(word)
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

def get_words_from_text(filename):
    '''
        Get words from text file
    '''
    with open(filename, 'r') as f:
        text = f.read()

    return text.split(" ")
        
def sanitize(word):
    '''
        Clean words and return *filtered* for content to remove
    '''
    if word == "\n":
        word = "*filtered*"
    
    word = word.strip(". ,:\r\n\"\t\!\?").lower()
    
    return word
'''
if __name__ == "__main__":
    default_file_name = 'small_sample_text.txt'

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = default_file_name
    
    if len(sys.argv) > 2:
        sentence_len = int(sys.argv[2])
    else:
        sentence_len = 5
    start_time = int(round(time.time()*1000))
    print(stochastic_sample(filename, sentence_len))
    end_time = int(round(time.time()*1000))
    print("Ran in {}ms".format(end_time - start_time))
'''