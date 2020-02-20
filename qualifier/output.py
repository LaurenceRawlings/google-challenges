class Output:

    def __init__(self, path):
        self.path = path
    
    def __call__(self, libraries):
        f = open(self.path, 'w')

        outputText = str(len(libraries)) + '\n'

        for library in libraries :
            bookQueue = library.get('book_queue')
            queueLength = len(bookQueue)
            currentBook = 0

            outputText = outputText + str(library.get('id')) + ' ' + str(queueLength) + '\n'
            
            for book in bookQueue :
                if currentBook < queueLength - 1 :
                    outputText = outputText + book + ' '
                    currentBook += 1
                else :
                    outputText = outputText + book + '\n'

        f.write(outputText)
        f.close