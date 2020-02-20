class Reader:

    def __init__(self, path):
        self.path = path
    
    def __call__(self):
        with open(self.path, 'r') as file:
            lines = file.read().split('\n')
            dict = {
                'book_scores': [],
                'libraries': [],
                'days': 0
            }

            info = lines[0].split(' ')
            dict.update( {'book_scores' : lines[1].split(' ')} )
            dict.update( {'days' : info[2]} )

            line = 2
            for i in range(0, int(info[1])):
                library = lines[line].split(' ')
                line += 1
                dict.get('libraries').append( {
                    'id': i, 
                    'signup': library[1], 
                    'scanrate': library[2], 
                    'books': lines[line].split(' ')
                    } )
                line += 1

        return dict