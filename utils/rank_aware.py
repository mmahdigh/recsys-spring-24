import math

# def calculate_relative_weight(index):
#   return 1 / (index + 1)


def calculate_relative_weight(index):
  return 1

# def calculate_relative_weight(index):
#   return 1 / math.pow(index + 1, 2)

# def calculate_relative_weight(index, total):
#   cutoff = 10
#   if (index >= cutoff): return 0
#   effectiveTotal = min(cutoff, total)
#   sum = sum_reciprocals(effectiveTotal)
#   # print("sr:", sum)
#   return (1 / (index + 1)) / sum  # 1 / (1 + 0.5 + 0.33 + 0.25 ... + 0.1) 


def sum_reciprocals(N):
    return sum(1/i for i in range(1, N+1))
  
  
# print(calculate_relative_weight(0, 40))