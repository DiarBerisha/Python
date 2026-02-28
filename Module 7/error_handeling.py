# from csv import excel
#
# try:
#     result = 10/0
#
# except ZeroDivisionError:
#     print("Dont")
#
# fruits = {
#     "apple": 5,
#     "orange": 3,
#     "banana": 7
# }
# try:
#     print(fruits["cherry"])
#
# except KeyError:
#     print("The key does not match")
#
#
#
# text = 'this is not number'
#
# try:
#     text_to_int = int(text)
#
# except Exception as e:
#     print("An error ocurred", e)
#
#
#
# try:
#     result = 10/2
# except ZeroDivisionError:
#     print("Division by 0")
# else:
#     print("Division succsessful. Result = ", result)
#
#
# try:
#     result  = 10/0
#
# except ZeroDivisionError:
#     print("Error")
# finally:
#     print("Finally block executed")
#


def divide_numbers(a,b):
    try:
        result = a/b
        print("the result is: ",result)
    except ZeroDivisionError:
        print("You tried to divide by 0")
    except TypeError:
        print("invalid type for division")
    except Exception as e:
        print("Unexcpeted error", e)

divide_numbers(10, 2)