def pow(base, exp):
    if exp == 0:
        return 1
    else :
        return base * pow(base, exp - 1)
    

def main():
    base = int(input("Enter the base:"))
    exp  = int(input("Enter exponent:"))
    result = pow(base, exp)
    print(f"{base} raised to the power of {exp} is {result}")   

main()