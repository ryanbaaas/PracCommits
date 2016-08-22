def main():
    numbers = []
    user_input = 5

    for number in range(1, user_input + 1):
        value = int(input("Enter value for number {}:".format(number)))
        numbers.append(value)

    min_num = min(numbers)

    print("The smallest number is: {}".format(min_num))


main()