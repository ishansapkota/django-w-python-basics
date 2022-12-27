#print('HelloWorld')


#OPERATORS

# / --> this operator is used in normal division 
# // --> this operator is used in integer division
# % --> this operator is used in modular division 
# a = 30
# b = 4

# print(a/b)
# print(a//b)
# print(a%b)

# # **    -->this operator is used as the power sign
# print(2**2) #the result of this logic gives 2 ko power 2 

# a = int(input('The number is: '))
# print(f'The next number for the number {a} is ',a+1)
# print(f'The previous number for the number {a} is ',a-1 )


#snakify ko "input,print and numbers" section ko "timestamp" wala question ko mero solution

# hr1 = 0
# min1 = 0
# sec1 = 0 

# hr1 = int(input('First hour: '))
# min1 = int(input('First minute: '))
# sec1 = int(input('First second: '))

# hr1 = hr1 + min1//60 +sec1//3600
# min1 = min1 + sec1//60 
# sec1 = sec1

# hr2 = 0
# min2 = 0
# sec2 = 0

# hr2 = int(input('Second hour: '))
# min2 = int(input('Second minute: '))
# sec2 = int(input('Second second: '))

# hr2 = hr2 + min2//60 + sec2//3600
# min2 = min2 + sec2//60
# sec2 = sec2

# # if (hr1-hr2)<=0:
# #     hr = 0
# # else:
# #     hr = hr1-hr2

# # if(min1-min2)<=0:
# #     min = 0
# # else:
# #     min = min1-min2

# hr = (hr2 - hr1)*3600
# min = (min2 - min1)*60
# sec = sec2-sec1
# time = hr + min + sec
# print(abs(time))

#snakeify ko desk wala question 

# a = int(input("Enter the number of students in class first: "))
# b = int(input("Enter the number of students in class second: "))
# c = int(input("Enter the number of students in class third: "))

# #for a 
# if(a %2==0):
#     n1 = a//2
    

# elif(a %2!=0):
#     n1 = a//2 +1
    
    
# #for b 
# if(b % 2 ==0):
#     n2 = b//2
  

# elif(b % 2 !=0):
#     n2 = b//2 +1 
    

# #for c 
# if (c % 2 == 0):
#     n3 = c//2
    

# elif(c % 2 != 0):
#     n3 = c//2 + 1
    
# n = n1 + n2 + n3
# print(n)

#snakify ko dictionary wala ko 1st question ko answer
# s = input()

# words = {}
# counts = []
# for word in s.split():
#     if word not in words:
#         words[word] = 0
#     else:
#         words[word] += 1
#     counts.append(words[word])

# n = len(counts)

# print(n)
# for i in range(0,n,1):
#     print(counts[i])

# mathi ko question ko alternative answer

# counter = {}
# for word in input().split():
#     counter[word] = counter.get(word, 0) + 1
#     print(counter[word] - 1, end=' ')

#snakify ko dictionary ko 2nd question

# a = {}
# n = int(input("Enter the number of keys and values to be made: "))

# for i in range(0,n):
#     keys = input("Enter the key: ")
#     values = input("Enter the values: ")

#     a.update({keys:values})
# print(a)

# word = input("Enter the word of which synonym is to be found: ")

# # Loop over the dictionary and check if the word is a key or a value
# for keys, values in a.items():
#     if word == keys:
#         synonym = values
#         break
#     elif word == values:
#         synonym = keys
#         break
# print(synonym)



# election = {}

# num_of_records = int(input("Enter the number of records in the election: "))

# for i in range(0,num_of_records):
#     keys = input("Name of the candidate: ")
#     values  = int(input("Number of votes casted on the candidate: "))

#     election.update({keys:values})



# # List of records
# records = {}
# n = int(input("Enter the number of records: "))

# for i in range(0,n):
#     keys = input("Name of the candidate: ")
#     values = int(input("Number of votes casted on the candidate: "))
#     records.update({keys:values})
# # Dictionary to store the number of votes for each candidate
# votes = {}

# # Loop over the records and update the dictionary with the number of votes for each candidate
# for keys, values in records:
#     if keys not in votes:
#         votes[keys] = 0
#     votes[keys] += values


# # Print the number of votes for each candidate
# for candidate in sorted(votes):
#     print(f"{candidate}: {votes[candidate]}")

a = float(input())

b = int(a)

if b==0:
    print(0)


else:
    div = a%b
    div_str = str(div)
    power = len(div_str)
    actual_power = int(power-2)
    decimal_numbers = div*pow(10,actual_power)
    first_digit = decimal_numbers//pow(10,actual_power-1)
    first_digit_int = int(first_digit)



    print(first_digit_int)
