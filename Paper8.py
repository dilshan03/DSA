def sum(n):
    if n == 1:
        return 1
    else:
        return (sum (n - 1) + n )


def main():
    while(True):
        try:
            n = int(input("Enter integer or press -1 to stop :"))
            if n == -1:
                print("program ended")
                break

            elif n<-1:
                 print("Number should be a positve integer")
                
                   

            else:
                result = sum(n)
                print(f"output = {result}")


        except ValueError:
            print("Error")


main()
