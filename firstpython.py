import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the URL
boston_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/boston_housing.csv'
df = pd.read_csv(boston_url)

# Discretize AGE variable
bins = [0, 35, 70, 100]
labels = ['35 years and younger', 'between 35 and 70 years', '70 years and older']
df['AGE_group'] = pd.cut(df['AGE'], bins=bins, labels=labels, include_lowest=True)

# Create visualizations
fig, axs = plt.subplots(3, 2, figsize=(15, 15))

# Boxplot for MEDV (Median Value of Owner-Occupied Homes)
axs[0, 0].boxplot(df['MEDV'])
axs[0, 0].set_title('Boxplot for Median Value of Owner-Occupied Homes (MEDV)')
axs[0, 0].set_ylabel('MEDV')

# Bar Plot for CHAS (Charles River Variable)
chas_counts = df['CHAS'].value_counts()
axs[0, 1].bar(chas_counts.index, chas_counts.values)
axs[0, 1].set_title('Bar Plot for Charles River Variable (CHAS)')
axs[0, 1].set_xlabel('CHAS')
axs[0, 1].set_ylabel('Count')
axs[0, 1].set_xticks([0, 1])

# Boxplot for MEDV vs AGE_group
df.boxplot(column='MEDV', by='AGE_group', ax=axs[1, 0])
axs[1, 0].set_title('Boxplot of MEDV by Age Group')
axs[1, 0].set_xlabel('Age Group')
axs[1, 0].set_ylabel('MEDV')

# Scatter Plot for NOX (Nitric Oxide Concentrations) vs INDUS (Proportion of Non-Retail Business Acres per Town)
axs[1, 1].scatter(df['INDUS'], df['NOX'])
axs[1, 1].set_title('Scatter Plot of NOX vs INDUS')
axs[1, 1].set_xlabel('Proportion of Non-Retail Business Acres per Town (INDUS)')
axs[1, 1].set_ylabel('Nitric Oxide Concentration (NOX)')

# Histogram for PTRATIO (Pupil to Teacher Ratio)
axs[2, 0].hist(df['PTRATIO'], bins=20)
axs[2, 0].set_title('Histogram of Pupil to Teacher Ratio (PTRATIO)')
axs[2, 0].set_xlabel('Pupil to Teacher Ratio (PTRATIO)')
axs[2, 0].set_ylabel('Frequency')

# Remove empty subplot
fig.delaxes(axs[2, 1])

plt.tight_layout()
plt.savefig('boston_visualization.png')
plt.show()


