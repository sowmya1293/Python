def volume_of_sphere(radius):
  PI = 3.14
  fraction = 4/3

  volume = fraction*PI*(radius)**3

  return volume


result = volume_of_sphere(2)
print(result)