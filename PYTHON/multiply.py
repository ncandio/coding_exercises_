import math

def arrayOfProducts(array):
    output = []
    for i in range(len(array)):
        prod_element = [array[j] for j in range(len(array)) if j != i]
        output.append(math.prod(prod_element))   
    return output
      