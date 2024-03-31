limit_dict = {"red" : 12,
            "green" : 13,
            "blue": 14}
line_number = 0
final_sum = 0

with open("Day_2_input.txt", "r") as file:
    for line in file:
        line_corrected = line[line.find(":") + 1:]
        line_results = line_corrected.split(";")
        line_number += 1
        line_status = 1
        max_dict = {}
        line_factor = 1

        for i in line_results:
            iteration_result = i.split(",")
            for j in iteration_result:
                j_corrected = j[1:]
                j_number = int(j_corrected[0:j_corrected.find(" ")])
                j_color = j_corrected[j_corrected.find(" ") + 1:].replace("\n", "")
                if j_color in max_dict:
                    if max_dict[j_color] < j_number:
                        max_dict[j_color] = j_number
                else:
                    max_dict[j_color] = j_number
                
        for k in max_dict:
            line_factor = line_factor * max_dict[k]
        
        final_sum += line_factor

print(final_sum)