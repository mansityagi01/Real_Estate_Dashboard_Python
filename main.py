import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import os

# Create images folder if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Set style for visualizations
plt.style.use('dark_background')
sns.set_palette("husl")

# Load data
df = pd.read_csv('Real_Estate_Sales_2001-2022_GL.csv')

# Basic data exploration
print("DATA OVERVIEW:")
print("\nFirst 5 rows of data:")
print(df.head())

print("\nLast 5 rows of data:")
print(df.tail())

print("\nDataFrame shape (rows, columns):")
print(df.shape)

print("\nColumn information:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nUnique values in categorical columns:")
print("Property Type unique values:", df['Property Type'].nunique())
print("Town unique values:", df['Town'].nunique())

# Data Cleaning
df = df[(df['List Year'] >= 0) & (df['Town'].notna()) & (df['Sale Amount'] >= 0) & 
        (df['Assessed Value'] >= 0) & (df['Sales Ratio'] >= 0)]

# Remove outliers
z_scores = np.abs(stats.zscore(df['Sales Ratio']))
df = df[(z_scores < 3)]

# Convert values to millions
df['Sale Amount'] = df['Sale Amount'] / 1e6
df['Assessed Value'] = df['Assessed Value'] / 1e6

# Get top towns and property types
top_towns = df.groupby('Town')['Sale Amount'].sum().nlargest(10).index
df_top_towns = df[df['Town'].isin(top_towns)]
top_properties = df.groupby('Property Type')['Sale Amount'].sum().nlargest(5).index

