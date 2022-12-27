#DICTIONARY

d = {
    "Brand": "Lamborghini",
    "Model" : "Aventador",
    "Year"  : 2008
}
# print(d["Brand"])

# print(len(d))

#PYTHON MA 'dict' bhanney inbuilt keyword cha 

# user = dict(name = 'Ram', age = '23', is_Married = True)

# print(user["name"])

# print(d.get('Model',None))  #--> this dictionary function helps to get the values where get(<key name>,<if chaina bhaney k print garney>)
# print(d.keys()) #--> this function returns the list of keys
# print(d.values()) #--> this function returns the list of values

# d['Owner'] = 'Francesco'    #----> this helps to add the keys and values in the dictionary 
# d['Year'] = 2011        #---> this helps to ovwrride the keys and its values

# print(d)

# print(d.items())    #this gives list of values in list or tuples form whose 0th index is key and 1sst index is values 


# if 'Year' in d:
#     print(d['Brand'])

# d.update(
#     {
#        'Year' : 2009,   #---. yelley maathi ko value update gariraako 
#         'Country': 'Italy'  #--> yelley naya key ra tesko value add garidiyo dictionary ma 
#     }
# )

# d.pop('Country')    #--> this function pops out the given keyword
# print(d)

# nikaaleko_key_ko_value = d.pop('Brand')
# print(nikaaleko_key_ko_value)


# del d['Country']    #---> this del keyword is universal and deletes the dictionary, variables, keys 

# print(d)

for i in d:
    print(f'{i}----->{d[i]}')


#the best way of getting value in a dictionary is by using get() function! 