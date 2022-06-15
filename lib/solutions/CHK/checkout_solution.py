

# noinspection PyUnusedLocal
# skus = unicode string
import string
def recursionForB(orderNumber, total):
    if orderNumber >= 2:
        total = total + 45
        return recursionForB(orderNumber-2, total)
    elif orderNumber < 2:
        total = total + (orderNumber * 30)
        return total

def recursionForKPQ(orderNumber, total, quantity, bulkAmount, unitAmount):
    if orderNumber >= quantity:
        total = total + bulkAmount
        return recursionForKPQ(orderNumber - quantity, total, quantity, bulkAmount, unitAmount)
    elif orderNumber < quantity:
        total = total + (orderNumber * unitAmount)
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

def recursionForH (orderNumber, total):
    if orderNumber >= 10:
        total = total + 80
        return recursionForA(orderNumber - 10, total)
    elif orderNumber >= 5:
        total = total + 45
        return recursionForA(orderNumber - 5, total)
    elif orderNumber < 5:
        total = total + (orderNumber * 10)
        return total




def totalValue(basket):
    total = 0
    orderDict = {}
    alphabets = list(string.ascii_uppercase)
    for alphabet in alphabets:
        orderDict[alphabet] = 0
    # orderDict = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
    itemPriceDict = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35, 'J': 60,
                     'K': 80, 'L': 90,
                     'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 30, 'T': 20, 'U': 40,
                     'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50}
    for i in range(len(basket)):
        product = str(basket[i])
        orderDict[product] = orderDict.get(product) + 1

    extra_quantity_b = 0
    freeF = 0
    for item in orderDict:
        # item = item.upper()

        if item == "E":
            total = total + orderDict[item] * 40




        if item == "C" or "G":
            total = total + orderDict[item] * 20
        if item == "D":
            total = total + orderDict[item] * 15

        if item == "A":
            if orderDict[item] < 3:
                total = total + orderDict[item] * 50
            elif orderDict[item] >= 3:
                total = recursionForA(orderDict[item], total)

        if item == "H":
            if orderDict[item] < 5:
                total = total + orderDict[item] * 10
            elif orderDict[item] >= 5:
                total = recursionForH(orderDict[item], total)

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
        if item == "K" or "P" or "Q":
            if item == "K":
                

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

