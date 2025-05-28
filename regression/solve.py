import fullregression as fq

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 4, 6]
reg = fq.regression(x, y)
print(reg)
reg.plotXX2("Mere plot ka title", "mere digram ka title", "X ka title", "Y ka title")
