def simulate_snake_game(map_matrix, actions):
    # Define the directions for movements: up, down, left, right
    directions = {
        0: (-1, 0),  # Up
        1: (1, 0),   # Down
        2: (0, -1),  # Left
        3: (0, 1)    # Right
    }
    
    # Find the initial position of the snake's head (@)
    head_position = None
    body_positions = set()  # To keep track of the snake's body positions
    
    for i in range(len(map_matrix)):
        for j in range(len(map_matrix[i])):
            if map_matrix[i][j] == '@':
                head_position = (i, j)
            elif map_matrix[i][j] == '#':
                body_positions.add((i, j))
    
    # Initialize the running time
    running_time = 0
    
    # Process each action
    for action in actions:
        if head_position is None:
            break  # No head found, exit
        
        # Get the direction to move
        move = directions[action]
        new_head_position = (head_position[0] + move[0], head_position[1] + move[1])
        
        # Check for boundary conditions
        if (new_head_position[0] < 0 or new_head_position[0] >= len(map_matrix) or
            new_head_position[1] < 0 or new_head_position[1] >= len(map_matrix[0])):
            break  # Out of bounds
        
        # Check for collision with rocks
        if map_matrix[new_head_position[0]][new_head_position[1]] == 'x':
            break  # Collision with rock
        
        # Check for collision with the snake's body
        if new_head_position in body_positions:
            break  # Collision with body
        
        # Update the head position and body positions
        body_positions.add(head_position)  # Move the current head to the body
        head_position = new_head_position  # Update the head position
        
        # Update running time
        running_time += 1
    
    # Output the result
    if running_time < len(actions):
        print(running_time)
    else:
        print(f"{head_position[0]} {head_position[1]}")

# Example input
map_input = [
    "---------",
    "------x--",
    "-x-------",
    "---@-----",
    "---##----",
    "------x--",
    "--x----x-",
    "-x-------",
    "---------"
]

action_input = [0, 0, 3, 3, 0, 3, 3, 1, 1, 1, 1, 1, 3, 1, 1, 2, 2, 2, 2, 2]

# Running the simulation
simulate_snake_game(map_input, action_input)