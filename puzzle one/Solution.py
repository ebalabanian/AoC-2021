Depths = open("puzzle one/Input","r")
Depths_list = Depths.readlines()
#print (Depths_list) 
#for num in Depths_list:
  #num = int(num)
  #print (num.type)
  #print(Depths_list[0])
count = 0
i = 0

for num in Depths_list:
  if (int(Depths_list[i]) - int(Depths_list[i+1])) <= 0:
    count = count + 1
  #print(Depths_list[0] - Depths_list[1])
  i += 1
  print(count)
  

print(count)



  #assign the num or make an array or comma delimited etcc.
  #compare 1 against the next
  #increment a counter