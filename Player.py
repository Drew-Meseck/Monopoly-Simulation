class Player:
    id = 0
    pos = 0

    def __init__(self, i):
        self.id = i
    
    def move(self, roll):
        self.pos = self.pos + roll
        if self.pos >= 40:
            self.pos = self.pos - 40

    def reset(self):
        self.pos = 0
    
    def ToString(self):
        print('Name: ' + str(self.id) + ' ' + 'Position: ' + str(self.pos))