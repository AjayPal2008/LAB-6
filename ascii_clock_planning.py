# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ajay Palanisamy
#       Benjamin Hatch
#       Micah Kadiri
#       Hudson Dobbs
# Section: ENGR 102 508
# Assignment: LAB 8
# Date: 10/16/2026


# Top-down design:
# 1. Read inputs and retry invalid preferred characters.
# 2. Convert the hour and determine AM or PM.
# 3. Look up five rows per symbol in a dictionary.
# 4. Join matching rows with one space and print the clock.

# 1. Take inputs
# Read the time string from the user
time = input("Enter the time: ").strip()
# Read the preferred clock type format
clock = input("Choose the clock type (12 or 24): ").strip()
# Allowed characters for preferred character validation
allowed = "abcdeghkmnopqrsuvwxyz@$&*="
# Prompt user for a custom character to replace default ones
char = input("Enter your preferred character: ")
# Loop to ensure input character is either empty or valid
while char != "" and (len(char) != 1 or char not in allowed):
    char = input("Character not permitted! Try again: ")
# Parse hours and minutes
# Find the index of the colon separator
hours = time[:time.find(":")]
# Extract the minutes substring following the colon
minutes = time[time.find(":") + 1:]
# Initialize the AM or PM suffix string variable
AMorPM = ""


# Define function to generate ASCII art rows for a character
def clock_ASCII(char, num):
# Define 3x5 ASCII art dictionary for digits, colon, and letters
    doc_string = {
        "0": ["000", "0 0", "0 0", "0 0", "000"],
        "1": [" 1 ", "11 ", " 1 ", " 1 ", "111"],
        "2": ["222", "  2", "222", "2  ", "222"],
        "3": ["333", "  3", "333", "  3", "333"],
        "4": ["4 4", "4 4", "444", "  4", "  4"],
        "5": ["555", "5  ", "555", "  5", "555"],
        "6": ["666", "6  ", "666", "6 6", "666"],
        "7": ["777", "  7", "  7", "  7", "  7"],
        "8": ["888", "8 8", "888", "8 8", "888"],
        "9": ["999", "9 9", "999", "  9", "999"],
        ":": [" ", ":", " ", ":", " "],
        "A": [" A ", "A A", "AAA", "A A", "A A"],
        "P": ["PPP", "P P", "PPP", "P  ", "P  "],
        "M": ["M   M", "MM MM", "M M M", "M   M", "M   M"],
    }
    # Check if both a custom character and a numeric digit are provided
    if char and num.isdigit():
        # Replace default digit representation with the custom user character
        return [row.replace(num, char) for row in doc_string[num]]
    # Fallback to return standard dictionary representation if no replacement
    return doc_string[num]

# Handle 12-hour clock conversion and AM/PM suffix
# Check if the user selected a 12-hour clock format
if clock == "12":
    AMorPM = "AM" if int(hours) < 12 else "PM"
    # Adjust hour value and set suffix for 12-hour format
    hours = str(int(hours) % 12 or 12)
else:
    hours = str(int(hours))

# Combine hours, colon separator, minutes, and AM/PM into one string
Connector = hours + ":" + minutes + AMorPM
# Loop through each of the 5 vertical rows of the ASCII display
for row in range(5):
    print(" ".join(clock_ASCII(char, digit)[row] for digit in Connector))
