# Langton's Ant Simulation

This Python script implements Langton's Ant, a cellular automaton and an example of emergent behavior. The simulation is displayed using the Pygame library, creating a graphical representation of the ant's movement and its interaction with the grid.

Prerequisites
Ensure you have the following installed before running the script:
- Python (>= 3.x)
- Pygame library

Installation
1. Make sure you have Python installed. You can download it from the official Python website (https://www.python.org/downloads/).
2. Install Pygame library using pip: pip install pygame

Usage
1. Run the Python script in your terminal or IDE.
2. The simulation window will open, displaying the Langton's Ant behavior.
3. The ant moves on a 2D grid, and each cell can be in either an "on" (white) or "off" (black) state.
4. Initially, the ant is placed in the center of the grid, facing upwards (North).
5. The ant follows the following rules at each step:
- If the cell the ant is on is white, it turns 90 degrees left, flips the cell to black, and moves forward one step.
- If the cell the ant is on is black, it turns 90 degrees right, flips the cell to white, and moves forward one step.

Contributing
If you want to contribute to this project, feel free to fork the repository, make improvements, and create a pull request.

License
This project is licensed under the MIT License. Feel free to use and distribute it according to the terms of the license.

Note
Make sure you have the required dependencies installed before running the script. Enjoy observing the fascinating behavior of Langton's Ant!
