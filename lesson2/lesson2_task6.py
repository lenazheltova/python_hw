goods = []
while input('do you want to add another product, enter yes/no: ') == 'yes':
    number = int(input('enter product number: '))
    features = {}
    while input('do you want to add a parameter of the product, e.g. name, price, enter yes/no: ') == 'yes':
        feature_key = input('enter parameter: ')
        feature_value = input('enter parameter value: ')
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)