import cashregister

#Unit Testing

def test_makeChange():
	assert cashregister.makeChange(17.83, 20) == 2.17

def test_applyTax_noArgument():
	assert cashregister.applyTax(56.47) == 63.81

def test_applyTax_oneArgument():
	assert cashregister.applyTax(13.86, 0.17) == 16.22

def test_applyDiscount():
	assert cashregister.applyDiscount(17.49, 0.15) == 14.87

def test_cashAmount_roundUp():
	assert cashregister.cashAmount(12.47) == 12.45

def test_cashAmount_roundDown():
	assert cashregister.cashAmount(12.43) == 12.45

def test_cashAmount_noAlteration():
	assert cashregister.cashAmount(12.45) == 12.45

#Integration Testing

def test_cashAmountOfChange():
	assert cashregister.makeChange(cashregister.cashAmount(12.27),20) == 7.75

def test_taxAndDiscount():
	assert cashregister.applyTax(cashregister.applyDiscount(23.16, 0.1), 0.1) == 22.93

def test_allAtOnce():
	assert cashregister.makeChange(cashregister.cashAmount(cashregister.applyTax(cashregister.applyDiscount(24.49, 0.15))), 25)