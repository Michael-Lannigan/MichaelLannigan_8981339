def makeChange(price, given):
	if (given < price):
		raise ValueError("Cash tendered must be at least value of item(s).")
	else:
		return round((given - price), 2) 

def applyTax(price, tax = 0.13): #tax argument should be fraction of price added, e.g. 10% tax -> tax = 0.1; default is Ontario GST.
	return round((tax + 1)*price, 2)

def applyDiscount(price, discount): #discount argument should be fraction of price subtracted, e.g. 10% off -> discount = 0.1
	return round((1 - discount)*price, 2)

def cashAmount(price): #returns the price rounded to the nearest five cents, to be used for cash payment in Canada.
	return round(round(price/5, 2)*5, 2)
	