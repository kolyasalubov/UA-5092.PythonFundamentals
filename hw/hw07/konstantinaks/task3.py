def calc_num(text):
    result_dict = {}
    for i in text:
        if i in result_dict:
            result_dict[i] += 1
        else:
            result_dict[i] = 1
    return result_dict

res = calc_num("hello")
print(res) # {'h': 1, 'e': 1, 'l': 2, 'o': 1}