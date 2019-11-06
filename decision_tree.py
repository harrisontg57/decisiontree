from sklearn import tree
import tree_features


clf = tree.DecisionTreeClassifier(random_state=0, max_depth=6)
features = ["buy", "sell", "us ", "uk ", " rip", "card", "bank", "transfer", "address", "paypal", "fullz", "money", "btc", "proof", "logs", "pm ", "dm "]
x, y = tree_features.get_array_from_file("tim.csv", features)
clf.fit(x[:1000], y[:1000])

chats = tree_features.load_sep("tim.csv")
correct = 0
incorrect = 0
for n in range(300):
    print(chats[1001 + n])
    pred = clf.predict([x[1001 + n]])
    print(pred)
    if chats[1001 + n][1] == "a":
        if pred == 1:
            correct += 1
        else:
            incorrect += 1
    else:
        if pred == 0:
            correct += 1
        else:
            incorrect += 1
    print(correct)

print(str(correct + incorrect) + " " + str(incorrect) + " " + str(100*correct/(correct+incorrect)) + "% Accurate")
