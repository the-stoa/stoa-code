def web_scrape():
    # some steps
    return "570"

def get_current_price():
    price_from_page = web_scrape()
    price = int(price_from_page)
    return price


def main():
    my_limit = 500
    current_price = get_current_price()
    print(current_price)

    if current_price < my_limit:
        print("Go visit amazon.co.uk to buy now!!")
    elif current_price == 550:
        print("The price is 550!")
    else:
        print("No luck, get rich bitch!")


if __name__ == "__main__":
    main()
