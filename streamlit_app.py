import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st



# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# 1. Generate Query IDs
query_ids = range(1, 10001)

# 2. Generate Query Texts (some duplicates)
sql_queries = ["SELECT * FROM table1;", "SELECT * FROM table2 WHERE condition;",
               "UPDATE table3 SET column = value;", "DELETE FROM table4 WHERE condition;",
               "INSERT INTO table5 (columns) VALUES (values);"]
query_texts = np.random.choice(sql_queries, size=10000, p=[0.2, 0.3, 0.2, 0.2, 0.1])

# 3. Generate User IDs and assign to data products
user_ids = list(range(1, 51))
data_products = ['device360', 'customer360', 'store360', 'sales360']

# Distribute users across data products
user_data_product = {}
for i, dp in enumerate(data_products):
    start_idx = i * 10
    end_idx = start_idx + (10 if i != 3 else 15)
    for user_id in user_ids[start_idx:end_idx]:
        user_data_product[user_id] = dp

# Distribute queries across data products
queries_per_product = {'device360': 4000, 'customer360': 2500, 'store360': 2000, 'sales360': 1500}
user_queries = []

for dp, count in queries_per_product.items():
    users = [user for user, product in user_data_product.items() if product == dp]
    user_queries.extend(random.choices(users, k=count))

# 4. Generate Dataset IDs
dataset_ids = {dp: [f'{dp}_dataset_{i}' for i in range(1, 21)] for dp in data_products}
query_dataset_ids = [random.choice(dataset_ids[user_data_product[user_id]]) for user_id in user_queries]

# 5. Generate Error Texts
errors = ["system generated error", "syntax related error", "resource exceed error", None]
error_texts = np.random.choice(errors, size=10000, p=[0.05, 0.05, 0.05, 0.85])

# 6. Generate Memory Usage
memory_usage = np.random.uniform(10, 20, size=10000).round(2)

# 7. Generate Compute Usage
compute_usage = np.random.uniform(10, 20, size=10000).round(2)

# 8. Generate Data Processed
data_processed = np.random.uniform(10, 20, size=10000).round(2)

# 9. Generate Date Column
end_date = datetime.now()
start_date = end_date - timedelta(days=60)
date_range = pd.date_range(start_date, end_date)
dates = np.random.choice(date_range, size=10000)

# 10. Generate Data Product Name
dp_names = [user_data_product[user_id] for user_id in user_queries]

# Create DataFrame
data = {
    'Query ID': query_ids,
    'Query Text': query_texts,
    'User ID': user_queries,
    'Dataset ID': query_dataset_ids,
    'Error Text': error_texts,
    'Memory Usage (GB)': memory_usage,
    'Compute Usage (GB)': compute_usage,
    'Data Processed (GB)': data_processed,
    'Date': dates,
    'Data Product Name': dp_names
}

df = pd.DataFrame(data)

# Save to CSV
# df.to_csv('mock_data.csv', index=False)

# Display first few rows
# df.head()

# # Load the mock data
# df = pd.read_csv('mock_data.csv')

# Set plot style
sns.set(style="whitegrid")

st.title('Mock Data Visualization')

# 1. Unique users per data product
st.subheader('Unique Users per Data Product')
unique_users_per_product = df.groupby('Data Product Name')['User ID'].nunique()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=unique_users_per_product.index, y=unique_users_per_product.values, ax=ax)
ax.set(title='Unique Users per Data Product', xlabel='Data Product Name', ylabel='Unique Users')
# Display the figure using st.pyplot()
st.pyplot(fig)


# 2. Total queries per data product
st.subheader('Total Queries per Data Product')
total_queries_per_product = df['Data Product Name'].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=total_queries_per_product.index, y=total_queries_per_product.values, ax=ax)
ax.set(title='Total Queries per Data Product', xlabel='Data Product Name', ylabel='Total Queries')
st.pyplot(fig)  # Display the figure as an image


# 3. Total queries per user
st.subheader('Total Queries per User (Top 10)')
total_queries_per_user = df['User ID'].value_counts().head(10)  # Top 10 users
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=total_queries_per_user.index, y=total_queries_per_user.values, ax=ax)
ax.set(title='Total Queries per User (Top 10)', xlabel='User ID', ylabel='Total Queries')
plt.xticks(rotation=90)
st.pyplot(fig)  # Display the figure as an image


# 4. Error distribution across data products
st.subheader('Error Distribution across Data Products')
error_distribution = df[df['Error Text'].notnull()].groupby(['Data Product Name', 'Error Text']).size().unstack(fill_value=0)
fig, ax = plt.subplots(figsize=(10, 6))
error_distribution.plot(kind='bar', stacked=True, ax=ax)
ax.set(title='Error Distribution across Data Products', xlabel='Data Product Name', ylabel='Error Count')
st.pyplot(fig)  # Display the figure as an image


# Users with high failed queries
st.subheader('Users with High Failed Queries (Top 10)')
failed_queries = df[df['Error Text'].notnull()]
failed_queries_per_user = failed_queries['User ID'].value_counts().head(10)  # Top 10 users
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=failed_queries_per_user.index, y=failed_queries_per_user.values, ax=ax)
ax.set(title='Users with High Failed Queries (Top 10)', xlabel='User ID', ylabel='Failed Queries')
plt.xticks(rotation=90)
st.pyplot(fig)  # Display the figure as an image



