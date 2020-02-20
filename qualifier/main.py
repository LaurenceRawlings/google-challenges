import reader as r
import output as o
import numpy as np
import math

### Input and Process ###
read = r.Reader('input/a_example.txt')
dict = read()

libraries = dict.get('libraries')

book_scores = dict.get('book_scores')
temp = []
for score in book_scores:
    temp.append(int(score))
book_scores = temp

days = int(dict.get('days'))

print(dict)

max_score = 0
min_score = math.inf

max_signup = 0
min_signup = math.inf

max_scanrate = 0
min_scanrate = math.inf

for library in libraries:
    books = library.get('books')
    total = 0
    for book in books:
        total += int(book_scores[int(book)])

    library.update({'book_score' : total} )

    if (total > max_score):
        max_score = total
    if (total < min_score):
        min_score = total
    
    if (int(library.get('signup')) > max_signup):
        max_signup = int(library.get('signup'))
    if (int(library.get('signup')) < min_signup):
        min_signup = int(library.get('signup'))

    if (int(library.get('scanrate')) > max_scanrate):
        max_scanrate = int(library.get('scanrate'))
    if (int(library.get('scanrate')) < min_scanrate):
        min_scanrate = int(library.get('scanrate'))

for library in libraries:
    a = (library.get('book_score') / (max_score - min_score)) * 100
    b = 100 - ((int(library.get('signup')) / (max_signup - min_signup)) * 100)
    c = (int(library.get('scanrate')) / (max_scanrate - min_scanrate)) * 100

    total_score = (a + b + c) / 3

    library.update( {'total_score' : total_score} )


library_queue = sorted(libraries, key=lambda i:i['total_score'], reverse=True)

#### Algorithm ###
registered = []
completed_books = []
signup_in_progress = False
signup_timer = 0

for day in range(0, days):
    if (signup_in_progress == False):
        if (len(library_queue) > 0):
            signup_in_progress = True
            signup_timer = int(library_queue[0].get('signup'))

    if (len(registered) > 0):
        for library in registered:
            books = library.get('books')

            
    

    signup_timer -= 1
    if (signup_timer == 0):
        signup_in_progress = False
        registered.append(library_queue[0])
        library_queue = library_queue[1:]

### Output ###
out = o.Output('output/a_example_out.txt')
out(registered)