# IMPORTS REQUIRED PACKAGES
import numpy as np
from sklearn import datasets
import pandas as pd
from heapq import nsmallest
import matplotlib.pyplot as plt
import seaborn as sns


# LOADS & VIEWS THE DATA
iris = datasets.load_iris()
iris_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])
iris_df
iris_df.groupby('target').count()

plt.figure()
plt.scatter(iris_df['sepal length (cm)'], iris_df['sepal width (cm)'], c=iris_df['target'])
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xticks(())
plt.yticks(())
plt.show()

plt.figure()
plt.scatter(iris_df['petal length (cm)'], iris_df['petal width (cm)'], c=iris_df['target'])
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.xticks(())
plt.yticks(())
plt.show()

iris_df["target"] = iris_df["target"].astype('category')
sns.scatterplot(iris_df['sepal length (cm)'], iris_df['sepal width (cm)'], hue=iris_df['target'])
plt.show()
sns.scatterplot(iris_df['petal length (cm)'], iris_df['petal width (cm)'], hue=iris_df['target'])
plt.show()
# all set!

#quick fix
iris_df["target"] = iris_df["target"].astype('int_')

# DEFINES KNN FUNCTIONS
def sarahs_dist_formula(rec1, rec2):
    diff = rec1 - rec2
    squared = diff**2
    summed = sum(squared)
    return np.sqrt(summed)

# testing
sarahs_dist_formula(iris_df.iloc[1,:4], iris_df.iloc[1,:4])

def sarahs_dist_dict(predictors):
    dist_dict = {}
    for record in predictors.index:
        dist_dict[record] = {}
    for record1 in predictors.index:
        for record2 in predictors[record1+1:].index:
            if record1 == record2:
                dist_dict[record1][record2] = 0
            else:
                dist = sarahs_dist_formula(predictors.iloc[record1], predictors.iloc[record2])
                dist_dict[record1][record2] = dist
                dist_dict[record2][record1] = dist
    return dist_dict

# testing
sarahs_dist_dict(iris_df.iloc[:,:4])

def sarahs_knn_single_prediction_v1(records_dict, target, k):
    indeces = nsmallest(k, records_dict, key = records_dict.get)
    class_counts = target[indeces].value_counts()
    if len(class_counts[class_counts==class_counts.max()]) > 1:
        new_guess = sarahs_knn_single_prediction_v1(records_dict, target, k+1) #ooo recursion!
        return new_guess
    else:
        return class_counts.idxmax()

def sarahs_knn_single_prediction_v2(records_dict, target, k):
    indeces = nsmallest(k, records_dict, key = records_dict.get)
    class_counts = target[indeces].value_counts()
    if len(class_counts[class_counts==class_counts.max()]) > 1:
        val_class_count = class_counts[class_counts==class_counts.max()]
        filtered_targs = target[indeces][target[indeces].isin(list(val_class_count.index))]
        filtered_indeces = list(filtered_targs.index)
        dists = {ind:records_dict[ind] for ind in filtered_indeces}
        dists = pd.DataFrame.from_dict(dists, orient='index', columns = ['dist_value'])
        tot = dists.join(target[indeces])
        tot_summed = tot.groupby('target').sum()
        tot_summed_min_dist = min(tot_summed['dist_value'])
        new_guess = tot_summed[tot_summed['dist_value'] == tot_summed_min_dist].index[0]
        return new_guess
    else:
        return class_counts.idxmax()

target = iris_df.loc[:, 'target']
k = 4
i = 133
records_dict = dist_dict[i]

# testing
sarahs_knn_single_prediction_v1(records_dict, target, k)
sarahs_knn_single_prediction_v2(records_dict, target, k)

def sarahs_knn_v1(predictors, outcome, k):
    dist_dict = sarahs_dist_dict(predictors)
    predictions = []
    for record in dist_dict.keys():
        predictions.append(sarahs_knn_single_prediction_v1(dist_dict[record], outcome, k))
    return predictions

def sarahs_knn_v2(predictors, outcome, k):
    dist_dict = sarahs_dist_dict(predictors)
    predictions = []
    for record in dist_dict.keys():
        predictions.append(sarahs_knn_single_prediction_v2(dist_dict[record], outcome, k))
    return predictions

# testing
v1_results = sarahs_knn_v1(iris_df.iloc[:,:4], iris_df['target'], 4)
v2_results = sarahs_knn_v2(iris_df.iloc[:,:4], iris_df['target'], 4)

# RESULTS CAPTURE
for k_val in range(1,101):
    v1_string = 'v1_' + 'k_is_' + str(k_val)
    v2_string = 'v2_' + 'k_is_' + str(k_val)
    iris_df[v1_string] = sarahs_knn_v1(iris_df.iloc[:,:4], iris_df['target'], k_val)
    iris_df[v2_string] = sarahs_knn_v2(iris_df.iloc[:,:4], iris_df['target'], k_val)

iris_df

for k_val in range(1,101):
    v1_string = 'v1_' + 'k_is_' + str(k_val)
    v2_string = 'v2_' + 'k_is_' + str(k_val)
    iris_df[v1_string] = iris_df[v1_string] == iris_df['target']
    iris_df[v2_string] = iris_df[v2_string] == iris_df['target']

iris_df

df_len = len(iris_df)
results_dict = {}
for k_val in range(1,101):
    v1_string = 'v1_' + 'k_is_' + str(k_val)
    v2_string = 'v2_' + 'k_is_' + str(k_val)
    results_dict[k_val] = [k_val, sum(iris_df[v1_string])/df_len, sum(iris_df[v2_string])/df_len]

results_dict

results_df = pd.DataFrame.from_dict(results_dict, orient='index', columns=['k_value', 'V1','V2'])

# RESULTS ANALYSIS
results_melted = pd.melt(results_df, id_vars='k_value', var_name="Version", value_vars=['V1','V2'], value_name="Accuracy")

sns.set(style="darkgrid")
sns.lineplot(x='k_value', y='Accuracy', hue = 'Version', data = results_melted)
plt.show()

sns.set(style="darkgrid")
sns.lineplot(x='k_value', y='Accuracy', hue = 'Version', data = results_melted[results_melted['k_value']<=90])
plt.show()

sns.set(style="darkgrid")
sns.lineplot(x='k_value', y='Accuracy', hue = 'Version', data = results_melted[results_melted['k_value']<=40])
plt.show()

sns.set(style="darkgrid")
sns.lineplot(x='k_value', y='Accuracy', hue = 'Version', data = results_melted[(results_melted['k_value']>=15) & (results_melted['k_value']<=25)])
plt.show()


iris_df["target"] = iris_df["target"].astype('category')
best_v_and_k = 'v1_' + 'k_is_' + str(19)
sns.scatterplot(data=iris_df, x='sepal length (cm)', y='sepal width (cm)', hue=best_v_and_k, style='target')
plt.show()
sns.scatterplot(data=iris_df, x='petal length (cm)', y='petal width (cm)', hue=best_v_and_k, style='target')
plt.show()
# all set!
