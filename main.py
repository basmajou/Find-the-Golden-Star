import random 

def print_map(map):
  for item in map:
    for item2 in item:
      print(item2,end = ' ')
    print("\n")
  
map = ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

print("This is our initial map:\n")
print_map(map)

random_row = random.randint(0,2)
random_column = random.randint(0,2)
map[random_row][random_column] = '⭐️'
#gold_position = str(random_row+1)+str(random_column)
#print(random_row,random_column)
print("What do you think: where is the Golden Star in the map? ")

row = input("Row position(1-3): ")
row = int(row)-1

column = input("column position(1-3): ")
column = int(column)-1


print()

if row == random_row and column == random_column:
  print("Congratulations!!! You have found the Golden STAR!\n")
else:
  print("Unfortunatly you could find it 🙁\n")
  map[row][column] = "🆇 "

print_map(map)