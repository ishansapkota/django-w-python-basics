#while loop

# while True:
#     print("HelloWorld")
#     break

# counter = 0 
# while counter < 10:
#     print(counter)
#     if counter == 4:
#         break 
#     counter +=1

# #exception handling

# try:
#     a = 2/0     #--> exception auna sakney statement lai try ma raakhney ani tesma exception aayo bhaney except ma jaancha 
# except:
#     print("You cannot divide by zero")  #except ma bhaako chij chahi execute huncha


# try:
#     print('Dividing by zero.')
#     a = 2/0
#     print("Divided by zero ")
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
# else:
#     print("No exceptions to handle.")
# finally:
#     print("End of the try.")

while True:
    try:
        integer_input = int(input("Enter the integer: "))
        print(f"The integer given was: {integer_input}")
        break
    except ValueError:
        print('Invalid input')


