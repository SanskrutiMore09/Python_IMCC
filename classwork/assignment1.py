# create dictionaries with student details 
students = {
  101:{"name" : "sakshi" , "scores":[45,80,90]},
  102:{"name" : "meena" , "scores":[80,85,70]},
  103:{"name" : "kavya" , "scores":[88,56,60]},
  104:{"name" : "krisha" , "scores":[90,80,70]},
  105:{"name" : "veera" , "scores":[65,75,85]}
}

# calculate avg score and flag pass or fail 
for sid, details in students.items():
  avg = sum(details["scores"])/len(details["scores"])
  details["Average"]=avg
  details["passed "]= avg>= 50 # details["passed "]= avg>= 50 boolean flag 

# print names of students who passed 
for sid , details in students.items():
  if details["passed "]:
    print(details["name"])

# print(students) 