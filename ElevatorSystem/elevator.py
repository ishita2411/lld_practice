class Elevator:
    def __init__(self, elevator_id, current_floor=0):
        self.elevator_id = elevator_id
        self.current_floor = current_floor
        self.direction = None  # 'up', 'down', or None
        self.is_moving = False
        
    def move_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            self.direction = 'up'
        elif target_floor < self.current_floor:
            self.direction = 'down'
        else:
            self.direction = None
        
        self.is_moving = True
        # Simulate movement (in a real system, this would involve time and sensors)
        self.current_floor = target_floor
        self.is_moving = False