# 5. Average memory usage per data product
st.subheader('Average Memory Usage per Data Product')
avg_memory_usage_per_product = df.groupby('Data Product Name')['Memory Usage (GB)'].mean()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=avg_memory_usage_per_product.index, y=avg_memory_usage_per_product.values, ax=ax)
ax.set(title='Average Memory Usage per Data Product', xlabel='Data Product Name', ylabel='Average Memory Usage (GB)')
st.pyplot(fig)  # Display the figure as an image


# 6. Average compute usage per data product
st.subheader('Average Compute Usage per Data Product')
avg_compute_usage_per_product = df.groupby('Data Product Name')['Compute Usage (GB)'].mean()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=avg_compute_usage_per_product.index, y=avg_compute_usage_per_product.values, ax=ax)
ax.set(title='Average Compute Usage per Data Product', xlabel='Data Product Name', ylabel='Average Compute Usage (GB)')
st.pyplot(fig)  # Display the figure as an image


# 7. Average data processed per data product
st.subheader('Average Data Processed per Data Product')
avg_data_processed_per_product = df.groupby('Data Product Name')['Data Processed (GB)'].mean()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=avg_data_processed_per_product.index, y=avg_data_processed_per_product.values, ax=ax)
ax.set(title='Average Data Processed per Data Product', xlabel='Data Product Name', ylabel='Average Data Processed (GB)')
st.pyplot(fig)  # Display the figure as an image


# 8. Error count by type
st.subheader('Error Count by Type')
error_count = df['Error Text'].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=error_count.index, y=error_count.values, ax=ax)
ax.set(title='Error Count by Type', xlabel='Error Text', ylabel='Count')
plt.xticks(rotation=90)
st.pyplot(fig)  # Display the figure as an image


# 9. Total memory usage per user
st.subheader('Total Memory Usage per User (Top 10)')
total_memory_usage_per_user = df.groupby('User ID')['Memory Usage (GB)'].sum().sort_values(ascending=False).head(10)  # Top 10 users
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=total_memory_usage_per_user.index, y=total_memory_usage_per_user.values, ax=ax)
ax.set(title='Total Memory Usage per User (Top 10)', xlabel='User ID', ylabel='Total Memory Usage (GB)')
plt.xticks(rotation=90)
st.pyplot(fig)  # Display the figure as an image


# 10. Total compute usage per user
st.subheader('Total Compute Usage per User (Top 10)')
total_compute_usage_per_user = df.groupby('User ID')['Compute Usage (GB)'].sum().sort_values(ascending=False).head(10)  # Top 10 users
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=total_compute_usage_per_user.index, y=total_compute_usage_per_user.values, ax=ax)
ax.set(title='Total Compute Usage per User (Top 10)', xlabel='User ID', ylabel='Total Compute Usage (GB)')
plt.xticks(rotation=90)
st.pyplot(fig)  # Display the figure as an image


# 11. Total data processed per user
st.subheader('Total Data Processed per User (Top 10)')
total_data_processed_per_user = df.groupby('User ID')['Data Processed (GB)'].sum().sort_values(ascending=False).head(10)  # Top 10 users
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=total_data_processed_per_user.index, y=total_data_processed_per_user.values, ax=ax)
ax.set(title='Total Data Processed per User (Top 10)', xlabel='User ID', ylabel='Total Data Processed (GB)')
plt.xticks(rotation=90)
st.pyplot(fig)  # Display the figure as an image


# 12. Top 5 users with the highest number of queries
st.subheader('Top 5 Users by Number of Queries')
top_5_users_by_queries = df['User ID'].value_counts().head(5)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_5_users_by_queries.index, y=top_5_users_by_queries.values, ax=ax)
ax.set(title='Top 5 Users by Number of Queries', xlabel='User ID', ylabel='Total Queries')
plt.xticks(rotation=90)
st.pyplot(fig)  # Display the figure as an image


# 13. Top 5 users with the highest memory usage
st.subheader('Top 5 Users by Memory Usage')
top_5_users_by_memory_usage = df.groupby('User ID')['Memory Usage (GB)'].sum().sort_values(ascending=False).head(5)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_5_users_by_memory_usage.index, y=top_5_users_by_memory_usage.values, ax=ax)
ax.set(title='Top 5 Users by Memory Usage', xlabel='User ID', ylabel='Total Memory Usage (GB)')
plt.xticks(rotation=90)
st.pyplot(fig)  # Display the figure as an image


# 14. Top 5 users with the highest compute usage
st.subheader('Top 5 Users by Compute Usage')
top_5_users_by_compute_usage = df.groupby('User ID')['Compute Usage (GB)'].sum().sort_values(ascending=False).head(5)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_5_users_by_compute_usage.index, y=top_5_users_by_compute_usage.values, ax=ax)
ax.set(title='Top 5 Users by Compute Usage', xlabel='User ID', ylabel='Total Compute Usage (GB)')
plt.xticks(rotation=90)
st.pyplot(fig)  # Display the figure as an image


# 15. Top 5 users with the highest data processed
st.subheader('Top 5 Users by Data Processed')
top_5_users_by_data_processed = df.groupby('User ID')['Data Processed (GB)'].sum().sort_values(ascending=False).head(5)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_5_users_by_data_processed.index, y=top_5_users_by_data_processed.values, ax=ax)
ax.set(title='Top 5 Users by Data Processed', xlabel='User ID', ylabel='Total Data Processed (GB)')
plt.xticks(rotation=90)
st.pyplot(fig)  # Display the figure as an image