# Chart 1: Line Chart - Save individually
plt.figure(figsize=(12, 8))
df.groupby('List Year')['Sale Amount'].sum().plot(color='yellow', marker='o', linewidth=2)
plt.title('Sum of Sale Amount Over Years (2001-2022)', color='white', pad=15, fontsize=16)
plt.xlabel('List Year', color='white', labelpad=10, fontsize=14)
plt.ylabel('Sum of Sale Amount (Millions)', color='white', labelpad=10, fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.grid(True, color='gray', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('images/line_chart.png', dpi=300, bbox_inches='tight')
plt.close()

# Chart 2: Stacked Bar Chart - Save individually
plt.figure(figsize=(12, 8))
residential_by_town = df_top_towns.groupby(['Town', 'Residential Type']).size().unstack().fillna(0)
colors = sns.color_palette('husl', len(residential_by_town.columns))
residential_by_town.plot(kind='bar', stacked=True, color=colors, width=0.8)
plt.title('Residential Type Distribution by Town', color='white', pad=15, fontsize=16)
plt.xlabel('Town', color='white', labelpad=10, fontsize=14)
plt.ylabel('Count', color='white', labelpad=10, fontsize=14)
plt.xticks(rotation=45)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.grid(True, color='gray', linestyle='--', alpha=0.3)
plt.legend(title='Residential Type', fontsize=10, title_fontsize=12)
plt.tight_layout()
plt.savefig('images/stacked_bar_chart.png', dpi=300, bbox_inches='tight')
plt.close()

# Chart 3: Correlation Heatmap - Save individually
plt.figure(figsize=(12, 8))
sns.heatmap(df[['Assessed Value', 'Sale Amount', 'Sales Ratio']].corr(), 
            annot=True, cmap='viridis', linewidths=0.5, 
            cbar_kws={'label': 'Correlation'})
plt.title('Correlation Heatmap', color='white', pad=15, fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tight_layout()
plt.savefig('images/heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# Chart 4: Vertical Bar Chart - Save individually
plt.figure(figsize=(12, 8))
town_sum_sale = df_top_towns.groupby('Town')['Sale Amount'].sum().sort_values(ascending=False)
plt.bar(town_sum_sale.index, town_sum_sale, color='#66FF99', edgecolor='white')
plt.title('Total Sales by Town (Millions)', color='white', pad=15, fontsize=16)
plt.xlabel('Town', color='white', labelpad=10, fontsize=14)
plt.ylabel('Sale Amount (Millions)', color='white', labelpad=10, fontsize=14)
plt.xticks(rotation=45)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tight_layout()
plt.savefig('images/vertical_bar_chart.png', dpi=300, bbox_inches='tight')
plt.close()

# Chart 5: Horizontal Bar Chart - Save individually
plt.figure(figsize=(12, 8))
town_avg_ratio = df_top_towns.groupby('Town')['Sales Ratio'].mean().sort_values()
plt.barh(town_avg_ratio.index, town_avg_ratio, color='#FF66B2')
plt.title('Average Sales Ratio by Town', color='white', pad=15, fontsize=16)
plt.xlabel('Average Sales Ratio', color='white', labelpad=10, fontsize=14)
plt.ylabel('Town', color='white', labelpad=10, fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tight_layout()
plt.savefig('images/horizontal_bar_chart.png', dpi=300, bbox_inches='tight')
plt.close()

# Chart 6: Pie Chart - Save individually
plt.figure(figsize=(12, 8))
property_sum_sale = df[df['Property Type'].isin(top_properties)].groupby('Property Type')['Sale Amount'].sum()
colors = sns.color_palette('rainbow', len(property_sum_sale))
plt.pie(property_sum_sale, labels=property_sum_sale.index, autopct='%1.1f%%', 
        colors=colors, startangle=90, textprops={'color': 'white', 'fontsize': 12})
plt.title('Top 5 Property Type Distribution', color='white', pad=15, fontsize=16)
plt.axis('equal')
plt.tight_layout()
plt.savefig('images/pie_chart.png', dpi=300, bbox_inches='tight')
plt.close()

# Chart 7: Combo Chart - Save individually
plt.figure(figsize=(12, 8))
yearly_data = df.groupby('List Year').agg({'Assessed Value': 'sum', 'Sale Amount': 'sum'})
ax = plt.gca()
bars = ax.bar(yearly_data.index, yearly_data['Assessed Value'], 
              width=0.6, color='#6699FF', alpha=0.7, label='Assessed Value')
ax.set_xlabel('Year', color='white', labelpad=10, fontsize=14)
ax.set_ylabel('Assessed Value (Millions)', color='white', labelpad=10, fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.grid(True, color='gray', linestyle='--', alpha=0.3)

ax2 = ax.twinx()
line, = ax2.plot(yearly_data.index, yearly_data['Sale Amount'], 
                color='#FF9933', marker='o', linewidth=3, markersize=8, label='Sale Amount')
ax2.set_ylabel('Sale Amount (Millions)', color='white', labelpad=10, fontsize=14)
ax2.tick_params(axis='both', which='major', labelsize=12)

plt.title('Yearly Assessed Value vs Sales', color='white', pad=15, fontsize=16)
plt.legend([bars, line], ['Assessed Value', 'Sale Amount'], loc='upper left', fontsize=12)
plt.tight_layout()
plt.savefig('images/combo_chart.png', dpi=300, bbox_inches='tight')
plt.close()

# Chart 8: Count Plot - Save individually
plt.figure(figsize=(12, 8))
sns.countplot(data=df_top_towns, x='Town', palette='magma', 
              order=df_top_towns['Town'].value_counts().index)
plt.title('Property Count by Town', color='white', pad=15, fontsize=16)
plt.xlabel('Town', color='white', labelpad=10, fontsize=14)
plt.ylabel('Count', color='white', labelpad=10, fontsize=14)
plt.xticks(rotation=45)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tight_layout()
plt.savefig('images/count_plot.png', dpi=300, bbox_inches='tight')
plt.close()

# Create complete dashboard with all charts
fig = plt.figure(figsize=(48, 24))
plt.subplots_adjust(wspace=0.3, hspace=0.4)

# Chart 1: Line Chart (Position 1)
ax1 = plt.subplot(2, 4, 1)
df.groupby('List Year')['Sale Amount'].sum().plot(color='yellow', marker='o', linewidth=2, ax=ax1)
ax1.set_title('Sum of Sale Amount Over Years (2001-2022)', color='white', pad=15, fontsize=16)
ax1.set_xlabel('List Year', color='white', labelpad=10, fontsize=14)
ax1.set_ylabel('Sum of Sale Amount (Millions)', color='white', labelpad=10, fontsize=14)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.grid(True, color='gray', linestyle='--', alpha=0.3)

# Chart 2: Stacked Bar Chart (Position 2)
ax7 = plt.subplot(2, 4, 2)
residential_by_town.plot(kind='bar', stacked=True, color=colors, ax=ax7, width=0.8)
ax7.set_title('Residential Type Distribution by Town', color='white', pad=15, fontsize=16)
ax7.set_xlabel('Town', color='white', labelpad=10, fontsize=14)
ax7.set_ylabel('Count', color='white', labelpad=10, fontsize=14)
ax7.tick_params(axis='x', rotation=45, labelsize=12)
ax7.tick_params(axis='y', labelsize=12)
ax7.grid(True, color='gray', linestyle='--', alpha=0.3)
ax7.legend(title='Residential Type', fontsize=10, title_fontsize=12)

# Chart 3: Correlation Heatmap (Position 3)
ax2 = plt.subplot(2, 4, 3)
sns.heatmap(df[['Assessed Value', 'Sale Amount', 'Sales Ratio']].corr(), 
            annot=True, cmap='viridis', linewidths=0.5, 
            cbar_kws={'label': 'Correlation'}, ax=ax2)
ax2.set_title('Correlation Heatmap', color='white', pad=15, fontsize=16)
ax2.tick_params(axis='both', which='major', labelsize=12)

# Chart 4: Vertical Bar Chart (Position 4)
ax5 = plt.subplot(2, 4, 4)
ax5.bar(town_sum_sale.index, town_sum_sale, color='#66FF99', edgecolor='white')
ax5.set_title('Total Sales by Town (Millions)', color='white', pad=15, fontsize=16)
ax5.set_xlabel('Town', color='white', labelpad=10, fontsize=14)
ax5.set_ylabel('Sale Amount (Millions)', color='white', labelpad=10, fontsize=14)
ax5.tick_params(axis='x', rotation=45, labelsize=12)
ax5.tick_params(axis='y', labelsize=12)

# Chart 5: Horizontal Bar Chart (Position 5)
ax4 = plt.subplot(2, 4, 5)
ax4.barh(town_avg_ratio.index, town_avg_ratio, color='#FF66B2')
ax4.set_title('Average Sales Ratio by Town', color='white', pad=15, fontsize=16)
ax4.set_xlabel('Average Sales Ratio', color='white', labelpad=10, fontsize=14)
ax4.set_ylabel('Town', color='white', labelpad=10, fontsize=14)
ax4.tick_params(axis='both', which='major', labelsize=12)

# Chart 6: Pie Chart (Position 6)
ax3 = plt.subplot(2, 4, 6)
ax3.pie(property_sum_sale, labels=property_sum_sale.index, autopct='%1.1f%%', 
        colors=colors, startangle=90, textprops={'color': 'white', 'fontsize': 12})
ax3.set_title('Top 5 Property Type Distribution', color='white', pad=15, fontsize=16)
ax3.axis('equal')

# Chart 7: Combo Chart (Position 7)
ax8 = plt.subplot(2, 4, 7)
bars = ax8.bar(yearly_data.index, yearly_data['Assessed Value'], 
               width=0.6, color='#6699FF', alpha=0.7, label='Assessed Value')
ax8b = ax8.twinx()
line, = ax8b.plot(yearly_data.index, yearly_data['Sale Amount'], 
                 color='#FF9933', marker='o', linewidth=3, markersize=8, label='Sale Amount')
ax8.set_xlabel('Year', color='white', labelpad=10, fontsize=14)
ax8.set_ylabel('Assessed Value (Millions)', color='white', labelpad=10, fontsize=14)
ax8b.set_ylabel('Sale Amount (Millions)', color='white', labelpad=10, fontsize=14)
ax8.set_title('Yearly Assessed Value vs Sales', color='white', pad=15, fontsize=16)
ax8.tick_params(axis='both', which='major', labelsize=12)
ax8b.tick_params(axis='both', which='major', labelsize=12)
ax8.grid(True, color='gray', linestyle='--', alpha=0.3)
ax8.legend([bars, line], ['Assessed Value', 'Sale Amount'], loc='upper left', fontsize=12)

# Chart 8: Count Plot (Position 8)
ax6 = plt.subplot(2, 4, 8)
sns.countplot(data=df_top_towns, x='Town', palette='magma', 
              order=df_top_towns['Town'].value_counts().index, ax=ax6)
ax6.set_title('Property Count by Town', color='white', pad=15, fontsize=16)
ax6.set_xlabel('Town', color='white', labelpad=10, fontsize=14)
ax6.set_ylabel('Count', color='white', labelpad=10, fontsize=14)
ax6.tick_params(axis='x', rotation=45, labelsize=12)
ax6.tick_params(axis='y', labelsize=12)

# Save complete dashboard
plt.tight_layout()
plt.savefig('images/complete_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()