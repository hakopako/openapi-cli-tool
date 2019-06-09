

class Route:

    def __init__(self, method, url, file, spec={}):
        self.method = method
        self.url = url
        self.file = file
        self.spec = spec
