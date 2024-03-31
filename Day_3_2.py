source_file = "Day_3_input_final_set.txt"
source_list = []
with open(source_file, "r") as file:
    for line in file:
        source_list.append(line.replace("\n", ""))
        
prev_line = ""
next_line = ""
final_sum = 0
for k in range(0, len(source_list)):
    
    if k > 0:
        prev_line = source_list[k - 1]
    curr_line = source_list[k]
    if k == len(source_list) - 1:
        next_line = ""
    else:
        next_line = source_list[k + 1]
    
    for i in range(0, len(curr_line)):
        char = curr_line[i]
        if char == "*":
            number_temp = ""
            should_count = 0
            star_coordinates = []
            start_digit = 0 if i == 0 else i - 1
            end_digit = len(curr_line) - 1 if i == len(curr_line) - 1 else i + 2
            checked_coordinates = [[k, i]]
            solution_count = 0
            star_factor = 1
            
            for l in range (start_digit, end_digit):
                number_temp = ""
                if prev_line != "" and prev_line[l].isdigit() == 1 and [k-1, l] not in checked_coordinates:
                    should_count += 1
                    number_temp = prev_line[l]
                    checked_coordinates.append([k-1, l])
                    for j in range(l + 1, len(line) + 1):
                        if prev_line[j].isdigit() == 1 and [k-1, j] not in checked_coordinates:
                            number_temp = number_temp + prev_line[j]
                            checked_coordinates.append([k-1, j])
                        else:
                            break
                    for j in range(l - 1, -1, -1):
                        if prev_line[j].isdigit() == 1 and [k-1, j] not in checked_coordinates:
                            number_temp = prev_line[j] + number_temp
                            checked_coordinates.append([k-1, j])
                        else:
                            break
                    solution_count += 1
                    star_factor = star_factor * int(number_temp)
                
                number_temp = ""
                if curr_line[l].isdigit() == 1 and [k, l] not in checked_coordinates:
                    should_count += 1
                    number_temp = curr_line[l]
                    for j in range(l + 1, len(line) + 1):
                        if curr_line[j].isdigit() == 1 and [k, j] not in checked_coordinates:
                            number_temp = number_temp + curr_line[j]
                            checked_coordinates.append([k, j])
                        else:
                            break
                    for j in range(l - 1, -1, -1):
                        if curr_line[j].isdigit() == 1 and [k, j] not in checked_coordinates:
                            number_temp = curr_line[j] + number_temp
                            checked_coordinates.append([k, j])
                        else:
                            break
                    solution_count += 1
                    star_factor = star_factor * int(number_temp)
                    
                number_temp = ""
                if next_line != "" and next_line[l].isdigit() == 1 and [k+1, l] not in checked_coordinates:
                    should_count += 1
                    number_temp = next_line[l]
                    checked_coordinates.append([k+1, l])
                    for j in range(l + 1, len(line) + 1):
                        if next_line[j].isdigit() == 1 and [k+1, j] not in checked_coordinates:
                            number_temp = number_temp + next_line[j]
                            checked_coordinates.append([k+1, j])
                        else:
                            break
                    for j in range(l - 1, -1, -1):
                        if next_line[j].isdigit() == 1 and [k+1, j] not in checked_coordinates:
                            number_temp = next_line[j] + number_temp
                            checked_coordinates.append([k+1, j])
                        else:
                            break
                    solution_count += 1
                    star_factor = star_factor * int(number_temp)
            
            if (solution_count != 2):
                star_factor = 0
            final_sum = final_sum + star_factor
print(final_sum)