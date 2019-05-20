#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for i in range(list_length):
        try:
            newlist.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by zero")
            newlist.append(0)
        except (ValueError, TypeError):
            print("wrong type")
            newlist.append(0)
        except IndexError:
            print("out of range")
            newlist.append(0)
        finally:
            pass
    return newlist
