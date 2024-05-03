import pandas as pd
import prince
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('MH_CLD.csv')
selected_columns = ["AGE", "EDUC", "ETHNIC", "RACE", "GENDER", "MARSTAT", "EMPLOY", "LIVARAG", "REGION"]
filtered_data = dataset[(dataset[selected_columns] != -9).all(axis=1) & (dataset['TRAUSTREFLG'] != 0)]

filtered_data = filtered_data[selected_columns]

mca = prince.MCA(
    n_components=1,
    n_iter=3,
    copy=True,
    check_input=True,
    engine='sklearn',
    random_state=42,
    one_hot=True 
)
mca = mca.fit(filtered_data)

cosine_similarities = mca.column_cosine_similarities(filtered_data)
cosine_similarities *= 100
cosine_similarities = cosine_similarities.round(2)
cosine_similarities_df = pd.DataFrame(cosine_similarities)
cosine_similarities_df_sorted = cosine_similarities_df.sort_values(by=0, ascending=False)
cosine_similarities_df_sorted.to_csv('cosine_similarities_traumaflg.csv', index=True)


####MCA Coordinate
'''
column_coords = mca.column_coordinates(filtered_data)

num_columns = len(selected_columns)
colors = plt.cm.tab10(np.linspace(0, 1, num_columns))

plt.figure(figsize=(8, 6))  
for i in range(num_columns):
    plt.scatter(column_coords[0][i], column_coords[1][i], color=colors[i], label=selected_columns[i])

plt.title("MCA Plot")  
plt.xlabel("Component 1") 
plt.ylabel("Component 2") 
plt.grid(True) 
plt.legend() 

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.savefig('mca_plot_person.png', transparent=True)
plt.show()

'''


####MCA Plot
'''import pandas as pd
import prince
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
dataset = pd.read_csv('MH_CLD.csv')

# Define selected columns
selected_columns = ["AGE", "EDUC", "ETHNIC", "RACE", "GENDER", "MARSTAT", "EMPLOY", "LIVARAG", "STATEFIP"]

# Filter data
filtered_data = dataset[(dataset[selected_columns] != -9).all(axis=1) & (dataset['NUMMHS'] != 0)]
filtered_data = filtered_data[selected_columns]

# Perform MCA
mca = prince.MCA(
    n_components=3,
    n_iter=3,
    copy=True,
    check_input=True,
    engine='sklearn',
    random_state=42,
    one_hot=True 
)
mca = mca.fit(filtered_data)

# Get one-hot encoded columns
one_hot_columns = mca.column_coordinates(filtered_data)

# Define colors based on selected columns
color_map = {
    "AGE": "blue",
    "EDUC": "red",
    "ETHNIC": "green",
    "RACE": "orange",
    "GENDER": "purple",
    "MARSTAT": "yellow",
    "EMPLOY": "cyan",
    "LIVARAG": "magenta",
    "STATEFIP": "brown"
}

# Plot MCA with colors based on selected columns
plt.figure(figsize=(8, 6))  
for col in selected_columns:
    mask = filtered_data[col] != -9
    plt.scatter(one_hot_columns.loc[mask, 0], one_hot_columns.loc[mask, 1], color=color_map[col], label=col)

plt.title("MCA Plot")  
plt.xlabel("Component 1") 
plt.ylabel("Component 2") 
plt.grid(True) 
plt.legend() 

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.savefig('mca_plot_new.png', transparent=True)
plt.show()
'''