# names = ["erina", "blina,","uvejs", "diarBerishaBabamaimadhi"]
#
# for name in names:
#     print(name)
#
# sentence = "Hello World"
#
# for char in sentence:
#     if char.isalpha():
#         print(char)
#
# for number in range(1,19):
#     print(number)
#
# numbers = [12,20,33,58,80]
# maximum = numbers[0]
#
# for number in numbers:
#     if number > maximum:
#         maximum = number
#
# print("the max was:", maximum)


count = 1

while count<=5:
    print("the number is ", count)
    count+=1

#break
numbers=[1,2,3,4,5,6,7,8]
target =4

for number in numbers:
    if number == target:
        print("target found")
        break

#continue
scores = [65,6,5,44,33,44,345,88]
total =0
count = 0
mesatarja =0
for score in scores:
    if score >50:
        total += score
        count+=1
        continue
mesatarja = total/count if count>0 else 0
print(mesatarja)

#do while

while True:
    user_input = input("enter a positive number: ")
    if user_input.isnumeric():
        number = int(user_input)

        if number>0:
            break
    print("input invalid > try again")
print("positiv", number)


numbers = [1,2,3,4,5,6,7,8,9,10]
total = 0
for number in range(1,11):
    if number%2==0:
        total+=number
print(total)


















