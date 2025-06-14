# OOP-Python-Game-Framework-
A simple terminal-based adventure game built using Python's Object-Oriented Programming concepts. The player navigates through connected rooms using text commands. Each room has its own description and possible directions.

🎯 Project Objective
This project was designed to:
Practice core OOP concepts (classes, encapsulation, abstraction)
Simulate a player navigating through connected rooms
Build a modular and extendable framework for future game logic

📦 Features
Player can move between rooms using direction commands
Rooms are interconnected via a dictionary-based system
Input-driven loop allows for continuous gameplay
Invalid directions are handled gracefully

🧱 OOP Concepts Applied
Classes & Objects: Player and Room are the main classes
Encapsulation: Each class handles its own state and behavior
Composition: A Player holds a Room instance
Abstraction: Simple interface for room connection and movement

#Example Output:
You are in Entrance
A dark and quiet entrance.
Available directions:
 - north to Hall

Where do you want to go?
north

You moved to Hall

Requirements:Python 3.6 or higher

How to Run:
git clone https://github.com/Norpok/OOP-Python-Game-Framework-.git
cd OOP-Python-Game-Framework-
python Game\ Framework.py

📌 Future Improvements
Add items in rooms
Implement puzzles or enemies
Add score tracking or inventory system
Save/load game state
