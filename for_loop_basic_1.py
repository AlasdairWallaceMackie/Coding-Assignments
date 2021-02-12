# for i in range(150+1):
#     print( i )

# for i in range(5,1000+1,5):
#     print( i )


# for i in range(100+1):
#     string = ""
#     if i % 5 == 0:
#         string+="Coding"
#     if i % 10 == 0:
#         string+="Dojo"
#     if i%10!=0 and i%5!=0:
#         string = i
#     print( string )

# sum = 0
# for i in range(500000 + 1):
#     if i%2 != 0:
#         sum+=i
# print(f"The sum is: {sum}")

# for i in range (2018, 0, -4):
#     print(i)

low_num = 2
high_num = 9
mult = 3
for i in range (low_num, high_num+1, 1):
    if i%mult == 0:
        print(i)