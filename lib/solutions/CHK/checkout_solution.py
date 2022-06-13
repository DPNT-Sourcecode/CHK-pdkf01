

# noinspection PyUnusedLocal
# skus = unicode string

def recursionForB(orderNumber, total):
    if orderNumber>= 2:

        total = total + 45
        return recursionForB(orderNumber-2)
    elif orderNumber < 2:
        total = total + (orderNumber * 30)
        return total


def totalValue(basket):
    total = 0

    orderDict = {"A":0, "B":0, "C":0, "D":0}
    for i in range(len(basket)):
        product = str(basket[i])
        orderDict[product] = orderDict.get(product) + 1

    for item in orderDict:
        # item = item.upper()
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
                total = total + (orderDict[item] * 30)
            elif orderDict[item] >= 2:
                recursionForB(orderDict[item], total)
                # orderDict[item] = orderDict[item] - 2
                # total = total + 45
                # total = total + (orderDict[item] * 30)
    return total


def checkout(skus):
    finalPrice = -1
    if type(skus) == str or skus == "" or skus.isupper():
        finalPrice = totalValue(skus)

    return finalPrice

