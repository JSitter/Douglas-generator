def test_second_order():
  from markov_chain import MarkovChain
  corpus = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
  mc = MarkovChain(corpus)
  sentence = mc.walk(4)
  assert len(sentence.split(' ')) == 4