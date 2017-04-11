
"""
Run python autograder.py 
"""

def average(priceList):
    "Return the average price of a set of fruit"
    result = 0.0;

    priceList.sort();

    for price in priceList:
    	if priceList.count(price)>1:
    		priceList.remove(price);


    for price in priceList:
    	result += price;


    result = result / len(priceList);
    return result;
