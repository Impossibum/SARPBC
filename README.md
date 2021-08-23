# Python Hivemind Quickstart Template

This template is meant as a solid foundation for the creation of a Python hivemind rlbot bot.

## Framework Concept
This framework isn't intended to be your one stop shop for an SSL bot. There's basic utilities included to get you up and running but it's suggested you incorporate a community utility package (RLU, gosling utils, virx-rlu) to quickly and easily inject more functionality.

### Maneuvers
Manuevers are meant to be the simple building blocks of a routine. Drive to specific coordinates, carry out a flip, orient your car a specific way, etc. 

### Routines
Routines are more complex tasks that generally involve chaining several different manuevers and even other routines together. Example scenarios might include taking a shot and then demoing the defender, stealing corner boost and then retreating, etc.

### Strategies
Strategies are the high level coordinaters of the game. They take in the gamestate and decide what routines would be best for the current situation. Is it kickoff? Better exit the current routine and start up the kickoff routine. Etc. 
