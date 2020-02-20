class Reader:

    def __init__(self, path):
        self.path = path
    
    def __call__(self):
        with open(self.path, 'r') as file:
            lines = file.readlines()
            dict = {
                'videos': [],
                'endpoints': [],
                'requests': [],
                'caches': [],
                'cache_max': 0
            }

            info = lines[0].split(' ')
            videos = lines[1].split(' ')

            for i in range(0, len(videos)):
                dict.get('videos').append((i, int(videos[i])))

            line = 2
            endpoints = {}
            for i in range(0, int(info[1])):
                endpoint = lines[line].split(' ')
                for j in range(0, endpoint[1]):
                    line += 1

            


            



        return dict