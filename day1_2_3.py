# # if statement

# if 5>4:
#     print("5 is greater than 4")
    
#     if 5>3:
#         print("5 is greater than 3")

#         if 0>2: #since yo statement is false yo block ma chirdai chirdaina so yo tala ko true statement pani print hudaina 
#             print("0 is greater than 2.")

#             if 5>1:
#                 print('5 is greater than 1')
# else:
#     print("5 is not greater than 4")


# # TYPE CASTING

# a = '10' #since it consists of inverted comma so it is string 

# int(a) #this syntax helps in the type casting the string to integer, but in the case of type casting
#         #only the variables which can be changed into the other variable type can be typecasted, like 10a cannot be an integer type
# print(type(a))


# #we can assign values to multiple variable

# int_example, str_example = 1, 'NCIT'

# print(int_example,str_example)

# #Collection of objects

# tuple_example = (1,2,3,4) #this cannot be modified or updated

#list_example = [1,2,3,4] #this can be modified or changed tala ko example le 
# list_example.append(5)  #yo append wala function le chahi value add garna 
# print(list_example) 

# list_example.insert(2,9)  #yo function le chahi 2nd index ma aafuley raakhna khojeko value haaldincha yo case ma 9
# print(list_example)

#for i in list_example(range = 3):
#   print(i)
list_example = [1,2,3,4,5]

# list_example.append(6)
# print(list_example)

# list_example.clear()
# print(list_example)

# list_example.copy()
# print(list_example)

# list_example2 = ['Ishan']

# list_example.extend(list_example2) #extends in other can be called concatenate as well
# print(list_example + list_example2)
# print(list_example)

# print(len(list_example))

# aa = -10

# print(abs(aa))

# for i in range(0,5,2):
#     print(list_example[i])

# for i in range(0,101,2):    #range ko bracket ko first-->
#     print(i)

#appending odd numbers from 1 to 100 in a list
# odd_numbers = []

# for i in range (1,100,2):
#         odd_numbers.append(i)
#         print(odd_numbers)

#USING FUNCTION
# def ishan():
#     print("My name is Ishan")

# ishan()

# def print_helloworld():
#     print("HELLO WORLD")
#     return '1'
# a = print_helloworld()
# print(a)

# def print_word(word):
#     print(word)

# print_word("hey")

# word = 'hey'
# print_word(word)

# def add_numbers(first,second):
#     sum = first + second
#     return sum
# a = add_numbers(2)
# print(a)


# def add_numbers(first,second=2):
#     sum = first + second
#     return sum
# a = add_numbers(2)
# print(a)


#write a function that returns a list with odd numbers from 1 to 100

# def oddnumbers_1to100():
#     list_oddnumbers = []
#     for i in range(1,100,2):
#         list_oddnumbers.append(i)
    
#     return list_oddnumbers
# a = oddnumbers_1to100()
# print(a)


#write a function that returns true if the function is prime

# def oddnumbers_in_range(start,stop):
#     list_oddnumbers = []
#     for i in range(start,stop,2):
#         list_oddnumbers.append(i)
#     return list_oddnumbers
# a = oddnumbers_in_range(1,1000)
# print(a)

# def prime_num(num):
#     if num > 1:
#         for n in range(2,num):
#             if (num%n) == 0:
#                 return False
#         return True
#     else:
#         return False
# print(prime_num(39))
# print(prime_num(11))

# def prime_num(num):
#     if num <= 1:
#         raise Exception(f'Invalid argument{num}')   #range ma 1 dekhi suru garyo bhaney print garney bela tei 1 mai output rokkincha
#     for n in range(2,num):
#             if (num%n) == 0:
#                 return False
#     return True

# for  i in range (2,101):
#     if prime_num(i) == True:
#         print(f'{i} --> Prime')
#     else:
#         print(f'{i} --> Composite')

# write a program that loops from 1 to 100 and prints FIZZ if the number is divisible by 3, prints BUZZ if divisible by 5 and FIZZBUZZ
#if it is divisible by 3 and 5

# for i in range (1,101):
#     if i%3 == 0:
#         print(f'{i}-->FIZZ')
#     if i%5 == 0 :
#         print(f'{i}-->BUZZ')
#     if i%3 & i%3 == 0:
#         print(f'{i}-->FIZZBUZZ')
#     else: 
#         print('Nothing')

#condition chahi 

# def divisible():
#     for num in range(1,101):
#         if num%3==0 and num%5==0:
#             print(f'{num}-->FIZZ BUZZ')
#         elif num%3 == 0:
#             print(f"{num}-->FIZZ")
#         elif num%5 == 0:
#             print(f'{num}-->BUZZ')
        
 
# divisible()

# list_example = []

# if len(list_example)==0:
#     list_example = int(input("Enter the numbers for the list: "))
# for  i in range(0,len(list_example),2):
#     print(list_example)

# # for i in range(0,2):
# #     print(list_example[i])

A = []


while len(A) == 0:
  A = input("Enter a list of numbers: ")

  A = [x for x in A.split()]

for i in range(0, len(A)):
  if A[i]%2==0:
    print(A[i])
