weight = int(input('weight: '))
unit = input('(K)g or (L)bs:')
if unit.upper() == "K":
    converted = weight * 0.45
    print(f'you are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'you are {converted} lbs')


#weight_lbs = int(weight_kgs) / 0.45

#print(weight, 'lbs')

