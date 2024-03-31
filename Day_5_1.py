source_file = "Day_5_input_final_set.txt"
source_list = []
dict_map = {}
map_coordinates_temp = []
result_list = []

line_number = 0
with open(source_file, "r") as file:
    for line in file:
        if line_number == 0:
            seeds_list = line[line.find(" ") + 1:].replace("\n", "").split(" ")
        elif line == '':
            line_corrected = line
        elif line.find(" map:") != -1:
            list_name_temp = line
            line_corrected = line
            map_coordinates_temp = []
            dict_map[line_corrected.replace("\n", "")] = map_coordinates_temp
        elif line[0].isdigit() == 1:
            map_coordinates_temp.append(line.replace("\n", "").split(" "))
        line_number += 1
        
for seed in seeds_list:
    seed_n = int(seed)
    for map in dict_map:
        current_matrix = dict_map[map]
        for line in range(0, len(dict_map[map])):
            seed_corrected_n = seed_n
            if seed_corrected_n >= int(current_matrix[line][1]) and seed_corrected_n <= int(current_matrix[line][1]) + int(current_matrix[line][2]):
                seed_corrected_n = int(current_matrix[line][0]) + (seed_n - int(current_matrix[line][1]))
                seed_n = seed_corrected_n
                break
        print(map, seed_n)
    print("")
    result_list.append(seed_n)

print(min(result_list))
                