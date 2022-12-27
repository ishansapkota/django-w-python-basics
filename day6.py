#file_handling

#the key function for working with files is open() which takes two parameters filename, mode of file like read etc



# file = open("movies.txt","rt") #---> yo file arkai thauu ma cha bhaney tesko absolute path diyera access garna ni milcha
# file_contents = file.read()
# print(file_contents)

#FOR READING

# filename = "C:\\Users\\Lenovo\\Desktop\\test.txt"       #==> python ma path haaldaa double backslash haalnu parch

# file = open(filename,'rt')

# filecontents = file.read()
# print(filecontents)

#FOR WRITING

# filename = "C:\\Users\\Lenovo\\Desktop\\test.txt"       #==> python ma path haaldaa double backslash haalnu parch

# file = open(filename,'wt')

# file.write('Titanic\n')
# file.write('Avatar 2')

#write mode ma if hamiley specify gareko path ma file chaina bhaney tyo path ma file paahila create garera ani tesma write garidincha 
#ani write mode ley if tyo hamiley raakheko path ma already texts or anyything cha bhaney teslai overwrite garidincha

#if we want to add texts or anything in that file without overwritting it we have to use the file mode as append-->'at'

# filename = "C:\\Users\\Lenovo\\Desktop\\test.txt"       #==> python ma path haaldaa double backslash haalnu parch

# file = open(filename,'at')        

# file.write('Titanic 2\n')
# file.write('Avatar 3')


# #files lai bulk ma write garney ho bhaney writelines function ma list banaayera garidiney 

# filename = "C:\\Users\\Lenovo\\Desktop\\test.txt"       #==> python ma path haaldaa double backslash haalnu parch

# file = open(filename,'at')

# file.writelines(['\nValorant','\nCS:GO'])
# file.close()

# IF HAMILAI EKKAICHOTI READ NI GARNA MANN CHA RA WRITE NI GARNA MANN CHA BHANEY R+ file-mode use garney 

#deleting the file 
# import os

# os.remove() #---> remove function ma chahi directory name lekhera delete 

# filename = "C:\\Users\\Lenovo\\Desktop\\test.csv"

# file = open(filename,'wt')

# file.writelines(['Name, Age, Gender'])
# file.close()

import csv

data =[
    {
    "Name" : "Bishal",
    "Age"   : 22,
    "Gender" : "Male"
},
{
    "Name" : "Ishan",
    "Age"  : 22,
    "Gender": "Male"
}
]

# filename = "D:\\Programming folder\\Python programs\\Python with DJANGO basics\\test.csv"

# file = open(filename,'wt')

# file.writelines(['Name, Age, Gender \n'])

# for i in range(0,len(data)):
#     file.writelines([input(), input(), input()])
    

keys = data[0].keys()

with open('test.csv','w',newline='') as csvfile:
    writer = csv.DictWriter(csvfile,keys)
    writer.writeheader()
    writer.writerows(data)