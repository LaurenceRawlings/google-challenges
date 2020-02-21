import reader as r
import output as o

import math

files = ['a_example']
#files = ['a_example', 'b_read_on', 'c_incunabula', 'd_tough_choices', 'e_so_many_books', 'f_libraries_of_the_world']

def calc(dict):
    signed_up = []
    signup_queue = []
    signup_timer = 0

    books = sorted(dict.get('books'), key=lambda i:i['score'], reverse=True)

    for day in range(0, dict.get('days')):
        if (len(books) > 0):
            next_book = books.pop()
        else:
            return signed_up
        
        libraries = []
        available_libraries = []
        for library in next_book.get('libraries'):
            libraries.append(dict.get('libraries')[library])
            if (library in signed_up):
                available_libraries.append(library)
        
        if not (len(available_libraries) > 0):
            library = min(libraries, key=lambda i:i['signup'])
            signup_queue.append(library)
        else:
            library = min(libraries, key=lambda i:i['scanrate'])
            library.get('book_queue').append(next_book.get('id'))

        for library in signed_up:
            stock = sorted(library.get('books'), key=lambda i:i['score'], reverse=True)

            ##############################
        
        if (signup_timer <= 0):
            if (len(signup_queue) > 0):
                if (day > 0):
                    signed_up.append(signup_queue.pop())
                signup_timer = signup_queue[0].get('signup')
        else:
            signup_timer -= 1

    return signed_up

for f in files:
    read = r.Reader(f'input/{f}.txt')
    out = o.Output(f'output/{f}_out.txt')
    out(calc(read()))