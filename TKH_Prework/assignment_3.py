print(len("hello"))
name="joe"
print(len(name))
longest_name=""
names_list=["bob","jimmy", "max b","bernie","jordan","future hendrix"]
for name in names_list:
    if len(name)>len(longest_name):
        longest_name=name
print(longest_name)
