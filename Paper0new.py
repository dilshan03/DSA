def Triangular(n) :
    if n == 1 :
        return 1
    else :
        return n + Triangular(n - 1)
    


def main ():
    while True:
        try:
            num = int(input("Enter integer or enter -1 to finish"))
            if num == -1:
                print("Finished")
                break

            elif num < 0:
                print("enter a positive integer ")

            else:
                result = Triangular(num)    
                print(f"Output = {result}")

        except ValueError:
            print("error compiling")        



main()
