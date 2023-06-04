import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

heart_data = pd.read_csv("/home/christy/Documents/Myself/Academia/PG docs/Lab-assignments/2nd Sem/TFML/Heart.csv")

heart_data = heart_data.drop(columns='Unnamed: 0')

heart_data['ChestPain'] = heart_data['ChestPain'].astype('category')
heart_data['ChestPain'] = heart_data['ChestPain'].cat.codes

heart_data['Thal'] = heart_data['Thal'].astype('category')
heart_data['Thal'] = heart_data['Thal'].cat.codes

heart_data['AHD'] = heart_data['AHD'].astype('category')
heart_data['AHD'] = heart_data['AHD'].cat.codes

heart_data = heart_data.dropna()

x = heart_data.drop(columns='AHD')
y = heart_data['AHD']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.3, random_state= 23)

scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)

log_reg = LogisticRegression(random_state=0, C=1, fit_intercept=True)

log_reg.fit(x_train_scaled, y_train)

y_pred_train = log_reg.predict(x_train_scaled)

print(log_reg.score(x_train_scaled, y_train))
print(log_reg.score(x_test_scaled, y_test))
