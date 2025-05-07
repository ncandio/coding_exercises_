def threeNumberSum(array, targetSum):
    return sorted([[x,y,z] for x in array
                    for y in array 
                    for z in array 
                    if x+y+z == targetSum and x < y < z] )