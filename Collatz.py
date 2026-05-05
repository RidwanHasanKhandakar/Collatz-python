def main():
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
            min_number = number
        steps+=1

    print(f" Max Value: {max_number}")
    print(f" Min Value: {min_number}")
    print(f" Total Steps: {steps}\n")

    print("[1] to try again")
    print("[0] EXIT")
    ch = input("")
    if ch == "1":
        main()
    else:
        print("###BYE###")

if __name__ == "__main__":
    main()