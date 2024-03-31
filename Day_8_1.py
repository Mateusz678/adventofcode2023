source_file = "Day_8_input_test_set_1.txt"
string_list = ""
coordiantes_dict = {}
curr_coordinates = {}

line_number = 0
with open(source_file, "r") as file:
    for line in file:
        if line_number == 0:
            string_list = line.replace(" ", "").replace("\n", "")
        elif line.find(" ") != -1:
            coordiantes_dict[line[0:3]] = line[line.find("(") + 1:line.find(")")]
            if line[2] == "A":
                curr_coordinates[line[0:3]] = line[0:3]
            
        line_number += 1

iteration_count = 0
z_validation = 0

while z_validation == 0:
    for char in string_list:
        iteration_count += 1
        for coordinate in curr_coordinates:
            mapping = coordiantes_dict[curr_coordinates[coordinate]]
            if char == "L":
                curr_coordinates[coordinate] = mapping[0:mapping.find(",")]
            elif char == "R":
                curr_coordinates[coordinate] = mapping[mapping.find(" ") + 1:]
        
        for element in curr_coordinates:
            if (curr_coordinates[element])[2] == "Z":
                z_validation += 1
        z_validation = z_validation / len(curr_coordinates)

        if z_validation != 1:
            z_validation = 0  
        else:
            break

print(curr_coordinates, iteration_count)