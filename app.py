from flask import Flask
import random
import time
import pprint
from markov_chain import MarkovChain

import sys
import filewrangler as fw
from threading import Thread
print("Loading Corpus ...")
start_time = int(round(time.time()*1000))
corpus1 = fw.create_corpus("corpus1.txt")
print("first corpus loaded")
corpus2 = fw.create_corpus("corpus2.txt")
print("second corpus loaded")
corpus3 = fw.create_corpus("corpus3.txt")
print("third corpus loaded")
corpus4 = fw.create_corpus("corpus4.txt")
print("fourth corpus loaded")
corpus5 = fw.create_corpus("corpus5.txt")
print("last corpus loaded")

corpus = corpus1 + corpus2
morecorpus = corpus3 + corpus4

end_time = int(round(time.time()*1000))
time_delta = end_time - start_time
print("\nFinished in {}ms.".format(time_delta))

print("Creating Markov Chain...")
start_time = int(round(time.time()))
#Create markovchain datastructure in memory
markov_chain = MarkovChain(corpus)
end_time = int(round(time.time()))
print("\nMarkov structure generated in {}s.".format(end_time-start_time))
    

app = Flask(__name__)

@app.route("/")
def index():
    start_time = int(round(time.time()*1000))
    sentence = markov_chain.walk(7)
    end_time = int(round(time.time()*1000))
    print("\nGenerated sentence in {}ms.".format(end_time-start_time))
    return sentence
    # return "Noice"

# print("Name: ")
# print(__name__)
if __name__ == "__main__":
    app.run()



