def get_num_words(string):
    return len(string.split())

def get_char_count(string):
    lowered_case = string.lower()
    char_dict = {}
    for char in lowered_case:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(arr):
    return arr["num"]

def get_sorted_char_count_list(char_count_dict):
    unsorted_arr = []
    for key,value in char_count_dict.items():
        unsorted_arr.append({ "char": key, "num": value })
    unsorted_arr.sort(reverse=True, key=sort_on)
    return unsorted_arr
    