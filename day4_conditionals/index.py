# no. of days:- , till 5days = 2rs/day,, 6-10:- 3/day 11-15:- 4/day, after 15:- 5/day

nd = int(input("Enter the number of days = "));
if nd <= 5:
    amt = nd*2;
elif nd > 5 and nd <= 10:
    amt = 10 + (nd-5)*3;
elif nd > 10 and nd <= 15:
    amt = 25 + (nd-10)*4;
else:
    amt = 45 + (nd-15)*5;
print("Amount to be paid = ", amt);



# kmc = int(input("Enter the kilometer = "))

# if kmc <= 10:
#     amt = kmc*11;
# elif kmc > 10 and kmc <=100:
#     amt = 110 + (kmc-10)*10;
# elif kmc > 100:
#     amt = 1010 + (kmc-100)*9;

# print("Total amount to be paid: Rs.", amt);




# conditionals
# 6. Match case
# number = 9
# match number:
#     case 5:
#         print("one")
#     case 2:
#         print("two")
#     case 3:
#         print("three")
#     case 4 | 5:
#         print("four or five")
#     case _:
#         print("other number")






# 5. Ternary Condtion statement
# age = 20;
# s = "Adult" if age >= 18 else "Minor";
# print(s)





# 4. nested if-else statements
# age = 70;
# is_member = True;
# if age >= 60:
#     if is_member:
#         print("30% discount");
#     else:
#         print("20% discount");
# else:
#     print("you are not eligible to get any discount");






# 3. elif
# age = 45;
# if age <= 12:
#     print("you are a child")
# elif age <=19:
#     print("you are a teenager")
# elif age <= 35:
#     print("you are a young person")
# else:
#     print("you are an old person")



# 2. if else statement
# age = 20;
# if age >= 12:
#     print("you can travel for free")
# else:
#     print("you have to pay for the ticket")

# short hand
# print("you have to pay for the ticket") if age<=12 else print("you can travel for free");



# 1. if
# age = 20;
# if age >= 18:
#     print("You are eligible to vote")

# short hand
# if age>= 18 : print("You are eligible to vote")






# print("conditioals")