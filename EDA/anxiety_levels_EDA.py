import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv('Indicators_of_Anxiety_or_Depression_Based_on_Reported_Frequency_of_Symptoms_During_Last_7_Days_20240206.csv')  

relevant_columns = ["Subgroup","Value", "Low CI","High CI","Time Period End Date"]
data = data[relevant_columns]
data = data[data["Subgroup"].str.contains("years")]
data.dropna(inplace=True) 


# save the filtered version to the folder
data.to_csv('filtered_data.csv', index=False)


# VIZ #1

data['Timestamp'] = pd.to_datetime(data['Time Period End Date'])

data['Month'] = data['Timestamp'].dt.to_period('M')
monthly_mean_prevalence = data.groupby('Month')['Value'].mean()

plt.figure(figsize=(10, 6))
plt.plot(monthly_mean_prevalence.index.astype(str), monthly_mean_prevalence.values, marker='o', color='royalblue') 
plt.xlabel('Month', fontname='Times New Roman') 
plt.ylabel('Mean Symptom Prevalence', fontname='Times New Roman')
plt.title('Trend of Symptom Prevalence Over Time', fontsize=18, fontname='Times New Roman',y=1.02)  
plt.xticks( fontname='Times New Roman')  

labels = monthly_mean_prevalence.index.astype(str).tolist()
n = len(labels)
plt.xticks(range(0, n, n//6), labels[::n//6])

for month in range(n//6, n, n//6):
    plt.axvline(x=labels.index(labels[month]), color='gray', linestyle='--', linewidth=0.5)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Trend_of_Symptom_Prevalence_Over_Time.png', transparent=True)
plt.show()


# VIS #2

data['Timestamp'] = pd.to_datetime(data['Time Period End Date'])
data['Month'] = data['Timestamp'].dt.to_period('M')

# Create a pivot table to prepare the data for the heatmap
heatmap_data = data.pivot_table(index='Subgroup', columns='Month', values='Value', aggfunc='mean')

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='YlGnBu',  annot=False,fmt=".1f", linewidths=0.5)

plt.ylabel('Age Group')
plt.title('Symptom Prevalence Across Age Groups Over Time',fontsize=18, fontname='Times New Roman',y=1.02)
plt.xticks(fontname='Times New Roman')
plt.yticks(fontname='Times New Roman')
n = len(heatmap_data.columns)
plt.xticks(range(0, n, n//6), heatmap_data.columns[::n//6], rotation=45, ha='right')

plt.tight_layout()
plt.savefig('Symptom_Prevalence_Heat_Map.png', transparent=True)
plt.show()
