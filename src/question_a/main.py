#add import 
def main (): 
    kilometers = int(input("Enter the number of kilometers: "))
    minutes = int(input("Enter the number of minutes: "))

    result = get_miles_per_hour(kilometers, minutes) 

    if result == 'Invalid argument': 
        print(result)
    else:
        print(f"The speed is {result:.6f}miles per hour.") 

if __name__ == "__main__":
    main()