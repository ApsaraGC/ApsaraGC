temp= 20
if temp > 20:
    print("Its a hot day")
else:
    print("Its a cold day")
    
name="Afggggh"
if len(name)< 2:
    print("Name at least 3 character")
elif len(name)>2:
    print("maximum of 10 character")
else:
    print("ffff")
    
#weight coverter
weight= int(input("Weight:"))
unit=input('(l)bs or (k)g:')
if unit.upper()=="l":
    converter= weight * 0.45
    print(f"You are{ converter} kilos")
else:
    converter= weight/0.45
    print(f" You are {converter} pounds")
    
#while loops
i=1
while i <=5:
    print(i)
    i=i+1
print("Done")

#building guessing game
secret_number=2
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess= int(input('Guess:'))
    guess_count +=1
    if guess== secret_number:
        print("wow")
        break
    
