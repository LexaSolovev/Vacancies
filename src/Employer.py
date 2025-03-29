class Employer:

    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url

    def __str__(self):
        return self.name
