

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

def recursionForHandV (orderNumber, total, lowerDiscount, upperDiscount, lowerOrderNumber, UpperOrderNumber, unitPrice):
    if orderNumber >= UpperOrderNumber:
        total = total + upperDiscount
        return recursionForA(orderNumber - UpperOrderNumber, total)
    elif orderNumber >= lowerOrderNumber:
        total = total + lowerDiscount
        return recursionForA(orderNumber - lowerOrderNumber, total)
    elif orderNumber < lowerOrderNumber:
        total = total + (orderNumber * unitPrice)
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
    extra_quantity_r = 0
    extra_quantity_n  = 0
    freeF = 0
    freeU = 0
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
        if item == "V":
            if orderDict[item] < 2:
                total = total + orderDict[item] * 50
            elif orderDict[item] >= 2:
                total = recursionForHandV(orderDict[item], total, 90, 130, 2, 3, 50)

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

        if item == "M":
            orderN = orderDict["N"]
            while orderN >= 3:
                if orderN >= 3:
                    orderN = orderN - 3
                    extra_quantity_n = extra_quantity_n + 1
            while extra_quantity_n > orderDict[item]:
                extra_quantity_n = extra_quantity_n - 1
            orderM = orderDict[item] - extra_quantity_n
            total = total + (orderM * 40)

        if item == "Q":
            orderR = orderDict["R"]
            while orderR >= 3:
                if orderR >= 3:
                    orderR = orderR - 3
                    extra_quantity_r = extra_quantity_r + 1
            while extra_quantity_r > orderDict[item]:
                extra_quantity_r = extra_quantity_r - 1
            orderQ = orderDict[item] - extra_quantity_r
            total = total + (orderQ * 50)

        if item == "K" or "P" or "Q":
            if item == "K":
                orderK = orderDict["K"]
                if orderDict["K"] < 2:
                    total = total + (orderDict["K"] * 80)
                elif orderDict["K"] >= 2:
                    total = recursionForKPQ(orderK, total, 2, 150, 80)
            if item == "P":
                orderP = orderDict["P"]
                if orderDict["P"] < 5:
                    total = total + (orderDict["P"] * 50)
                elif orderDict["P"] >= 5:
                    total = recursionForKPQ(orderP, total, 5, 200, 50)
            if item == "Q":
                orderQ = orderDict["Q"]
                if orderDict["Q"] < 3:
                    total = total + (orderDict["Q"] * 30)
                elif orderDict["Q"] >= 3:
                    total = recursionForKPQ(orderQ, total, 3, 80, 30)

        if item == "F":
            orderF = orderDict[item]
            if orderF <= 2:
                total = total + (orderF * 10)
            else:
                while orderF > 2:
                    orderF = orderF - 2
                    freeF = freeF + 1
                total = total + (orderDict[item] - freeF) * 10

        if item == "U":
            orderU = orderDict[item]
            if orderU <= 3:
                total = total + (orderU * 40)
            else:
                while orderU > 3:
                    orderU = orderU - 3
                    freeU = freeU + 1
                total = total + (orderDict[item] - freeU) * 40
        else:
            orderOther = orderDict[item]
            total = total + (orderOther * itemPriceDict[item])

    return total


def checkout(skus):
    finalPrice = -1
    if skus == "":
        return 0
    elif type(skus) == str and skus.isupper():
        finalPrice = totalValue(skus)

    return finalPrice




