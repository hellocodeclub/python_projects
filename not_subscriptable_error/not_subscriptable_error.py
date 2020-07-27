var_integer = 1
var_list = [3,5]

print(var_list[0])
#print(var_integer[0])  << Error

var_float = 1.0
var_list = [3,5]

print(var_list[0])
#print(var_float[0])


### Lucky number

birthday = '04/08/1984'
sum_month_digits = (int(birthday[0])+int(birthday[1]))
sum_day_digits = (int(birthday[3])+int(birthday[4]))
sum_year_digits= (int(birthday[6])+int(birthday[7])+int(birthday[8])+int(birthday[9]))
sum_all = sum_month_digits + sum_day_digits + sum_year_digits
lucky_number= (int(str(sum_all)[0])+int(str(sum_all)[1]))
print("Your lucky number is", lucky_number)

var_string='Hello'
print(var_string[0])