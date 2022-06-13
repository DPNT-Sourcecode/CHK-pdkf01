

# noinspection PyUnusedLocal
# skus = unicode string
def totalValue(basket):
    total = 0
    orderDict = {"A":0, "B":0, "C":0, "D":0}
    for i in range(len(basket)):
        product = str(basket[i])
        orderDict[product] = orderDict.get(product) + 1
    for i

        # if basket[i] == "A" or "B" or "C" or "D":
        #     if basket[i] =="A":
        #         total+=50
        #     if basket[i] =="B":
        #         total+=30
        #     if basket[i] =="C":
        #         total+=20
        #     if basket[i] =="D":
        #         total+=15
        # elif basket[i] == "3" or "5":
        #     if basket[i] == 3



def checklite(skus):
    if skus == "A"









