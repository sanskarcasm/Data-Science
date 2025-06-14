import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Added missing import

excel_file = "C:\\Users\\Owner\\Sanskar\\Projects\\Project 1\\MyThrivingChild\\Datasets\\Instagram_Analytics.xlsx"

# Read data with explicit engine specification
xls = pd.ExcelFile(excel_file)
df_demographics = pd.read_excel(excel_file, sheet_name="Instagram Age Gender Demographi")
df_engagement = pd.read_excel(excel_file, sheet_name="Instagram Post Engagement")
df_overview = pd.read_excel(excel_file, sheet_name="Instagram Profile Overview")
df_cities = pd.read_excel(excel_file, sheet_name="Instagram Top Cities Regions")

# Data cleaning with more robust handling
def clean_data(df, columns):
    
    initial_count = len(df)
    df_clean = df.dropna(subset=columns)
    final_count = len(df_clean)
    print(f"Removed {initial_count - final_count} rows with missing values")
    return df_clean

df_demographics = clean_data(df_demographics, ['Gender', 'Age', 'Profile followers', 'RowHash'])
df_overview = clean_data(df_overview, ['Date','Profile impressions','Shares','Engagement','Profile visits','Profile reach','Reel shares', 'New followers', 'RowHash'])
df_cities = clean_data(df_cities, ['City','Area & city', 'Area', 'Profile followers', 'RowHash'])
df_engagement = clean_data(df_engagement, ['Date', 'Media ID', 'Media caption', 'Media product type', 
                                         'Media impressions', 'Media reach', 'Like count', 
                                         'Comments count', 'Shares', 'Unique saves', 'Video views', 'RowHash'])

# Convert date with error handling
df_engagement['Date'] = pd.to_datetime(df_engagement['Date'], errors='coerce')

# Calculate metrics with type conversion
df_engagement = df_engagement.astype({
    'Like count': 'int',
    'Comments count': 'int',
    'Shares': 'int',
    'Unique saves': 'int',
    'Media impressions': 'int'
})

df_engagement['Total Engagement'] = (
    df_engagement['Like count'] +
    df_engagement['Comments count'] +
    df_engagement['Shares'] +
    df_engagement['Unique saves']
)

# Engagement rate calculation with zero-division guard
df_engagement['Engagement Rate'] = df_engagement.apply(
    lambda row: (row['Total Engagement'] / row['Media impressions']) * 100 if row['Media impressions'] > 0 else 0,
    axis=1
)

# Basic Analysis
avg_engagement_rate = df_engagement['Engagement Rate'].mean()
print(f"\nAverage Engagement Rate: {avg_engagement_rate:.2f}%")

# Top post with proper column reference
top_post = df_engagement.loc[df_engagement['Total Engagement'].idxmax()]
print("\nTop Performing Post:")
print(top_post[['Media ID', 'Media caption', 'Media product type', 'Total Engagement', 'Engagement Rate']])

# Visualization
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_engagement, x='Date', y='Total Engagement', marker='o')
plt.title('Instagram Engagement Over Time')
plt.ylabel('Total Engagement')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Post type comparison
media_type_summary = df_engagement.groupby('Media product type', as_index=False)['Total Engagement'].mean()

plt.figure(figsize=(8, 5))
sns.barplot(data=media_type_summary, x='Media product type', y='Total Engagement', palette='muted')
plt.title('Average Engagement by Post Type')
plt.ylabel('Average Engagement')
plt.xlabel('Media Product Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bonus Task: well performing post prediction function
def predict_well_performing_posts(df, threshold_percentile=75):
   
    threshold = df['Engagement Rate'].quantile(threshold_percentile / 100)
    df['Is_Well_Performing'] = df['Engagement Rate'] >= threshold
    print(f"\nThreshold for well-performing posts: {threshold:.2f}%")
    print("Performance Classification:")
    print(df['Is_Well_Performing'].value_counts())
    return df

df_engagement = predict_well_performing_posts(df_engagement)
