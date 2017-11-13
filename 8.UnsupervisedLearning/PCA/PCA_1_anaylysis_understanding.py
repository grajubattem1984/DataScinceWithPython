import numpy as np
from sklearn import decomposition
import pandas as pd

df1= pd.DataFrame({
        'X1':[10,2,8,9,12],
        'X2':[20,5,17,20,22],
        'X3':[10,2,7,10,11]})
pca = decomposition.PCA(1)#Here input(3 features, 3 argument) output=3features
#input(3 features, 2 argument) output=2features
#input(3 features, 1 argument) output=1features
#input(3 features, 0 argument) output=0features
#find eigen values and eigen vectors of covariance matrix of df
pca.fit(df1)
#convert all the data points from standard basis to eigen vector basis
df1_pca = pca.transform(df1)

#variance of data along original axes
np.var(df1.X1) + np.var(df1.X2) + np.var(df1.X3)#total variance=59.52
#variance of data along principal component axes
#show eigen values of covariance matrix in decreasing order
np.sum(pca.explained_variance_)

#understand how much variance captured by each principal component
print(pca.explained_variance_)
print(pca.explained_variance_ratio_)#1st feature importance=99.08
print(pca.explained_variance_ratio_.cumsum())#99.08

#show the principal components
#show eighen vectors of covariance matrix of df
pca.components_[0]
pca.components_[1]
pca.components_[2]

#specify number of required dimensions as n_components
pca = decomposition.PCA(n_components=2)
pca.fit(df1)
pca.explained_variance_
pca.components_[0]
pca.components_[1]
df1_pca = pca.transform(df1)
