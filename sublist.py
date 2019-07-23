def check_lists(first_list, second_list):
    if first_list == second_list:
        print("EQUAL")
    else:
        value = second_list.find(first_list)
        if value > 0:
            print("SUBLIST")
