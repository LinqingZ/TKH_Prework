def greet(name):
    print ("hello "+name)

greet("joe")
greet("sam")

def add(num1, num2):
    return num1+num2

add(1,2)
num_sum=add(1,2)
print(num_sum)

def largest(a, b):
    if a>b:
        return a
    else:
        return b

num_largest=largest(8, 6)
print (num_largest)