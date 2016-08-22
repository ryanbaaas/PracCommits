def main():
    numbers = []
    user_input = 5

    for number in range(1, user_input + 1):
        value = int(input("Enter value for number {}:".format(number)))
        numbers.append(value)

    min_num = min(numbers)
    max_num = max(numbers)
    first_num = numbers[0]
    last_num = numbers[len(numbers) - 1]
    avg_num = sum(numbers) // len(numbers)

    print("The First number is: {}".format(first_num))
    print("The last number is: {}".format(last_num))
    print("The smallest number is: {}".format(min_num))
    print("The largest number is: {}".format(max_num))
    print("The average of the numbers is: {}".format(avg_num))



main()