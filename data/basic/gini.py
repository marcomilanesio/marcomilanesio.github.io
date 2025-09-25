import numpy as np

def gini_impurity(y):
    classes, counts = np.unique(y, return_counts=True)
    impurity = 1 - np.sum((counts / counts.sum()) ** 2)
    return impurity

def split_dataset(X, y, feature_index, threshold):
    left_mask = X[:, feature_index] <= threshold   # boolean mask over columns
    right_mask = ~left_mask   
    return X[left_mask], y[left_mask], X[right_mask], y[right_mask]

def best_split(X, y):
    num_rows, num_features = X.shape
    if num_rows <= 1:
        return None, None

    gini = 1.0  # best value found
    best_idx, best_thr = None, None
    all_ginis = [gini]   # cache for later plot
    for feature_index in range(num_features):
        thresholds = np.unique(X[:, feature_index])
        for thresh in thresholds:
            _, y_left, _, y_right = split_dataset(X, y, feature_index, thresh)  # don't care about features here
            if len(y_left) == 0 or len(y_right) == 0:
                continue  # we don't need empty splits

            current_gini = (len(y_left) / len(y)) * gini_impurity(y_left) + \
                (len(y_right) / len(y)) * gini_impurity(y_right)
            
            all_ginis.append(current_gini)
            
            if current_gini < gini:
                gini = current_gini
                best_idx = feature_index
                best_thr = thresh

    print('Best gini', gini)
    return best_idx, best_thr, all_ginis
