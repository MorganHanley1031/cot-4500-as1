
def check_for_alternating(function_we_got: str):
    term_check = check_for_negative_1_exponent_term(function_we_got)

    return term_check

def check_for_decreasing(function_we_got: str, x: int):
    decreasing_check = True
    k = 1
    starting_val = abs(eval(function_we_got))
    for k in range(2, 1000):
        result = abs(eval(function_we_got))

        #print(result)
        if starting_val <= result:
            decreasing_check = False

    return decreasing_check

def check_for_negative_1_exponent_term(function: str) -> bool:
    if "-1**k" in function:
        return True
    return False

def absolute_error(precise:float, approximate: float):
    
    sub_operation = precise - approximate
    return abs(sub_operation)

def relative_error(precise:float, approximate: float):

    sub_operation = absolute_error(precise, approximate)
    div_operation = sub_operation / precise
    return div_operation



#---------------------------------------------------------------------------------------------------

def bisection_method(left: float, right: float, given_function: str,tolerance: float):

    # pre requisites
    # 1. we must have the two ranges be on opposite ends of the function (such that
    # function(left) and function(right) changes signs )
    x = left
    intial_left = eval(given_function)

    x = right
    intial_right = eval(given_function)
    
    if intial_left * intial_right >= 0:
        #print("Invalid inputs. Not on opposite sides of the function")
        return

    diff: float = right - left
    
    # we can only specify a max iteration counter (this is ideal when we dont have all
    # the time in the world to find an exact solution. after 10 iterations, lets say, we
    # can approximate the root to be ###)
    max_iterations = 200
    iteration_counter = 0
    while (diff >= tolerance and iteration_counter <= 20):
        
        iteration_counter += 1
        # find function(midpoint)
        mid_point = (left + right) / 2
        
        x = mid_point
        evaluated_midpoint = eval(given_function)

        if evaluated_midpoint == 0.0:
            break
        
        # find function(left)
        x = left
        evaluated_left_point = eval(given_function)
        
        # this section basically checks if we have crossed the origin point (another way
        # to describe this is if f(midpoint) * f(left_point) changed signs)
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0

        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point
        
        diff = abs(right - left)

        # OPTIONAL: you can see how the root finding for bisection works per iteration
        #print(mid_point)
    return (iteration_counter)   


#-----------------------------------------------------------------------------------------------
def custom_derivative(value):
    return (3*(value*value)) + (8*value)

def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    # remember this is an iteration based approach...
    iteration_counter = 0

    # finds f
    x = initial_approximation
    f = eval(sequence)
    
    # finds f' 
    f_prime = custom_derivative(initial_approximation)
    
    approximation: float = f / f_prime
    while(abs(approximation) >= tolerance):
        # finds f
        x = initial_approximation
        f = eval(sequence)

        # finds f' 
        f_prime = custom_derivative(initial_approximation)

        # division operation
        approximation = f / f_prime

        # subtraction property
        initial_approximation -= approximation
        iteration_counter += 1
        
        
    return (iteration_counter)    


#---------------------------------------------------------------------------------------
def Double_Precision(binary_Number):
    
    sign = binary_Number[0]
    
    if sign==0:
        sign=1
    else:
        sign=-1
        
    exponent=binary_Number[1:12]
    mantissa=binary_Number[12:]
    
    mant_Val=mantissa_Value(mantissa)
    exp_Val=exponent_Value(exponent)
       
  
    return sign*( 2**exp_Val )*mant_Val
    
def exponent_Value(binary_Number):
    number: int=0
    binary_Number=np.flip(binary_Number)
    for i,j in enumerate(binary_Number):
            #print(i,j)
            number+=(2**i)*j       
    return number-1023

def mantissa_Value(mantissa_number):
    number: int=0
    for i,j in enumerate(mantissa_number):
            if(j!=0):
                number+= (1*(1/2)**(i+1))                   
    return 1+number


def Chopped_Rounding(number,cutOff):

    numLength=len(str(number).replace('.',''))
    number*=(10**numLength)
    numlist=[int(x) for x in str(int(number))]
    newNum=0
    
    for i,num in enumerate(numlist):
        newNum+=(num*(10**(numLength-i)))
        if i==(cutOff-1):
            return newNum/(10**(numLength-i))
    return number



def find_minimum_number(function: str,tolerance: float):
    
    max=1000
    for n in range(max):
        if eval(function)<=(tolerance):
            return(n)        
    return n

if __name__ == "__main__":
    
    import numpy as np

    #Q1    
    binary_Number = np.array([0  ,1,0,0,0,0,0,0,0,1,1,1  ,1,1,1,0,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    doublePrecisionNumber=Double_Precision(binary_Number)
    print(doublePrecisionNumber,"\n")
    
    
    #Q2
    #       Q2 part a
    chopped=Chopped_Rounding(doublePrecisionNumber,3)
    print(chopped,"\n")
    
    #       Q2 part b      
    round=doublePrecisionNumber+0.5
    rounding=Chopped_Rounding(round,3)
    print(rounding,"\n")
    
    
    
    #Q3
    #       Q3 part a
    print(absolute_error(doublePrecisionNumber, rounding),"\n")
    #       Q3 part b
    print(relative_error(doublePrecisionNumber, rounding),"\n")
    
    
    
    #Q4
    function_a: str = "(-1**k) * (x**k) / (k**3)"
    
    x: int = 1
    check1: bool = check_for_alternating(function_a)
    check2: bool = check_for_decreasing(function_a,x)
    
    if(check1 and check2):
        function_for_n: str = "(1)/((n+1)**3)"
        print(find_minimum_number(function_for_n,(10**-4)),"\n") 

       
       
    #Q6     
    initial_approximation: float = -4
    tolerance: float = .0001

    left = -4
    right = 7
    function_string = "x**3 +(4*(x**2))-10"   
    
    #Q6 part a
    print(bisection_method(left, right, function_string,tolerance),"\n")
    
    #Q6 part b
    print(newton_raphson(initial_approximation, tolerance, function_string))
    