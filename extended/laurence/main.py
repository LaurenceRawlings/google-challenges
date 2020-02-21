import reader as r
import output as o

import math

files = ['a_example']

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
        for library in next_book.get('libraries'):
            libraries.append(dict.get('libraries')[library])
        library = min(libraries, key=lambda i:i['signup'])
        
        if not (library in signed_up):
            signup_queue.append(library)
        library.get('book_queue').append(next_book.get('id'))
        
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