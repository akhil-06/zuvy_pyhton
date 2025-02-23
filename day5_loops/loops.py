# Homewrok - 1
# Exercise 13: Find the factorial of a given number
# Exercise 14: Reverse a integer number
# Exercise 15: Print elements from a given list present at odd index positions
# Exercise 16: Calculate the cube of all numbers from 1 to a given number
# Exercise 17: Find the sum of the series up to n terms






# prime number or not
num = int(input("Enter the number- "));

if num == 0 or num == 1:
    print(num, "is unique number");
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is a Composite number");
            break;
    else:
        print(num, "is a Prime number");


# for i in range (1,11) :
#     print(19*i)

# Pass keyword
# n=10;
# if n<20:
#     pass
#     # print("N is less than 10");

# for i in range(0,10):
#     pass






# nested while loop
# x = 1
# while x <= 3:
#     y = 1
#     while y <= x: 
#         print(x , y)
#         y += 1
#     x += 1




# While Loop
# num = int(input("Enter your number : "))
# while num != 0:
#     print(num);
#     num = int(input("Enter your number : "))

# print("You Have enetered the 0")



# number = 1;
# while number<=4:
#     print(number);
#     number = number + 1
    # number++;





# nested loops
# for i in range(0,2):
#     for j in range(0,2):
#         print (i,j);
#     print("--------------")




# vlaues = range(0,4);
# for i in range(0,10):
#     if (i == 2 or i == 6 or i == 9):
#         continue;
#     print(i)




# languages =  [ 'Swift', 'Go', 'Python', 'Java'];
# languages = "Javascript";

# access the elements one by one
# for(int i=0;i<10;i++){}
# Syntax of for loop in python
# for akhil in languages:
#     print(akhil)
#     print("--------------------------------")

# print("End of the loop");





# print("Zuvy")
# print("Zuvy")
# print("Zuvy")
# print("Zuvy")
# print("Akhil")
# print("Zuvy")
# print("Akhil")
# print("Akhil")
# print("Akhil")
# print("Akhil")