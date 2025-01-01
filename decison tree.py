import math

def entropy(data):
    class_counts = {}
    for row in data:
        label = row[-1]
        if label not in class_counts:
            class_counts[label] = 0
        class_counts[label] += 1
    
    total = len(data)
    entropy_value = 0
    for label in class_counts:
        prob = class_counts[label] / total
        entropy_value -= prob * math.log2(prob)
    
    return entropy_value

def information_gain(data, feature_index):
    feature_values = set(row[feature_index] for row in data)
    total_entropy = entropy(data)
    
    weighted_entropy = 0
    for value in feature_values:
        subset = [row for row in data if row[feature_index] == value]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)
    
    return total_entropy - weighted_entropy

def best_split(data):
    best_feature = None
    best_gain = -float('inf')
    
    for feature_index in range(len(data[0]) - 1):
        gain = information_gain(data, feature_index)
        if gain > best_gain:
            best_gain = gain
            best_feature = feature_index
    
    return best_feature

def build_tree(data, features):
    labels = [row[-1] for row in data]
    if len(set(labels)) == 1:
        return labels[0]
    
    if len(features) == 0:
        return max(set(labels), key=labels.count)
    
    best_feature_index = best_split(data)
    best_feature = features[best_feature_index]
    
    tree = {best_feature: {}}
    
    feature_values = set(row[best_feature_index] for row in data)
    for value in feature_values:
        subset = [row for row in data if row[best_feature_index] == value]
        new_features = features[:best_feature_index] + features[best_feature_index + 1:]
        tree[best_feature][value] = build_tree(subset, new_features)
    
    return tree

def classify(tree, instance):
    if not isinstance(tree, dict):
        return tree
    
    feature = list(tree.keys())[0]
    feature_value = instance[features.index(feature)]
    
    return classify(tree[feature].get(feature_value), instance)

data = [
    [True, False, 4, 'Mammal'],
    [True, False, 4, 'Mammal'],
    [False, True, 0, 'Fish'],
    [False, True, 0, 'Fish'],
    [True, False, 4, 'Mammal'],
    [False, False, 0, 'Reptile'],
    [False, False, 0, 'Reptile'],
    [True, False, 2, 'Mammal']
]

features = ['Has Fur', 'Can Swim', 'Legs']

tree = build_tree(data, features)

print("Decision Tree:")
print(tree)

new_instance = [True, False, 4]
result = classify(tree, new_instance)
print("\nClassified as:", result)
