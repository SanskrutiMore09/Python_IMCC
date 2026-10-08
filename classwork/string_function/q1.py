# create a list of no and string accept the value from user seperate the list from the maximum no display the names in descending order 
list = []
no_elem = int(input("how many no of elments : "))
for i in range (no_elem):
  num = input(f"enter {i}th elements in list : ")
  list.append(num)
print (list)
list.remove(max(list))
print (list)
print(sorted(list,reverse=True))

