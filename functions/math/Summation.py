def calculate_summation():
    additional_value_number = int(input("Specify amount of values: "))
    additional_value_list = []
    additional_value_list_summed = 0
    while additional_value_number > 0:
        additional_value_list_input = int(input("input value: "))
        additional_value_list.append(additional_value_list_input)
        additional_value_number = additional_value_number - 1

    print(f"Values: {additional_value_list}")

    for i in additional_value_list:
        additional_value_list_summed = additional_value_list_summed + int(i)

    print(f"The sum of these values is : {additional_value_list_summed}")
