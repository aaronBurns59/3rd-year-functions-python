def printList(l):
    for x in l:
        print(x)

list1 = [0,1,2,3,4,5,6,7,8,9,10]
list2 = ['apple', 'orange', 'banana', 'pear', 'kiwi']
list3 = [0.1,2.0,3.3,4.5,8.5]

choice = int(input("Enter which list you want 1, 2 or 3: "))

if choice == 1:
    list = list1
elif choice == 2:
    list = list2
elif choice == 3:
    list = list3 

printList(list)

