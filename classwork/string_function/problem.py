# create a list of 10 numbers print the sum of last 4 elements of the list find out the difference between max and min element of the list insert item or no in a list at 6th position this no must be 1/3 of no stored at 4th position 

list = [5,10,84,46,8,97,2,3,1,59] 
print("previous : ",list)
print(sum(list[-4:]))
print("max : ",max(list))
print("min : ",min(list))
print("difference between min max : ",max(list)-min(list))
list.insert(5,int(list[3]/3))
print("updated : ",list)