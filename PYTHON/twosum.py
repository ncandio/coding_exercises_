def twoNumberSum(array, targetSum):
    result = [[x,y] for x in array for y in array 
              if x < y and x+y==targetSum]
    if result:
        return result[0]
    return []