

class Route:

    def __init__(self, method, url, file, spec={}):
        self.method = method
        self.url = url
        self.file = file
        self.spec = spec

    def __repr__(self):
        return 'method='+self.method+' url='+self.url+' file='+self.file+' spec='+str(self.spec) 