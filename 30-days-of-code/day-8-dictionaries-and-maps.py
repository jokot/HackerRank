# Enter your code here. Read input from STDIN. Print output to STDOUT

phone_dict = {}
for i in range(int(input())):
    contact = input().split()
    phone_dict[contact[0]] = contact[1]
while True:
    try:
        name = input()
        print(name+"="+phone_dict[name])    
    except EOFError:
        break
    except:
        print("Not found")
        