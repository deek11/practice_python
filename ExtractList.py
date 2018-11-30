def main():
    numbers = raw_input("Enter list of numbers \n")
    input_list = list(map(int, numbers.split()))
    output_list = list()

    num = input("Enter the number \n")
    for n in input_list:
        if n < num:
            output_list.append(n)

    print output_list


if __name__ == '__main__':
    main()