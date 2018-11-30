import datetime


def main():
    name = raw_input("Hello! Please enter your full name. \n")
    age = input("Please enter your age. \n")
    year = find_year(age)
    print('{0}, you will turn 100 years old in {1}'.format(name,year))


def find_year(age):
    year = datetime.datetime.now().year + (100 - age)
    return year

if __name__ == '__main__':
    main()