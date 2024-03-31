final_result = 0
string_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
string_list_r = []
for s in string_list:
    string_list_r.append(s[::-1])
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dictionary = dict(zip(string_list, number_list))
dictionary_r = dict(zip(string_list_r, number_list))

with open("Day_1_input.txt", "r") as file, open("Day_1_output.txt", "w") as output_file:
    for line in file:
        
        line_corrected = line
        for i in range(2, len(line_corrected)):
            line_corrected_temp = line_corrected[0:i]
            for key, value in dictionary.items():
                if key in line_corrected_temp:
                    line_corrected = line_corrected_temp.replace(key, str(value))
            
        first_digit = 0
        for i in line_corrected:
            if i.isdigit() == 1:
                if first_digit == 0:
                    first_digit = int(i)

        line_r = line[::-1]
        line_r_corrected = line_r
        for i in range(2, len(line_r_corrected)):
            line_r_corrected_temp = line_r_corrected[0:i]
            for key, value in dictionary_r.items():
                if key in line_r_corrected_temp:
                    line_r_corrected = line_r_corrected_temp.replace(key, str(value))
        
        last_digit = 0
        for i in line_r_corrected:
            if i.isdigit() == 1:
                if last_digit == 0:
                    last_digit = int(i)

        current_line_result = first_digit * 10 + last_digit
        final_result = final_result + current_line_result
        
print(str(final_result))