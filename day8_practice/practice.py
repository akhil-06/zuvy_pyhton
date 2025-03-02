# HomeWork - 4
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# https://leetcode.com/problems/valid-palindrome/description/
# https://leetcode.com/problems/majority-element/description/
# https://leetcode.com/problems/happy-number/description/
# https://leetcode.com/problems/most-frequent-even-element/


# merge two sorted lists
lst1 = [2,5,9,10,11,24,67];
lst2 = [1,6,9];
i=0;
j=0;
n1 = len(lst1);
n2 = len(lst2);
outputLst = [];

while i<n1 and j<n2:
    if lst1[i] < lst2[j]:
        outputLst.append(lst1[i])
        i=i+1;
    else:
        outputLst.append(lst2[j])
        j=j+1;

while i<n1:
    outputLst.append(lst1[i]);
    i=i+1;

while j<n2:
    outputLst.append(lst2[j])
    j=j+1;

print(outputLst);
# reverse the words in the string
# s = "Hello my name is Akhil Sharma";
# # spilit the string inti list
# lst = s.split();
# # rv = reversed(lst);
# # print(rv);
# reversed_string = "";

# for i in reversed(lst):
#     reversed_string += i + " ";

# # how to remove the trailing spaces from a string:- strip
# reversed_string = reversed_string.strip();
# print(reversed_string);




# rotate Array d times
# lst = [1,2,3,4,5,6,7];
# d = 3;

# for i in range(d):
#     lst.insert(0, lst.pop())

# print(lst);