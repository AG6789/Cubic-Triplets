# Tri Cube Eq

# Odd number, number of iterations

firstNumber = 1
secondNumber = 3
continueCheck = 1000000000000000000000

# Root Finder

def quadCheck(cube):
    a = 6
    b = 12
    c = 8 - cube

    sol1 = (-b + (b**2 - (4*a*c))**0.5)/(2*a)
    sol2 = (-b + (b**2 - (4*a*c))**0.5)/(2*a)
    
    
    if sol1.is_integer() == True:
        thirdNumber = sol1
        return thirdNumber
    elif sol2.is_integer() == True:
        thirdNumber = sol2
        return thirdNumber
    else:
        thirdNumber = 0
        return thirdNumber
    
# Actual Check 

for v in range(continueCheck):
    
    cubeSum = (firstNumber**3) + (secondNumber**3)
    thirdNumber = quadCheck(cubeSum)
    
    if thirdNumber != 0:
        finalNumber = round((firstNumber**3 + secondNumber**3 + thirdNumber**3)**(1/3))
        print("Found! The numbers are ", firstNumber, ",", secondNumber, ",", int(thirdNumber), ",", finalNumber)
        
    firstNumber += 2
    secondNumber += 2