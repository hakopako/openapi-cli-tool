class RouteCollection:

    def __init__(self):
        self.collection = []


    def to_list(self):
        result = []
        for route in self.collection:
            result.append([route.method, route.url, route.file])
        return result


    def add(self, route):
        self.collection.append(route)


    def get(self):
        return self.collection


    def sort(self):
        try:
            self.collection.sort(lambda x,y: cmp(x.url, y.url), lambda x,y: cmp(x.method, y.method))
        except:
            self.collection.sort(key=lambda x: (x.url, x.method))


    def len(self):
        return len(self.collection)
