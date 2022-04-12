Depths = open("puzzle one/Input","r")
Depths_list = Depths.readlines()


count = 0
i = 0
Depths_integers = []

for num in Depths_list:
  Depths_integers.append(int(num))

for num in Depths_integers:
  if ((Depths_integers[i]+Depths_integers[i+1]+Depths_integers[i+2]) - (Depths_integers[i+1]+Depths_integers[i+2]+Depths_integers[i+3]))<0:
    count = count + 1
    print("increasing")
  i += 1
  print(count)

print(count)
