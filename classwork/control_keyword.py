# loop contrl keywords 
# 1 pass -- it is a placeholder which does nothing for now and we are going to work or write a logic later in it 
# 2 continue -- skips current iteration
# 3 break -- exits loop immediately
# loop else -- if i want to perform some operations and i want acknowlegdement then use it 


for i in range(5) :
  pass

for i in range (3):
  if i==1:
    continue
  print (i)

for i in range (3):
  print (i)
  if i==1:
    break

for i in range (3):
  print (i)
else :
  print("loop finished without else ")


