def arbitrary_function(queen):
    print(queen)

def multiply(a, b):
    print(a*b)

def say_hello(name):
    # this function will tell the person hello
    print("hello")
    print(name)

def really_stupid_function():
    print("stupid")

def main():
    current_price = int("570") # we get this from webpage

    my_limit = 500
    print(1 == 2)
    if current_price < my_limit:
        print("Go visit amazon.co.uk to buy now!!")
    elif current_price == 550:
        print("The price is 550!")
    else:
        print("No luck, get rich bitch!")


if __name__ == "__main__":
    main()
