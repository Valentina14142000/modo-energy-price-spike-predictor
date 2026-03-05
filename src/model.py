import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

df = pd.read_csv("data/ercot_data.csv")

# define spike
spike_threshold = df['price'].quantile(0.95)

df['price_spike'] = df['price'] > spike_threshold

X = df[['demand']]
y = df['price_spike']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(classification_report(y_test, predictions))