
from sklearn.neural_network import MLPClassifier

x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 1]

model = MLPClassifier(
    hidden_layer_sizes=(4,),
    max_iter=5000,
    random_state=1
)

model.fit(x, y)

a = int(input("Enter first value (0 or 1): "))
b = int(input("Enter second value (0 or 1): "))

print("Output:", model.predict([[a, b]])[0])
