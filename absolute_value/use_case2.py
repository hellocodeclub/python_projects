def is_smartphone_faulty(average_temp, temp_last_ten_hours):
    for temp in temp_last_ten_hours:
        absolute_difference = abs(average_temp - temp)
        if absolute_difference > 10 :
            return True

    return False

smartphone1_faulty = is_smartphone_faulty(15.5, [12.5, 16, 20.5, 13.5, 12.5, 5.5, 3.4, 13.5, 13.9, 14.6])
print(smartphone1_faulty)

smartphone2_faulty = is_smartphone_faulty(15.5, [12.5, 16, 25.5, 13.5, 12.5, 15.5, 13.4, 13.5, 13.9, 14.6])
print(smartphone2_faulty)

