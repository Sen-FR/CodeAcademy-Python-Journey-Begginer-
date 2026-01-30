print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 6

# Write an if statement below:
if planet == 3:
  print("This is your weight on jupiter")
  print(weight * 2.34)
elif planet == 2:
  print("This is your weight on Mars")
  print(weight * 0.38)
elif planet == 1:
  print("This is your weight on Venus")
  print(weight * 0.91)
elif planet == 4:
  print("This is your weight on Saturn")
  print(weight * 1.06)
elif planet == 5:
  print("This is your weight on Uranus")
  print(weight * 0.92)
elif planet == 6:
  print("This is your weight on Neptune")
  print(weight * 1.19)
