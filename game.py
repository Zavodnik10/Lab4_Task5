class Room:
    def __init__(self, name) -> None:
        self.name = name
    def set_description(self, descr):        
        self.descr = descr
    def link_room(self, next,  napr):
        self.next = next
        self.napr = napr        
        self.rooms = []
        self.rooms.append((self.next, self.napr))
        # return f'The {next.name} is {napr}'
    def set_item(self, item):
        self.item = item
    def set_character(self, character):
        self.character = character
    def get_character(self):
        try:
            return self.character
        except AttributeError: return None
    def get_item(self):        
        try:
            return self.item
        except AttributeError: return None
    def get_details(self):
            print(f'{self.name}\n''---------------------\n'f'{self.descr}\n')
            for i in self.rooms:
                print(f'The {i[0].name} is {i[1]}')
    def move(self, command):
        for i in self.rooms:
            if command in i:
                return i[0]
class Character:
    killed = 0
    def __init__(self, name , description):     
        self.name = name
        self.description = description      
    def set_conversation(self, conv):
        self.conv = conv
    def describe(self):       
        print(f'The {self.name} is here\n'f'{self.description}' )  
    def talk(self):
        print(self.conv) 
    def get_defeated(self):      
        return self.killed
class Enemy(Character):
    def __init__(self, name, description): 
        self.name = name
        self.description = description  
    
    def set_conversation(self, text):
        self.text = text
    def set_weakness(self, atribute):
        self.atribute = atribute
    def fight(self, item):      
        if item == self.atribute:
            Character.killed += 1
            return True
        else: 
            return False
class Item:
    def __init__(self, name) -> None:
        self.name = name
    def set_description(self, discr):
        self.discr = discr
    def describe(self):
        print(f'The {self.name} is here - {self.discr}')
    def get_name(self):
        return self.name