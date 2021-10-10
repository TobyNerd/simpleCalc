def calculate_division():
    first_value = int(input("Specify y: "))
    second_value = int(input("Specify x: "))
    divided_value = first_value / second_value
    if type(divided_value) != int:
        print(f"Dividing {first_value} with {second_value} equals: {divided_value} (Rounded: {round(divided_value)})")
    else:
        print(f"Dividing {first_value} with {second_value} equals: {divided_value}")
