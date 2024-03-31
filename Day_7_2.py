source_file = "Day_7_input_final_set.txt"
input_matrix = []
bet_dict = {}
hand_type_strenght = {}
hand_type_count = {}
string_list = "AKQT98765432J"

with open(source_file, "r") as file:
    for line in file:
        cards = line[0:5]
        line_result_dict = {}
        result_strenght = 0

        bet_dict[cards] = int(line[line.find(" ") + 1:])
        
        for char in cards:
            if char not in line_result_dict.keys():
                line_result_dict[char] = 1
            else:
                line_result_dict[char] += 1
        
        if "J" in line_result_dict.keys():
            j_count_temp = line_result_dict["J"]
            del line_result_dict['J']
            if (len(line_result_dict) == 0):
                line_result_dict["A"] = 0
            max_key = max(line_result_dict, key=line_result_dict.get)
            line_result_dict[max_key] += j_count_temp
        
        if len(line_result_dict) == 1:
            # Five of a kind
            result_strenght = 7
        elif max(line_result_dict.values()) == 4:
            # Four of a kind
            result_strenght = 6
        elif len(line_result_dict) == 2:
            # Full house
            result_strenght = 5
        elif max(line_result_dict.values()) == 3:
            # Three of a kind
            result_strenght = 4
        elif max(line_result_dict.values()) == 2 and len(line_result_dict) == 3:
            # Two pair
            result_strenght = 3
        elif max(line_result_dict.values()) == 2:
            # One pair
            result_strenght = 2
        elif len(line_result_dict) == 5:
            # High card
            result_strenght = 1

        hand_type_strenght[cards] = result_strenght
        hand_type_count[cards] = line_result_dict

        line_corrected = (line.replace("\n", "") + " " + str(result_strenght) + " 0 0").split(" ")
        input_matrix.append(line_corrected)

hand_type_strenght_sorted = dict(sorted(hand_type_strenght.items(), key=lambda item: item[1]))

tuple = list(hand_type_strenght_sorted.items())
print(tuple)
for k in range(0, len(tuple) - 1):
    for i in range(0, len(tuple) - k - 1):
        if tuple[i][1] == tuple[i + 1][1]:
            for j in range(0, 5):
                if string_list.find((tuple[i][0])[j]) < string_list.find((tuple[i + 1][0])[j]):
                    tuple[i], tuple[i + 1] = tuple[i + 1], tuple[i]
                    break
                elif string_list.find((tuple[i][0])[j]) > string_list.find((tuple[i + 1][0])[j]):
                    break

print(tuple)
sorted_dict = dict(tuple)

final_sum = 0
for j in range(0, len(sorted_dict)):
    final_sum += (j + 1) * bet_dict[tuple[j][0]]
print(final_sum)