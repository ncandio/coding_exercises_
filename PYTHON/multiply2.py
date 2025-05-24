from functools import reduce
import operator

def arrayOfProducts(array):
    output = []
    for i in range(len(array)):
        prod_element = [array[j] for j in range(len(array)) if j != i]
        output.append(reduce(operator.mul, prod_element, 1))   
    return output
