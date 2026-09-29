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


# User input for side length and layers of pyramid
side_length = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))

# Variable to calculate face area
face_area = side_length ** 2

# Top visible area is equal to the base area of n x n faces
top_area = (layers ** 2) * face_area

# Side area calculated by looping through each layer from 1 to n
side_faces = 0
for i in range(1, layers + 1):
    side_faces += i

    side_area = 4 * side_faces * face_area

total_area = top_area + side_area

print(f"You need {total_area:.2f} m^2 of gold foil to cover the pyramid")
