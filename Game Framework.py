class Player:
    def __init__(self,current_room):
        self.current_room=current_room
        self.inventory=[]
    
    def move(self,direction):
        if direction in self.current_room.connected_rooms:
            self.current_room=self.current_room.connected_rooms[direction]
            print(f"You moved to {self.current_room.name}")
        else:
            print("You can't go that way.")

    def take(self,item_name):
        for item in self.current_room.items:
            if item.name.lower()==item_name.lower():
                self.inventory.append(item)
                self.current_room.items.remove(item)
                return
        print(f"There is no item name{item} in this room")

    def use(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                print(f"You used the {item.name}")
                self.inventory.remove(item)
                return
        print("You don't have that item.")

class Room:
    def __init__(self,name,description,items=None):
        self.name=name
        self.description=description
        self.connected_rooms={}
        self.items= items if items else []  
    
    def get_details(self):
        print(f"You are in {self.name}")
        print(f"{self.description}")
        if self.items:
            print("Available items")
            for item in self.items:
                print(item)
        print("Available directions:")
        for direction in self.connected_rooms:
            print(f" - {direction} to {self.connected_rooms[direction].name}")

    def connect(self,direction,room):
        self.connected_rooms[direction]=room

class Item:
    def __init__(self,name,description,):
        self.name=name
        self.description=description

    def __str__(self):
        return f"A {self.name}:{self.description}"

    


sword=Item("Sword","A long sord is found",)
map=Item("Map","A Hidden Map in behind a painting")

entrance = Room("Entrance", "A dark and quiet entrance.")
hall = Room("Hall", "A long hallway with old paintings.",[map])
armory = Room("Armory", "Filled with ancient weapons.",[sword])

entrance.connect("north", hall)
hall.connect("south", entrance)
hall.connect("east", armory)
armory.connect("west", hall)

player=Player(entrance)

while True:
    player.current_room.get_details()
    command = input("\nWhat do you want to do? (move [dir], take [item], use [item], or quit)\n").lower()

    if command == "quit":
        print("Exiting game. Goodbye!")
        break
    elif command.startswith("move "):
        direction = command.split("move ")[1]
        player.move(direction)
    elif command.startswith("take "):
        item_name = command.split("take ")[1]
        player.take(item_name)
    elif command.startswith("use "):
        item_name = command.split("use ")[1]
        player.use(item_name)
    else:
        print("Unknown command.")
class Player:
    def __init__(self,current_room):
        self.current_room=current_room
    
    def move(self,direction):
        if direction in self.current_room.connected_rooms:
            self.current_room=self.current_room.connected_rooms[direction]
            print(f"You moved to {self.current_room.name}")
        else:
            print("You can't go that way.")
    
    
class Room:
    def __init__(self,name,description,):
        self.name=name
        self.description=description
        self.connected_rooms={}
    
    def get_details(self):
        print(f"You are in {self.name}")
        print(f"{self.description}")
        print("Available directions:")
        for direction in self.connected_rooms:
            print(f" - {direction} to {self.connected_rooms[direction].name}")


    def connect(self,direction,room):
        self.connected_rooms[direction]=room


entrance = Room("Entrance", "A dark and quiet entrance.")
hall = Room("Hall", "A long hallway with old paintings.")
armory = Room("Armory", "Filled with ancient weapons.")

entrance.connect("north", hall)
hall.connect("south", entrance)
hall.connect("east", armory)
armory.connect("west", hall)

player=Player(entrance)


while True:
    player.current_room.get_details()
    
    choice = input("Where do you want to go?\n")
    
    if choice == "quit":
        print("Exiting game. Goodbye!")
        break

    player.move(choice)
