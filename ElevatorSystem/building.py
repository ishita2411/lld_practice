class Building:
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.elevators = []

    def call_elevator(self, floor):
        # Simple logic to call the nearest elevator
        if not self.elevators:
            print("No elevators available.")
            return None
        
        nearest_elevator = min(self.elevators, key=lambda e: abs(e.current_floor - floor))
        print(f"Calling elevator {nearest_elevator.elevator_id} to floor {floor}.")
        nearest_elevator.move_to_floor(floor)
        return nearest_elevator