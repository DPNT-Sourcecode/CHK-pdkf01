

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

    orderDict = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
    for i in range(len(basket)):
        product = str(basket[i])
        orderDict[product] = orderDict.get(product) + 1

    extra_quantity_b = 0
    freeF = 0
    for item in orderDict:
        # item = item.upper()

        if item == "E":
            total = total + orderDict[item] * 40
            quantity_b = 0

            # extra_quantity_b = recursionForE(orderDict[item], quantity_b)
            # if orderDict.get("B") > 0:
            #     deduction = recursionForB(extra_quantity_b,0)
            #     total = total - deduction



        if item == "C" or "G":
            total = total + orderDict[item] * 20
        if item == "D":
            total = total + orderDict[item] * 15
        if item == "A":
            if orderDict[item] < 3:
                total = total + orderDict[item] * 50
            elif orderDict[item] >= 3:
                total = recursionForA(orderDict[item], total)

        if item == "B":
            orderE = orderDict["E"]
            while orderE >= 2:
                if orderE >= 2:
                    orderE = orderE - 2
                    extra_quantity_b = extra_quantity_b + 1
            while extra_quantity_b > orderDict[item]:
                extra_quantity_b = extra_quantity_b - 1
            orderB = orderDict[item] - extra_quantity_b
            if orderB < 2:
                total = total + (orderB * 30)
            elif orderB >= 2:
                total = recursionForB(orderB, total)

        if item == "F":
            orderF = orderDict[item]
            if orderF <= 2:
                total = total + (orderF * 10)
            else:
                while orderF > 2:
                    orderF = orderF - 2
                    freeF = freeF + 1
                total = total + (orderDict[item] - freeF) * 10



    return total


def checkout(skus):
    finalPrice = -1
    if skus == "":
        return 0
    elif type(skus) == str and skus.isupper():
        finalPrice = totalValue(skus)

    return finalPrice
