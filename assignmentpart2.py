#Task 1 
#Creating a List with
# the use of Numbers
# (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)
 
# Creating a List with
# mixed type of values
# (Having numbers and strings)
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values: ")
print(List)

# Create a list of 10 elements of four different data types like int, string, complex and float.
List = ["Deepika","Python", 1,2,3, 3 +4j,4+6j, 4.5,3.5,6.7]
print("\n List with four different data types")
print(List)

#Create a list of size 5 and execute the slicing structure

# Initialize list
Lst = [50, 70, 30, 20, 90]
 
# Display list
print(Lst[1:4])
# Display sliced list
print(Lst[::2])
 
# Display sliced list
print(Lst[::])

#Display sliced list
print(Lst[::-1])

#Write a program to get the sum and multiply of all the items in a given list.
#sum
list1 = [2 , 4,5,6]
list2 = ["deep", 3.41,"python"]
sum = list1 + list2
print(sum)
#product
lst1 =[1,2,3]
lst2 =[4,5,6]
products = []

for num1, num2 in zip(lst1,lst2):
    products.append(num1*num2)

    print(products)



#sum of all the elements in a list
total = 0

#creating list
list1 = [11,5,17,18,23]
for ele in range(0,len(list1)):
    total = total+list1[ele]
    print("sum of all the elements in a given list: ", total)


#4. Find the largest and smallest number from a given list.
number = [54,67,43,89,20,34]
number.sort()
print("largest element is:", number[5])
print("smallest element is:", number[0])

#5.Create a new list which contains the specified numbers after removing the even numbers from a
#predefined list.

#list with EVEN and ODD numbers

list = [11,22,33,44,55,66]
#print original list
print("Original list:")
print(list)

#loop
for i in list:
    if(i%2 == 0):
        list.remove(i)

#print list after removing even elements
print("list after removing Even numbers:")
print(list)

#6.Create a list of elements such that it contains the squares of the first and last 5 elements between
#1 and30 (both included).

def printValues():
    l = []
    for i in range(1,30):
        l.append(i**2)
        print(l[5:])
    

printValues

#Write a program to replace the last element in a list with another list.
#Sample input: [1,3,5,7,9,10], [2,4,6,8]

a = [1,3,5,7,9,10]
b = [2,4,6,8]
result = a[:-1]+b
print(result)