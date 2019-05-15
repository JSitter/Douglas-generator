# Second Order Refactor
This code was written to keep track of the following word by using an index. 

Three Refactoring items from the list:
1. Improve Class Structure: Refactor MarkovChain method into separate file.

2. Improve Naming: Use the Enumerate function instead of updating indexes.

3. Add Comments


Where can the code be changed?
In `app.py` the MarkovChain class is declared along with the flask route information. This Class should be removed from the flask server and separated into it's own file.

In MarkovChain.generate_second_order_markov_structure() it keeps track of a pointer to generate the window. This pointer can be taken care of by refactoring it to use the enumerate function.

In addition to these things this method could use some additional comments.
