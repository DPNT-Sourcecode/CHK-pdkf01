

# noinspection PyUnusedLocal
# skus = unicode string
def totalValue(basket):
    total = 0
    orderDict = {"A":0, "B":0, "C":0, "D":0}
    for i in range(len(basket)):
        product = str(basket[i])
        orderDict[product] = orderDict.get(product) + 1

    for item in orderDict:
        if item == "C":
            total = total + orderDict[item] * 20
        if item == "D":
            total = total + orderDict[item] * 15
        if item == "A":
            if orderDict[item] < 3:
                total = total + orderDict[item] * 50
            elif orderDict[item] >= 3:
                orderDict[item] = orderDict[item] - 3
                total = total + 130
                total = total + (orderDict[item] * 50)
        if item == "B":
            if orderDict[item] < 2:
                total = total + (orderDict[item] * 50)
            elif orderDict[item] >= 2:
                orderDict[item] = orderDict[item] - 2
                total = total + 130
                total = total + (orderDict[item] * 30)
    return total

def checkout(skus):

    if type(skus) == str:
        finalPrice = totalValue(skus)
    elif type(skus) != str:
        finalPrice = -1
    return finalPrice



