def sentence_to_camel_case(arg1, arg2):
   result = ""
   if arg2 == True:
    split_string = arg1.split()
    for word in split_string:
        result += word.capitalize()   
    return result
   else:
     split_string = arg1.split()
     result += split_string[0].lower()
     for word in split_string[1:]:
        result += word.capitalize()
     return result


