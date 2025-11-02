import time
import os

#Configuration of constants
FLOOR_TRAVEL_TIME = 10  #seconds per floor (for calculation)
ANIMATION_DELAY = 1.0   #seconds per floor (for display animation)

#Main program
def main():
    print("\n*** 🏢 Elevator Simulator ***\n")

    #Get valid starting floor
    start = get_positive_integer_input("Enter starting floor: ")

    #Get valid destination floors
    floor_list = get_positive_floor_list_input("Enter floors to visit (comma separated): ")

    #Get animation choice
    animate_choice = input("Animate movement? (y/n): ").strip().lower()
    animate = animate_choice == 'y'
    clear_screen()

    #Run simulation
    elevator_ride(start, floor_list, animate)

#Elevator logic
def elevator_ride(start_floor, floor_list, animate=False):
    #Simulate elevator movement and calculate total travel time.
    visited_floors = [start_floor] + floor_list
    total_time = 0

    print(f"\nLet's go on an Elevator Ride!...")
    print(f"Floors to visit: {', '.join(map(str, visited_floors))}\n")

    current = start_floor

    for next_floor in floor_list:
        diff = abs(next_floor - current)
        total_time += diff * FLOOR_TRAVEL_TIME

        if animate:
            animate_elevator(current, next_floor)

        current = next_floor

    print(f"\n🏢 You have reached the end of your Elevator Ride.")
    print(f"Floors visited in order: {', '.join(map(str, visited_floors))}")
    print(f"Total travel time: {total_time} seconds\n")

def animate_elevator(from_floor, to_floor):
    #Text-based animation of the elevator moving between floors.
    direction = 1 if to_floor > from_floor else -1
    print(f"Moving from floor {from_floor} to {to_floor}...")
    time.sleep(ANIMATION_DELAY)

    for floor in range(from_floor, to_floor + direction, direction):
        print(f"🚪 Elevator currently at floor {floor}")
        time.sleep(ANIMATION_DELAY)

    print(f"✅ Arrived at floor {to_floor}")
    time.sleep(ANIMATION_DELAY)

#Helper functions
def clear_screen():
    #Clears the console for a cleaner animation experience.
    os.system('cls')

def is_positive_integer(value):
    #Checks if a string represents a valid positive integer.
    return value.isdigit() and int(value) > 0

def get_positive_integer_input(prompt):
    #Prompt user for a single valid floor number.
    while True:
        user_input = input(prompt).strip()
        if is_positive_integer(user_input):
            return int(user_input)
        else:
            print(f"\n❌ Invalid input. Please enter a whole number greater than zero.")

def get_positive_floor_list_input(prompt):
    #Prompt user for a comma-separated list of valid positive integers.
    while True:
        floors_input = input(prompt).strip()
        if not floors_input:
            print(f"\n❌ You must enter at least one floor.")
            continue

        floor_list = []
        invalid_entries = []

        for part in floors_input.split(','):
            part = part.strip()
            if is_positive_integer(part):
                floor_list.append(int(part))
            else:
                invalid_entries.append(part or "blank")

        if invalid_entries:
            print(f"\n⚠️ Invalid floor(s): {', '.join(invalid_entries)} — only whole numbers greater than zero are allowed.")
            continue

        if floor_list:
            return floor_list
        else:
            print(f"\n❌ No valid floor numbers found. Please try again.")

if __name__ == "__main__": main()