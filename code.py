import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

df=pd.read_csv(r"C:\Users\nbkba\Desktop\tpt project\final_data.csv")
print(df.head())

print(df.info())

df['date']=pd.to_datetime(df['date'])
df=df.sort_values('date')
df=df.drop_duplicates()
print(df.isnull().sum())
print(df.head())
print(df.info())

X=df[['weekend','is_festival','is_brahmostavam','rolling_avg_7','google_trend_score']]
y=df['darshans']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,shuffle=False)
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("R2 Score:",r2_score(y_test,y_pred))
print("MAE:",mean_absolute_error(y_test,y_pred))

#visualizations
print("lineplot")
plt.figure(figsize=(10,5))
sns.lineplot(x=range(len(y_test)),y=y_test.values,label="Actual")
sns.lineplot(x=range(len(y_pred)),y=y_pred,label="Predicted")
plt.title("Actual vs Predicted Pilgrim Count")
plt.xlabel("Days")
plt.ylabel("Pilgrims")
plt.legend()
plt.show()

print("barplot")
df['festival_label']=df['is_festival'].map({0:'Normal Day',1:'Festival Day'})
plt.figure(figsize=(8,4))
sns.barplot(x='festival_label',y='darshans',data=df,width=0.4)
plt.title("Festival vs Normal Days")
plt.xlabel("Day Type")
plt.ylabel("Average Pilgrims")
plt.show()

print("boxplot")
df['brahm_label']=df['is_brahmostavam'].map({0:'Non-Brahmotsavam',1:'Brahmotsavam'})
plt.figure(figsize=(8,4))
sns.boxplot(x='brahm_label',y='darshans',data=df)
plt.title("Distribution of Pilgrim Count during Brahmotsavam")
plt.xlabel("Event Type")
plt.ylabel("Pilgrim Count")
plt.show()

print("Scatterplot")
plt.figure(figsize=(8,4))
sns.scatterplot(x='rolling_avg_7',y='darshans',data=df)
plt.title("Rolling Average vs Pilgrim Count")
plt.xlabel("Rolling Avg (7 days)")
plt.ylabel("Pilgrims")
plt.show()

print("barchart")
data={'Category':['Festival','Weekend','Brahmotsavam','Normal'],
      'Avg':[df[df['is_festival']==1]['darshans'].mean(),
             df[df['weekend']==1]['darshans'].mean(),
             df[df['is_brahmostavam']==1]['darshans'].mean(),
             df[(df['is_festival']==0)&(df['weekend']==0)&(df['is_brahmostavam']==0)]['darshans'].mean()]}
new_df=pd.DataFrame(data)
colors=['red','blue','green','orange']
plt.bar(new_df['Category'],new_df['Avg'],width=0.4,color=colors)
plt.title("Average Pilgrim Count Comparison")
plt.xlabel("Category")
plt.ylabel("Pilgrims")
plt.show()


print("pairplot")
cols=['darshans','rolling_avg_7','google_trend_score']
sns.pairplot(df[cols])
plt.show()






























