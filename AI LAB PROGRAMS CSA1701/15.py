from sklearn.tree import DecisionTreeClassifier
x = [[1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1]
model = DecisionTreeClassifier()
model.fit(x, y)
n = int(input("Enter a number: "))
result = model.predict([[n]])
if result[0] == 1:
    print("Yes")
else:
    print("No")
