

# noinspection PyUnusedLocal
# skus = unicode string

def recursionForB(orderNumber, total):
    if orderNumber >= 2:
        total = total + 45
        return recursionForB(orderNumber-2, total)
    elif orderNumber < 2:
        total = total + (orderNumber * 30)
        return total

def recursionForA(orderNumber, total):
    if orderNumber >= 5:
        total = total + 200
        return recursionForA(orderNumber - 5, total)
    elif orderNumber >= 3:
        total = total + 130
        return recursionForA(orderNumber - 3, total)
    elif orderNumber < 3:
        total = total + (orderNumber * 50)
        return total

def recursionForE(orderNumber, extraNumberOfB):
    if orderNumber >= 2:
        extraNumberOfB = extraNumberOfB + 1
        return recursionForE (orderNumber - 2, extraNumberOfB )
    elif orderNumber < 2:
        return extraNumberOfB




def totalValue(basket):
    total = 0

    orderDict = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    for i in range(len(basket)):
        product = str(basket[i])
        orderDict[product] = orderDict.get(product) + 1


    for item in orderDict:
        # item = item.upper()
        if item == "E":
            total = total + orderDict[item] * 40
            quantity_b = 0
            extra_quantity_b = recursionForE(orderDict[item], quantity_b)
            # orderDict["E"] = orderDict.get("E") + extra_quantity_b
            # total = total + extra_quantity_b * 30


        if item == "C":
            total = total + orderDict[item] * 20
        if item == "D":
            total = total + orderDict[item] * 15
        if item == "A":
            if orderDict[item] < 3:
                total = total + orderDict[item] * 50
            elif orderDict[item] >= 3:
                total = recursionForA(orderDict[item], total)

        if item == "B":
            if orderDict[item] < 2:
                total = total + (orderDict[item] * 30)
            elif orderDict[item] >= 2:
                total = recursionForB(orderDict[item], total)


    return total


def checkout(skus):
    finalPrice = -1
    if skus == "":
        return 0
    elif type(skus) == str and skus.isupper():
        finalPrice = totalValue(skus)

    return finalPrice





