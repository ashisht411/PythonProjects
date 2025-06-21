#create a 5x5 array of random numbers and normalize it
import numpy as np

def evenOnlyArray(arr):
  even_numbers = arr[arr%2==0]
  return even_numbers

def normalizedArray(arr):
  xmin = np.min(arr)
  xmax = np.max(arr)
  nArray = (arr - xmin) / (xmax - xmin)
  return nArray

if __name__ == "__main__":  # just to generate a random array 
  arr = np.random.randint(1, 11, size=(5, 5))
  arr2 = np.random.randint(1,10,size=(1,10))
  print('Original even Array:')
  print(arr2)
  #print(normalizedArray(arr))
  print(evenOnlyArray(arr2))

