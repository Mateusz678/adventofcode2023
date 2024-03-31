final_sum = 0

with open("Day_4_input_final_set.txt", "r") as file:
    for line in file:
        line_corrected = line[line.find(":") + 2:]
        line_winners = line_corrected[0:line_corrected.find("|") - 1].replace("\n", "").replace("  ", " ").split(" ")
        line_results = line_corrected[line_corrected.find("|") + 2:].replace("\n", "").replace("  ", " ").split(" ")
        for element in line_winners:
            if element.isdigit() == 0:
                line_winners.remove(element)
        for element in line_results:
            if element.isdigit() == 0:
                line_results.remove(element)
        
        count = 0
        for element in line_winners:
            if element in line_results:
                count += 1

        if count == 0:
            result = 0
        else:
            result = 2** (count - 1)

        final_sum += result
print(final_sum)