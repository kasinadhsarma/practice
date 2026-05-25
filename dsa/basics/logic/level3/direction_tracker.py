class DirectionTracker:
    # Simulates movement in a 2D coordinate plane (North, East, South, West)
    # Time Complexity: O(N) where N is the number of commands
    # Space Complexity: O(1) constant auxiliary space
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.directions = ["North", "East", "South", "West"]
        self.dir_idx = 0  # Starts facing North (index 0)

    def turn_right(self):
        self.dir_idx = (self.dir_idx + 1) % 4

    def turn_left(self):
        self.dir_idx = (self.dir_idx - 1) % 4

    def move_forward(self, steps):
        current_dir = self.directions[self.dir_idx]
        if current_dir == "North":
            self.y += steps
        elif current_dir == "East":
            self.x += steps
        elif current_dir == "South":
            self.y -= steps
        elif current_dir == "West":
            self.x -= steps

    def get_position(self):
        return f"Coordinates: ({self.x}, {self.y}), Facing: {self.directions[self.dir_idx]}"


# Example Execution:
tracker = DirectionTracker()
print("Starting Position:", tracker.get_position())

# Move 5 steps North
tracker.move_forward(5)
# Turn Right (Now facing East) and move 3 steps
tracker.turn_right()
tracker.move_forward(3)
# Turn Left (Now facing North) and move 2 steps
tracker.turn_left()
tracker.move_forward(2)

print("Final Position:", tracker.get_position())
