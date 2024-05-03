import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster import hierarchy
from scipy.spatial import distance
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import seaborn as sns

'''
df = pd.read_csv('MH_CLD.csv')


mental_health_issues = df[['TRAUSTREFLG', 'ANXIETYFLG', 'ADHDFLG', 'CONDUCTFLG', 'DELIRDEMFLG', 
                   'BIPOLARFLG', 'DEPRESSFLG', 'ODDFLG', 'PDDFLG', 'PERSONFLG', 'SCHIZOFLG', 
                   'ALCSUBFLG', 'OTHERDISFLG']]
mental_health_issues.columns = ['Trauma', 'Anxiety', 'ADHD', 'Conduct', 'Delirium', 'Bipolar', 'Depression',
                                'ODD', 'PDD', 'Personality', 'Schizophrenia', 'Alcohol/Substance', 'Other Disorder']



distance_matrix = distance.pdist(mental_health_issues.T, metric='hamming')
square_distance_matrix = distance.squareform(distance_matrix)

square_distance_matrix_df = pd.DataFrame(square_distance_matrix, columns=mental_health_issues.columns, index=mental_health_issues.columns)
square_distance_matrix_df.to_csv('matrix_data.csv', index=False)

linkage = hierarchy.linkage(distance_matrix, method='ward')

plt.figure(figsize=(12, 6))
hierarchy.dendrogram(linkage, labels=mental_health_issues.columns, leaf_rotation=90, leaf_font_size=10)
plt.xlabel('Mental Health Issues', fontsize=12,fontname='Times New Roman')
plt.ylabel('Distance', fontsize=12,fontname='Times New Roman')
plt.title('Hierarchical Clustering Dendrogram', fontsize=18, fontname='Times New Roman', y=1.02)

plt.savefig('MH Hierarchical Clustering.png', transparent=True, dpi=300, bbox_inches='tight')
plt.show()
'''
co_occurrence_matrix = pd.read_csv('co_occurrence_matrix.csv', index_col=0)

# Convert the entries to numeric values
co_occurrence_matrix = co_occurrence_matrix.apply(pd.to_numeric, errors='coerce')

# Sort the DataFrame based on the sum of each row in descending order
co_occurrence_matrix = co_occurrence_matrix.loc[co_occurrence_matrix.sum(axis=1).sort_values(ascending=False).index]
co_occurrence_matrix = co_occurrence_matrix[co_occurrence_matrix.sum().sort_values(ascending=False).index]

# Save the sorted DataFrame back to a CSV file
co_occurrence_matrix.to_csv('sorted_co_occurrence_matrix.csv')