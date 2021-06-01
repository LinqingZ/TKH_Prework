thing="car"
print(thing[0])
print(thing[2])
list=["one", 2,"3hree"]
print(list[2])

even=0
odd=1
even_list=[]
odd_list=[]
names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
for i in range(0, len(names_list)):
    if i % 2:
        even_list.append(names_list[i])
    else:
        odd_list.append(names_list[i])
        
print("even list= "+str(even_list))
print("odd list= "+str(odd_list))