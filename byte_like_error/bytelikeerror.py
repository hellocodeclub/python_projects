with open('file_sample.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

bike_available = False
for line in lines:
    tmp = line.strip().lower()
    split_line = tmp.split(';')
    if split_line[0]=='bike' and int(split_line[1])>0:
        bike_available = True

print("Bikes Available? "+ str(bike_available))

