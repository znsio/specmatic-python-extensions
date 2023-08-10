class CoverageRoute:
    def __init__(self, url, methods):
        self.url = url
        self.methods = methods

    def __eq__(self, other):
        if isinstance(other, CoverageRoute):
            return self.url == other.url and self.methods == other.methods
        return False
