
def verify_credit_card(card_number):
    # Drop the last digit from the number
    last_digit = int(card_number[-1])
    result_step1 = card_number[:-1]

    # Reverse the numbers
    result_step2 = result_step1[::-1]

    # Multiply the digits in odd positions (1, 3, 5, etc.) by 2
    # And subtract 9 to all any result higher than 9
    result_step3 = ''
    for digit in result_step2:
        doubled_digit = int(digit)*2
        if(doubled_digit > 9):
            doubled_digit = doubled_digit-9
        result_step3 = result_step3 + str(doubled_digit)

    # Add all the numbers together
    result_step4 =0
    for digit in result_step3:
        result_step4 = result_step4 + int(digit)

    # Check if the result of module 10 is equal to the last digit,
    # if so, the card number is a valid number
    final_result = result_step4 % 10
    return final_result==last_digit

is_card1_valid = verify_credit_card('4539797671535063') # Invalid number
is_card2_valid = verify_credit_card('4929817131531581') # Valid number
print(is_card1_valid)
print(is_card2_valid)

##### Another example 1

def function():
    variable1 = 2
    variable2 = variable1*3
    return 4

result = function()
print(result)

##### Another example 2

def function2(parameter1):
    if parameter1>5:
        return 1
    return 2

variable1 = function2(6)
variable2 = function2(3)
print(variable1)
print(variable2)

#### return multiple values python

def function3():
    var1 = 'value1'
    var2 = 'value2'
    var3 = 'value3'
    return var1, var2, var3

v1, v2, v3 = function3()
print(v1)
print(v2)
print(v3)

#### return two values python

def function_two_values():
    var1 = 'value1'
    var2 = 'value2'
    return var1, var2

value1, value2 = function_two_values()



#### return list python

def function4():
    list = [1,2,3,4]
    return list

result = function4()
print(result)
print(type(result))

#### return vs print

def display_sum(num1,num2):
    total_sum = num1 + num2
    print(total_sum)

result = display_sum(2,2)
print(result)

def display_sum2(num1,num2):
    total_sum = num1 + num2
    print(total_sum)
    return total_sum

result = display_sum2(2,2)
print(result)

