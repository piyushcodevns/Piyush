from allll import RegressionPredictor

x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 18, 20]
predictor = RegressionPredictor(x, y, company_name="Apple Inc.")
print(predictor)
predictor.plot("Stock Price", "Stock Regression", "Days", "Price")