
def sum_ascii(list):
    score_dict = {}
    for name in list:
      sum = 0
      for char in name:
        sum += ord(char.lower())
        score_dict[name] = sum
    highest_name = max(score_dict, key = score_dict.get)
    return {highest_name: score_dict[highest_name]}


