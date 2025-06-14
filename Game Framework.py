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
