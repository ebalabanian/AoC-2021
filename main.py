Directions = open("puzzle three/Input","r")
Directions_list = Directions.readlines()

x_position = 0
y_position = 0
z_position = 0
Directions = {}

for line in Directions_list:
  line.split()
  print(line)
  if "forward" in line:
      x_postion += num in line
  if "up" in line:
   # y_position = y_position - int(line[1]) 
    #subrtract from Y
  #if "down" in line:
    #add to x
  #print(x,y)
  #print(Directions)

#print (Directions)