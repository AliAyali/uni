def calculate_ticket_price(age, day_of_week):
    base_price = 100000
    
    if age < 7:
        price = 0
    elif age < 18:
        price = base_price * 0.5
    elif age >= 65:
        price = base_price * 0.6
    else:
        price = base_price

    if day_of_week.lower() in ["tuesday", "سه شنبه"]:
        price = price * 0.8

    return int(price)

if __name__ == "__main__":
    age_input = 20
    day_input = "Tuesday"
    
    final_price = calculate_ticket_price(age_input, day_input)
    print(f"سن: {age_input} سال | روز: {day_input}")
    print(f"قیمت نهایی بلیت: {final_price:,} تومان")