print(len("hello"))
name="joe"
print(len(name))

names_list=["bob","jimmy", "max b","bernie","jordan","future hendrix"]
for name in names_list:
    longest_name=""
    if len(name)>len(longest_name):
        longest_name=name
print(longest_name)