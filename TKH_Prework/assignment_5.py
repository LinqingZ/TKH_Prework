thing="car"
print(thing[0])
print(thing[2])
list=["one", 2,"3hree"]
print(list[2])

even=0
odd=1
b=[]
c=[]
names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
for i in range(0, len(names_list)):
    if i % 2:
        b.append(names_list[i])
    else:
        c.append(names_list[i])
        
print("even list= "+str(b))
print("odd list= "+str(c))
