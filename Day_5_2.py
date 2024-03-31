source_file = "Day_5_input_final_set.txt"
source_list = []
dict_map = {}
map_coordinates_temp = []
result_list = []
ranges = []
seeds_list = []

line_number = 0
with open(source_file, "r") as file:
    for line in file:
        if line_number == 0:
            ranges = line[line.find(" ") + 1:].replace("\n", "").split(" ")
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
        
print(dict_map)

for i in range(0, len(ranges), 2):
    start_number = int(ranges[i])
    count_number = int(ranges[i+1])
    print(start_number, count_number)
    
    for j in range(start_number, start_number + count_number + 1):
        if str(j) not in seeds_list and j not in seeds_list:
            seed_n = int(j)
            for map in dict_map:
                current_matrix = dict_map[map]
                for line in range(0, len(dict_map[map])):
                    seed_corrected_n = seed_n
                    if seed_corrected_n >= int(current_matrix[line][1]) and seed_corrected_n <= int(current_matrix[line][1]) + int(current_matrix[line][2]):
                        seed_corrected_n = int(current_matrix[line][0]) + (seed_n - int(current_matrix[line][1]))
                        seed_n = seed_corrected_n
                        break
            result_list.append(seed_n)
            seeds_list.append(str(j))

print(min(result_list))