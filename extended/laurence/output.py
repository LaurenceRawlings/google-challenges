class Output:

    def __init__(self, path):
        self.path = path
    
    def __call__(self, libraries):
        with open(self.path, 'w') as f:
            output = str(len(libraries)) + '\n'

            for library in libraries:
                book_queue = library.get('book_queue')
                queue_length = len(book_queue)
                currentBook = 0

                if not (queue_length == 0):
                    output = output + str(library.get('id')) + ' ' + str(queue_length) + '\n'
                
                for book in book_queue:
                    if (currentBook < queue_length - 1):
                        output = output + book + ' '
                        currentBook += 1
                    else:
                        output = output + str(book) + '\n'

            f.write(output)