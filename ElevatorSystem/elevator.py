class Elevator:
    def __init__(self, elevator_id, current_floor=0):
        self.elevator_id = elevator_id
        self.current_floor = current_floor
        self.direction = None  # 'up', 'down', or None
        self.is_moving = False
        
    