is_hot=False# True 
if is_hot:
    print("Its a hot day")
    print("Enjoy your day")
else:
    print("Its a cold day")
    
is_beautiful=True
is_ugly=False
if is_beautiful:
    print("Good")
elif is_ugly:
    print("oh")
else:
    print("sad")

price=100000
has_good_credit= True
if has_good_credit:
    down_payment=0.1 * price
else:
    down_payment=0.2 * price
print(f"Down payment:{down_payment}")

#logical operator
#and: both condition true
#or: at least one condition true
has_high_income= True
has_good_grade= True

if has_high_income and has_good_grade:
    print("Eligible ")
    
temp=30
if temp>30:
    print("it's a hot day")
else:
    print("its cold day")