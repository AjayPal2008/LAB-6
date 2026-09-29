# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Micah Kadiri
#               Benjamin Hatch
#               Ajay Palanisamy
#               Hudson Dobbs
# Section:      508
# Assignment:   Lab Topic 6 (Team)
# Date:         27 September 2026
 
import math
# Enter side length and the number of layers
side_length = float(input("Enter the side length in meters: "))
layers =  int(input("Enter the number of layers: "))

# Enter an equation that gives the surface area
side_area = side_length**2
total_area = 4*side_area*(layers*(layers+1)/2) + side_area*(layers**2)

# #Print final statement
if side_length <= 0 or layers <= 0:
     print("A number entered is invalid!")
else: 
    print(f"You need {total_area:.2f} m^2 of gold foil to cover the pyramid")
