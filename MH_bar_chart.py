import pandas as pd
import matplotlib.pyplot as plt

# GET THE DATASET
data = pd.read_csv('MH_CLD.csv')
data.drop(columns=['CASEID'], inplace=True)


data = data[data['MH1'] != '-9']

combined_series = data['MH1'].astype(str) + ' ' + data['MH2'].astype(str) + ' ' + data['MH3'].astype(str)

issues = combined_series.str.split(expand=True).stack()


issues = issues[issues != '-9']


issue_counts = issues.value_counts()

# BAR CHART HERE
issue_mapping = {
    '1': 'Trauma- and stressor-related disorders',
    '2': 'Anxiety disorders',
    '3': 'ADHD',
    '4': 'Conduct disorders',
    '5': 'Delirium, dementia',
    '6': 'Bipolar disorders',
    '7': 'Depressive disorders',
    '8': 'Oppositional defiant disorders',
    '9': 'Pervasive developmental disorders',
    '10': 'Personality disorders',
    '11': 'Schizophrenia or other psychotic disorders',
    '12': 'Alcohol or substance use disorders',
    '13': 'Other',
    '-9': 'Missing'
}


plt.figure(figsize=(10, 6))
bar_plot = issue_counts.plot(kind='bar', color='royalblue')
plt.title('Mental Health Issues Among Clients', fontsize=18, fontname='Times New Roman',y=1.02) 
plt.xlabel('Mental Health Issue', fontname='Times New Roman')  
plt.ylabel('Number of Clients Affected', fontname='Times New Roman') 
plt.xticks(rotation=45, ha='right', fontname='Times New Roman')  

plt.gca().set_xticklabels([issue_mapping.get(label.get_text(), label.get_text()) for label in plt.gca().get_xticklabels()])

plt.gca().grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('MH Bar Chart.png', dpi=300)
plt.show()