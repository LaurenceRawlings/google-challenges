import reader as r
import output as o
import numpy as np
import math

def calculate(dict):

    libraries = dict.get('libraries')

    book_scores = dict.get('book_scores')
    temp = []
    for score in book_scores:
        temp.append(int(score))
    book_scores = temp

    days = int(dict.get('days'))

    max_score = 0
    min_score = math.inf

    max_signup = 0
    min_signup = math.inf

    max_scanrate = 0
    min_scanrate = math.inf

    sharedBooks = []

    for library in libraries:
        books = library.get('books')
        total = 0
        for book in books:
            total += int(book_scores[int(book)])
            sharedBooks.append(book)

        sharedBooks = list(dict.fromkeys(sharedBooks))

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
        sharedCount = 1

        if (max_score - min_score == 0):
            a = 100
        else:
            a = (library.get('book_score') / (max_score - min_score)) * 100

        if (max_signup - min_signup == 0):
            b = 100
        else:
            b = 100 - ((int(library.get('signup')) / (max_signup - min_signup)) * 100)

        if (max_scanrate - min_scanrate == 0):
            c = 100
        else:
            c = (int(library.get('scanrate')) / (max_scanrate - min_scanrate)) * 100

        total_score = (a + b + c) / 3

        #library.update( {'total_score' : total_score} )

        for book in library.get('books') :
            for sharedBook in sharedBooks :
                if book == sharedBook :
                    sharedCount += 1

        total_score = total_score * sharedCount

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
                scores = []
                for book in books:
                    scores.append(book_scores[int(book)])
                books_with_scores = sorted(zip(scores, books), reverse=True)

                scanned = 0
                while scanned < int(library.get('scanrate')):
                    if (len(books_with_scores) > 0):
                        if not (books_with_scores[0][1] in completed_books):
                            library.get('book_queue').append(books_with_scores[0][1])
                            completed_books.append(books_with_scores[0][1])
                            scanned += 1
                        library.get('books').remove(books_with_scores[0][1])
                        books_with_scores = books_with_scores[1:]
                    else:
                        scanned = int(library.get('scanrate'))
                
        

        signup_timer -= 1
        if (signup_timer == 0):
            signup_in_progress = False
            registered.append(library_queue[0])
            library_queue = library_queue[1:]

    return registered



print('Start')
read = r.Reader('input/a_example.txt')
out = o.Output('output/a_example_out.txt')
out(calculate(read()))
print('Finished A')

read = r.Reader('input/b_read_on.txt')
out = o.Output('output/b_read_on_out.txt')
out(calculate(read()))
print('Finished B')

read = r.Reader('input/c_incunabula.txt')
out = o.Output('output/c_incunabula_out.txt')
out(calculate(read()))
print('Finished C')

read = r.Reader('input/d_tough_choices.txt')
out = o.Output('output/d_tough_choices_out.txt')
#out(calculate(read()))
print('Finished D')

read = r.Reader('input/e_so_many_books.txt')
out = o.Output('output/e_so_many_books_out.txt')
out(calculate(read()))
print('Finished E')

read = r.Reader('input/f_libraries_of_the_world.txt')
out = o.Output('output/f_libraries_of_the_world_out.txt')
out(calculate(read()))
print('Finished F')