number=int(input("Enter a number: "))
max_number,min_number,i,steps=number,number,1,0
while number >=i:
    if number%2==0 or number ==1:
        number = number /2
    else:
        number = (number*3)+1
    print(number)
    if number > max_number:
        max_number = number
    if number < min_number:
        min= number
    steps+=1


print(f" Max Value: {max_number}")
print(f" Min Value: {min_number}")
print(f" Total Steps: {steps}\n")
