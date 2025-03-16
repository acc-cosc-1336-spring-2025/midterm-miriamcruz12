def main():
    print("Celsius | Fahrenheit")
    print("___________________")

    for celsius in range(21): #Loop from 0 to 20 
        fahrenheit = get_fahrenheit(celsius)
        print(f"{celsius:^7} | {fahrenheit:^10.2f}")

if __name__ == "__main__": 
    main() 