from statistics import mean

def user_input(n):
    input_user = input("Enter numbers: ")

    if not input_user:
        print("You have not entered any number!")
        return None

    try:
        n = [float(number) for number in input_user.split()]

        return n
    except:
        print("Enter numbers separated by spaces!")

def main():
    x = []
    y = user_input(x)

    if y is not None:
        z = mean(y)
        print("Result:", z)



main()