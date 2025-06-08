from allll import RegressionPredictor

x = [1, 2, 3, 4, 5, 6, 7]
y = [33, 44, 53, 78, 99, 0, 20]
wickets = [4, 5, 2, 7, 4, 11, 0]
predictor = RegressionPredictor(x, y, wickets)
print(predictor)
predictor.plot("Virat Runs", "Runs Scored by Virat", "Match Number", "Runs Scored")
predictor.plotX("Virat Wickets", "Wickets by Virat", "Match Number", "Taken Wickets")