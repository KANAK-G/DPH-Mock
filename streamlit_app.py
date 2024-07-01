import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the mock data
df = pd.read_csv('mock_data.csv')

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



