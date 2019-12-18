#list comprehension basic 
#Authored : codename_123
#date : 18/12/19,wednesday

nums = [1,2,3,10,4,3,18,43,4,21,43,90]

for i in nums:
	print(i,end=',')

new_nums = [i for i in nums]
print('\nnew list',new_nums)

#task 1 
#we have given a list of 100 numbers from 1 to 100 and have to store all even numbers in a new list 

list_1_to_100 = [i for i in range(1,101)]
# print(list_1_to_100)
list_of_even_numbers = [i for i in list_1_to_100 if i%2 == 0]
print('filtered even numbers : ',list_of_even_numbers)

# we can do above task using lambda function too
find_even = lambda x : x%2==0
list_of_even_numbers = filter(find_even,list_1_to_100)
print('extracted even numbers : ')
for i in list_of_even_numbers:
	print(i,end=',')

nums1 = [i for i in range(1,11)]

square = lambda x : x*x
sqrs = map(square,nums1)
# print(sqrs) #this gives the address of first element 
# just iterate the list to get the elements 

for sqr in sqrs:
	print(sqr,end=',')

# # extract all vowels 
# alphabet = ['a','b','c','d','e','f','g','h','i','j','k',
# 'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# vowels = ['a','e','i','o','u']
print()
lst =  [num for num in range(1,15)]
lst_odd = filter(lambda x : x%2 != 0,lst)
print('filtered odd numbers : ')
for odd in lst_odd:
	print(odd,end=',')
print()
lst1 = [1,2,3,4,5]
lst2 = [1,5,3,5,10]

zipped_lst = zip(lst1,lst2)
print('zipped lst : ')
for i in zipped_lst:
	print(i,end=',')

print()
add_lst = lambda x,y : x+y 
added_lst = map(add_lst,lst1,lst2)
print('added result : ')
for val in added_lst:
	print(val,end=',')
print()