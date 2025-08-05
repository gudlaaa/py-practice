userscore = int (input('Give me age value: '))
day = input('Give me age value: ')

price = 0


# if userscore < 18:
#     price = 8
# else:
#     price = 12

price = 12 if userscore >= 18 else 8

if price > 0:
    if day == 'wednesday':
        price = price - 2

print(price)


 

