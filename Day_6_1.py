source_file = "Day_6_input_final_set.txt"
input_matrix = []

line_number = 0
with open(source_file, "r") as file:
    for line in file:
        i = 0
        line_corrected = line
        while i == 0:
            if line_corrected.find("  ") != -1:
                line_corrected = line_corrected.replace("  ", " ")
            else:
                i = 1
        
        line_corrected = line_corrected[line_corrected.find(": ") + 2:].replace("\n", "").split(" ")
        input_matrix.append(line_corrected)
print(input_matrix)

final_factor = 1
for i in range(0, len(input_matrix[0])):
    print("")
    print(input_matrix[0][i])
    count_results = 0
    for j in range(1, int(input_matrix[0][i]) + 1):
        dist = j * int(input_matrix[0][i]) - j * j
        if dist > int(input_matrix[1][i]):
            count_results += 1
    print(count_results)
    final_factor *= count_results
print(final_factor)