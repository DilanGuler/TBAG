class Room:
    def __init__(self,room_name) :
        self.name= room_name
        self.discruption= None

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
    
    def describe(self):
        print(self.description)