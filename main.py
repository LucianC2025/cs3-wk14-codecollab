import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#pip install wordcloud

# NOTE: for this week's discussion, make an attempt to guess
# the "question" I was trying to answer with each plot!
df = pd.read_csv('netflix.csv')
print(df.info())
print(df.head(10))

# 1. HISTPLOT
plt.figure(figsize=(12, 8))
sns.histplot(data=df, x='imdb_score', bins=20, kde=True)
plt.xlabel('IMDb Score')
plt.ylabel('Count')
plt.title('Distribution of IMDb Scores of Netflix Titles')
plt.savefig('histplot.png', bbox_inches='tight', dpi=200)

# 2. LINE PLOT
# Prepare data
avg_score_by_year = df.groupby(
    'release_year')['imdb_score'].mean().reset_index()
# Create plot
plt.figure(figsize=(12, 6))
sns.lineplot(x='release_year', y='imdb_score', data=avg_score_by_year)
plt.title('Average IMDb Score Over Years')
plt.xticks(rotation=45)
plt.savefig('lineplot.png', bbox_inches='tight', dpi=200)

# 3. PIE CHART
# Prepare data
type_counts = df['type'].value_counts()
# Create plot
plt.figure(figsize=(8, 6))
plt.pie(type_counts,
        labels=type_counts.index,
        autopct='%1.1f%%',
        startangle=140)
plt.title('Distribution of Netflix Content Types')
plt.savefig('piechart.png', bbox_inches='tight', dpi=200)

# 4. BAR PLOT with sorted df
# Prepare data
longest_runtimes = df.nlargest(30, 'runtime')
# Create plot
plt.figure(figsize=(10, 6))
sns.barplot(x='runtime',
            y='title',
            data=longest_runtimes,
            hue='type',
            palette='coolwarm')
plt.title('Netflix Titles with the Longest Runtimes')
plt.xlabel('Runtime (minutes)')
plt.ylabel('Title') 
plt.savefig('barplot.png', bbox_inches='tight', dpi=200)
