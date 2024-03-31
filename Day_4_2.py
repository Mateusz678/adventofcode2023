game_number = 0
card_dict = {}
with open("Day_4_input_final_set.txt", "r") as file, open("Day_4_output.txt", "w") as output_file:
    for line in file:
        game_number += 1
        line_corrected = line[line.find(":") + 2:]
        line_winners = line_corrected[0:line_corrected.find("|") - 1].replace("\n", "").replace("  ", " ").split(" ")
        line_results = line_corrected[line_corrected.find("|") + 2:].replace("\n", "").replace("  ", " ").split(" ")
        for element in line_winners:
            if element.isdigit() == 0:
                line_winners.remove(element)
        for element in line_results:
            if element.isdigit() == 0:
                line_results.remove(element)
        
        if str(game_number) not in card_dict.keys():
            card_dict[str(game_number)] = 1
        else:
            card_dict[str(game_number)] += 1

        count = 0
        for element in line_winners:
            if element in line_results:
                count += 1
        
        for i in range(1, count + 1):
            if str(game_number + i) not in card_dict.keys():
                card_dict[str(game_number + i)] = card_dict[str(game_number)]
            else:
                card_dict[str(game_number + i)] += 1 * card_dict[str(game_number)]

final_sum = sum(card_dict.values())
print(final_sum)
