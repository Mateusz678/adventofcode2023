source_file = "Day_3_input_final_set.txt"
source_dictionary = []
with open(source_file, "r") as file:
    for line in file:
        source_dictionary.append(line.replace("\n", ""))
        
exclusions_list = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
prev_line = ""
final_sum = 0
for k in range(0, len(source_dictionary)):
    
    if k > 0:
        prev_line = source_dictionary[k - 1]
    curr_line = source_dictionary[k]
    if k == len(source_dictionary) - 1:
        next_line = ""
    else:
        next_line = source_dictionary[k + 1]
    print(curr_line)

    i = 0
    while i in range(0, len(curr_line)):
        char = curr_line[i]
        if char.isdigit() == 1:
            number_temp = ""
            should_count = 0
            for j in range(i, len(curr_line)):
                if curr_line[j].isdigit() == 1:
                    number_temp = number_temp + curr_line[j]
                    start_digit = 0 if j == 0 else j - 1
                    end_digit = len(curr_line) - 1 if j == len(curr_line) - 1 else j + 2
                    
                    for l in range (start_digit, end_digit):
                        if prev_line != "" and prev_line[l] not in exclusions_list:
                            should_count = 1
                        if curr_line[l] not in exclusions_list:
                            should_count = 1
                        if next_line != "" and next_line[l] not in exclusions_list:
                            should_count = 1
                else:
                    i = j
                    break
            final_sum = final_sum + should_count * int(number_temp)
            print(final_sum)
        i += 1