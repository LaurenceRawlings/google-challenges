class Reader:

    def __init__(self, path):
        self.path = path
    
    def __call__(self):
        with open(self.path, 'r') as f:
            lines = f.read().split('\n')
            dict = {
                'books': [],
                'libraries': [],
                'days': 0
            }

            info = lines[0].split(' ')
            books = lines[1].split(' ')

            for i in range(0, len(books)):
                dict.get('books').append({
                    'id': i,
                    'score': int(books[i]),
                    'libraries': []
                })

            dict.update( {'days' : int(info[2])} )

            line = 2
            for i in range(0, int(info[1])):
                library = lines[line].split(' ')
                line += 1

                books = lines[line].split(' ')
                for book in books:
                    dict.get('books')[int(book)].get('libraries').append(i)

                dict.get('libraries').append({
                    'id': i, 
                    'signup': int(library[1]), 
                    'scanrate': int(library[2]),
                    'book_queue': []
                    })
                
                line += 1

        return dict