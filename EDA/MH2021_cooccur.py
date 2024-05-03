import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.spatial import distance
from scipy.cluster import hierarchy

df = pd.read_csv('MH_CLD.csv')



mental_health_issues_filtered = df[df[['TRAUSTREFLG', 'ANXIETYFLG', 'ADHDFLG', 'CONDUCTFLG', 'DELIRDEMFLG', 
                      'BIPOLARFLG', 'DEPRESSFLG', 'ODDFLG', 'PDDFLG', 'PERSONFLG', 'SCHIZOFLG', 
                      'ALCSUBFLG', 'OTHERDISFLG']].sum(axis=1) >= 2]

mental_health_issues = mental_health_issues_filtered[['TRAUSTREFLG', 'ANXIETYFLG', 'ADHDFLG', 'CONDUCTFLG', 'DELIRDEMFLG', 
                                                      'BIPOLARFLG', 'DEPRESSFLG', 'ODDFLG', 'PDDFLG', 'PERSONFLG', 
                                                      'SCHIZOFLG', 'ALCSUBFLG', 'OTHERDISFLG']]

mental_health_issues.columns = ['Trauma', 'Anxiety', 'ADHD', 'Conduct', 'Delirium', 'Bipolar', 'Depression',
                                'ODD', 'PDD', 'Personality', 'Schizophrenia', 'Alcohol/Substance', 'Other Disorder']



###########Hamming Distance Heatmap Visualization
distance_matrix = pd.DataFrame(distance.squareform(distance.pdist(mental_health_issues.T, metric='hamming')),
                               index=mental_health_issues.columns, columns=mental_health_issues.columns)

plt.figure(figsize=(10, 8))
sns.heatmap(distance_matrix, cmap='cubehelix', annot=False, square=True)
plt.title('Hamming Distance Heatmap of Mental Health Issues', fontsize=18, fontname='Times New Roman', y=1.02)
plt.xticks(fontsize=10,fontname='Times New Roman', rotation=90)
plt.yticks(fontsize=10,fontname='Times New Roman')
plt.tight_layout()
#plt.savefig('MH_Hamming_Distance_Heatmap2.png', transparent=True, dpi=300, bbox_inches='tight')
plt.show()





###########Hierarchical Clustering Visualization
distance_matrix = distance.pdist(mental_health_issues.T, metric='hamming')
linkage = hierarchy.linkage(distance_matrix, method='ward')

plt.figure(figsize=(12, 6))
hierarchy.dendrogram(linkage, labels=mental_health_issues.columns, leaf_rotation=90, leaf_font_size=10)
plt.xlabel('Mental Health Issues', fontsize=12,fontname='Times New Roman')
plt.ylabel('Distance', fontsize=12,fontname='Times New Roman')
plt.title('Hierarchical Clustering Dendrogram', fontsize=18, fontname='Times New Roman', y=1.02)

#plt.savefig('MH_Hierarchical_Clustering2.png', transparent=True, dpi=300, bbox_inches='tight')
plt.show()
