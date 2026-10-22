"""
Name: Roseann Lawson
Course: CIS105 - Introduction to Python Programming
Assignment: Exercise Assignment 4
Description: Space Mission Calculator
"""

# Converts miles to kilometers
def miles_to_kilometers(miles):
    return miles * 1.60934


# Calculates travel time
def calculate_travel_time(distance, speed):
    return distance / speed


# Calculates fuel needed
def calculate_fuel_needed(distance, fuel_rate):
    return distance * fuel_rate


# Checks if enough fuel is available
def check_fuel_supply(required_fuel, available_fuel):
    return available_fuel >= required_fuel


if __name__ == "__main__":

    print("=== Space Mission Calculator ===")

    distance_miles = float(input("Enter mission distance (miles): "))
    spacecraft_speed = float(input("Enter spacecraft speed (mph): "))
    fuel_rate = float(input("Enter fuel usage per mile: "))
    available_fuel = float(input("Enter available fuel: "))

    distance_km = miles_to_kilometers(distance_miles)
    travel_time = calculate_travel_time(distance_miles, spacecraft_speed)
    required_fuel = calculate_fuel_needed(distance_miles, fuel_rate)

    print("\nMission Results")
    print("--------------------------")
    print(f"Distance: {distance_km:.2f} kilometers")
    print(f"Travel Time: {travel_time:.2f} hours")
    print(f"Fuel Required: {required_fuel:.2f}")

    if check_fuel_supply(required_fuel, available_fuel):
        print("Status: Enough fuel available.")
    else:
        print("Status: Not enough fuel available.")
