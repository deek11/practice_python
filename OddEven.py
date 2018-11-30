def find_odd_even(num):
    if num % 2 == 0:
        return True
    return False


def main():
    num = input("Enter number : ")
    if find_odd_even(num):
        print "{0} is even".format(num)
    else:
        print "{0} is odd".format(num)


if __name__ == '__main__':
    main()