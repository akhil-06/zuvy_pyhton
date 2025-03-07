# Functions
def sum(a,b):
    # print(a+b);
    return a+b;


ans = sum(4,5);
print(ans);

# tuple packing
# a,b,c  = 10,20,30;
# a=10
# b=20
# c=30
# laksmi = (a,b,c);
# print(laksmi[0:1])
# print(type(laksmi))



# ways to create tuple
# tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
# tpl = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10;
# tpl = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
# tpl = ()
# tpl = (10)
# print(tpl);
# print(type(tpl));


# list -> tuple ?
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
# tpl = tuple(lst);
# print(tpl)





# delete the whole tpl, u can't delete the single element
# tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, True,"Single", False,"Akhil");
# del tpl
# print(tpl)
# print(len(tpl))



# Slicing in tuple
# tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
# t3 = tpl[::-1]  //to reverse we are doign this

# print(t3)



# t = ('python',)*50
# print(t)



# Nested tuples
# tpl1 = (1, 2, 3, 4, 5);
# tpl2 = (6, 7, 8, 9, 10);
# t3 = (tpl1, tpl2)
# print(t3)



# tpl1 = (1, 2, 3, 4, 5);
# tpl2 = (6, 7, 8, 9, 10);
# tpl3 = tpl1 + tpl2;
# print(tpl3)
# print(tpl1)
# print(tpl2)


# for i in tpl:
#     print(i)


# print(tpl[-1])
# print(tpl[-2])
# print(tpl[-3])
# print(tpl[-4])
# print(tpl[-5])




# tpl = (1, 2, 3, 4, 5);
# tpl[2] = 40000;
# print(tpl)
# print(tpl[0])
# print(tpl[3])


# lst = [1, 2, 3, 4, 5]
# lst[2] = 40000
# print(lst)
# tpl = (1, 2, 3, 4, 5)
# print(type(lst))
# print(type(tpl))


# print("Hello world!")