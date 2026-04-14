from building import Building
from elevator import Elevator
def main():
    building = Building(10)
    elevator1 = Elevator(elevator_id=1)
    elevator2 = Elevator(elevator_id=2)
    building.elevators.append(elevator1)
    building.elevators.append(elevator2)

if __name__ == "__main__":
    main()