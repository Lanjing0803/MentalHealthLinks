import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import textwrap


# Gender and Year Stacked Bar Chart
data = pd.read_csv('Indicators_of_Anxiety_or_Depression_Based_on_Reported_Frequency_of_Symptoms_During_Last_7_Days_20240206.csv')
df = data.dropna(subset=['Value'])
filtered_data = df[df['Subgroup'].isin(['Male', 'Female'])]
filtered_data['Time Period End Date'] = pd.to_datetime(filtered_data['Time Period End Date'])

filtered_data['Year'] = filtered_data['Time Period End Date'].dt.year

grouped_data = filtered_data.groupby(['Subgroup','Year' ])['Value'].mean().unstack()


plt.figure(figsize=(12, 8))
grouped_data.plot(kind='bar', stacked=True,colormap='cividis')

plt.title('Symptom Frequency by Gender and Year', fontsize=18, fontname='Times New Roman', y=1.02)
plt.xlabel('Time Period End Date', fontname='Times New Roman')
plt.ylabel('Total Symptom Frequency', fontname='Times New Roman')
plt.xticks(rotation=0, fontname='Times New Roman')
plt.yticks(fontname='Times New Roman')
plt.savefig('Symptom_Frequency_by_Gender_and_Year.png', transparent=True, dpi=300, bbox_inches='tight')
plt.tight_layout()

plt.show()


# Distribution of Symptom Frequencies by Gender
male_data = df[df['Subgroup'] == 'Male']['Value']
female_data = df[df['Subgroup'] == 'Female']['Value']


t_statistic, p_value = stats.ttest_ind(male_data, female_data)

print("t-statistic:", t_statistic)
print("p-value:", p_value)

if p_value < 0.05:
    print("The difference in symptom frequencies between males and females is statistically significant.")
else:
    print("There is no significant difference in symptom frequencies between males and females.")


plt.figure(figsize=(10, 6))
sns.kdeplot(male_data, color='#00204C', label='Male', linewidth=2)

sns.kdeplot(female_data, color='#E0D400', label='Female', linewidth=2, linestyle='--')

plt.xlabel('Anxiety or Depression Symptoms', fontname='Times New Roman')
plt.ylabel('Frequency', fontname='Times New Roman')

plt.title('Distribution of Symptom Frequencies by Gender', fontsize=18, fontname='Times New Roman', y=1.02)  
plt.xticks(fontname='Times New Roman')  
plt.yticks(fontname='Times New Roman')
plt.legend()
plt.tight_layout()
plt.savefig('Distribution_of_Symptom_Frequencies_by_Gender.png', transparent=True)
plt.show()