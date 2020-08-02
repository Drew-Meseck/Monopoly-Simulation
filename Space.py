class Space:
    name = 'N/A'
    group = 'N/A'
    prop = False
    count = 0

    def __init__(self, n, g, p):
        self.name = n
        self.group = g
        self.prop = p

    def increment(self):
        self.count += 1
    
    def ToString(self):
        print(self.name + " " + self.group + " " + "COUNT: " + str(self.count))