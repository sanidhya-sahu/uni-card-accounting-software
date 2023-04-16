string_list = [] # empty list to store the strings
a = input()
b = a.capitalize()
print(b)
search_words = b.split()
i=0
with open("materialcode.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    for word in search_words:
        if word in line:
            print(line)
            string_name = f"string_{i + 1}"  # create a variable name with a unique number
            string_value = f"{line}"  # create the string value
            locals()[string_name] = string_value  # dynamically create the variable and assign the string value
            string_list.append(locals()[string_name])  # add the variable to the list
            i+=1
            break
# n = 5 # number of strings to create
#
# for i in range(n):
#     string_name = f"string_{i+1}" # create a variable name with a unique number
#     string_value = f"This is string {i+1}" # create the string value
#     locals()[string_name] = string_value # dynamically create the variable and assign the string value
#     string_list.append(locals()[string_name]) # add the variable to the list
# # print the list of strings
print(string_list)
print(locals()["string_1"])
print(locals()["string_6"])
print(locals()["string_4"])
