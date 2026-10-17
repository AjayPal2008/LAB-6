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
time = input("Enter the time: ").strip()
clock = input("Choose the clock type (12 or 24): ").strip()
# Allowed characters for preferred character validation
allowed = "abcdeghkmnopqrsuvwxyz@$&*="
char = input("Enter your preferred character: ")
while char != "" and (len(char) != 1 or char not in allowed):
    char = input("Character not permitted! Try again: ")
# Parse hours and minutes
hours = time[:time.find(":")]
minutes = time[time.find(":") + 1:]
AMorPM = ""


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
    if char and num.isdigit():
        return [row.replace(num, char) for row in doc_string[num]]
    return doc_string[num]

# Handle 12-hour clock conversion and AM/PM suffix
if clock == "12":
    AMorPM = "AM" if int(hours) < 12 else "PM"
    hours = str(int(hours) % 12 or 12)
else:
    hours = str(int(hours))

Connector = hours + ":" + minutes + AMorPM
for row in range(5):
    print(" ".join(clock_ASCII(char, digit)[row] for digit in Connector))
