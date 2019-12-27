from math import factorial
def listPosition(word):
  if not word:
      return 1
  mul = lambda x, y: x * y
  divisor = reduce(mul, (factorial(y) for x, y in set((char, word.count(char)) for char in word)))
  return sorted(word).index(word[0]) * factorial(len(word) - 1) / divisor + listPosition(word[1:])

print(listPosition("bananonesopremo"))
