

string_length = len("Hello World")
list_length = len([1,2,3,4,5,6,7,8])
tuple_length = len((10,20,30))

print(string_length)
print(list_length)
print(tuple_length)
sum_of_list = sum([2,3,4,5,6])
sum_of_tuple = sum((1,2,34,6,))

print(sum_of_list)
print(sum_of_tuple)

max_value = max(5,15,2903)
max_float = max(1.23,9099,12.45)
print(max_value)
print(max_float)


def add(x,y):
    return x+y

def concentrate(x,y):
    return str(x) +str(y)

def operate(operation, x, y):
    return operation(x,y)
result_sum = operate(add,5,6)
result_concetrate=operate(concentrate,"hi","hello")
print(result_sum)
print(result_concetrate)