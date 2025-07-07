[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg


# Dijkstra Pathfinding Visualization

A Python implementation of Dijkstra's shortest path algorithm with procedural maze generation and interactive visualization.

## Features

- **Procedural Maze Generation**: Creates random mazes using a depth-first search algorithm
- **Dijkstra's Algorithm**: Finds the shortest path from home to target room
- **Interactive Visualization**: Step through different maze generations with visual path highlighting
- **Customizable Parameters**: Adjustable maze size and connection density

## Project Structure

```
dijkstraFunction1/
├── main.py          # Main application and Dijkstra implementation
├── MapClass.py      # Maze generation and visualization class
└── README.md        # This file
```

## How It Works

### Maze Generation (`MapClass.py`)
- Generates a maze using a modified depth-first search algorithm
- Creates passages (hallways) connecting rooms
- Places a home point (H) at the center
- Randomly selects a dead-end as the target room (R)
- Optionally adds extra connections to create loops

### Pathfinding (`main.py`)
- Implements Dijkstra's algorithm to find the shortest path
- Searches from Home (H) to Room (R)
- Marks the shortest path with asterisks (*) on the map
- Handles cases where no path exists

## Map Legend

| Symbol | Meaning |
|--------|---------|
| `H`    | Home (starting point) |
| `R`    | Room (target destination) |
| `.`    | Hallway (walkable path) |
| `*`    | Shortest path |
| ` `    | Wall (unwalkable) |

## Usage

### Prerequisites
- Python 3.7+
- No external dependencies required (uses only standard library)

### Running the Application

```bash
python main.py
```

### Controls
- **Press Enter**: Generate a new maze and find the shortest path
- **Ctrl+C**: Exit the application

## Configuration

You can modify the maze parameters in `main.py`:

```python
map = Map(size=51, extra_connection_chance=0.01)
```

### Parameters
- `size`: Maze dimensions (must be odd number ≥ 5)
- `extra_connection_chance`: Probability of creating additional connections (0.0 - 1.0)

## Algorithm Details

### Dijkstra's Implementation
- **Time Complexity**: O((V + E) log V) where V is vertices and E is edges
- **Space Complexity**: O(V) for distance and previous node tracking
- **Uses**: Min-heap priority queue for efficient node selection
- **Movement**: 4-directional (up, down, left, right)

### Maze Generation
- **Algorithm**: Depth-first search with backtracking
- **Ensures**: All accessible areas are connected
- **Features**: Guaranteed solvable mazes with single solution paths

## Example Output

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                      │
│                                                                                                      │
│                                                                                                      │
│                                                                                                      │
│                                          . . . . . . . .                                           │
│                                          .             .                                           │
│                                          . . . . * * * .                                           │
│                                                    *   .                                           │
│                                          . . . . . * . .                                           │
│                                          .         *                                               │
│                                          . . . H * * . .                                           │
│                                          .     *       .                                           │
│                                          . . . * . . . .                                           │
│                                                *                                                   │
│                                          . . . * . . . .                                           │
│                                          .     *       .                                           │
│                                          . . . * * * R .                                           │
│                                                      .                                             │
│                                          . . . . . . . .                                           │
│                                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────────────────────┘
 H = Home
 . = Hallway
 R = Room
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](LICENSE.md).

## Acknowledgments

- Map generation code adapted from previous project
- Dijkstra's algorithm implementation follows standard computer science practices

