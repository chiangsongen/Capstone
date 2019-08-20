[![Python Versions][pyversion-button]][md-pypi]

[pyversion-button]: https://img.shields.io/pypi/pyversions/Markdown.svg
[md-pypi]: https://pypi.org/project/Markdown/

# Capstone Project - Credit Card Fraud Detection using Machine Learning
- For General Assembly, Data Science Immersive, Batch 8
- link to dataset: https://www.kaggle.com/wendykan/lending-club-loan-data

## Background
- Lending Club is a peer to peer lending company based in the United States, in which investors provide funds for potential borrowers and investors earn a profit depending on the risk they take (the borrowers credit score). 
- Lending Club provides the "bridge" between investors and borrowers. Similar to the likes of Uber or Grab between lenders and investors.

<img src="http://echeck.org/wp-content/uploads/2016/12/Showing-how-the-lending-club-works-and-makes-money-1.png"><br><br>


## Problem Statement
- Predicting loans transaction that would default in a highly unbalanced dataset

## Steps
1. ETL
2. EDA, Data cleaning, and Feature engineering
3. SMOTE and random under sampling
4. Modelling

## Write up
I decided to have a go at credit loan default prediction due to it being a very practical challenge that banking industry faces. Credit loan default prediction falls under the umbrella of highly imbalance dataset prediction, and its application are applicable to various industries, such as manufacturing, biomedical, finance, government, etc. 

The first problem of a highly imbalanced dataset was that a dumb classifier (predicting all majority) will already have a very high accuracy. In the case of this lending club dataset, a dumb classifier could give a 99.6%. Hence, maximising accuracy as a scoring metrix is increasing difficult, and may not be the best metrix in terms of reducing loss due to misclassification. 

Primarily maximising Recall, secondly f1 score would be the preferred matrix. Maximising recall would reduce type II error, decreasing false negative in our context would mean decrease the probability that model predicted a loan to be good when it was actually in default. Failure to predict a defaulted loan incurred large cost due to the loss of whole notional amount. Hence the priority to predict correctly a defaulted loan. However, we cannot totally sacrifice precision in this precision vs recall trade off. Precision of the model provides relavancy to real life. In order to balance both requirements, maximising f1 score would be taken into account as a secondary metrix.

The second problem of a highly imbalanced dataset was that machine learning algorithms have trouble learning when one class dominates the other. When one class dominates the other, all a machine learning algorithm sees is the domination of the majority class. The biased proportion in dataset caused to machine to largely predict the majority class, as it does not have enough minority class examples to learn from. 

SMOTE synthesises new minority instances between existing (real) minority instances, up to the number of majority class present. This balances out the minority and the majoirty class for machine learning. Ideally, SMOTE could be used solely, in our case, to synthetically bring minority number of 8.8k datapoints up to majority numbers of 2252k datapoints. Totalling to 4500k datapoints after SMOTE. However, due to system limitation, such as memory size and runtime, SMOTE plus random under sampling would make the processing the dataset to be within the limited resources.

After cleaning, SMOTE, and under sampling our dataset. the next step would be to perform machine learning. A gridsearchCV was used to grind through various models and hyper-parameters that could maximise Recall, then f1 score. XGBoost with GPU support was selected after extension gridsearchCV done.

Results were pretty satisfactory with minority recall score of 0.99 and f1 score of 0.92


