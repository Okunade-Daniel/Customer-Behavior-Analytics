# Investigate drivers of Sales in the stores where there is a significant difference
# Finding which of the metric is driving sales

store77_data = new_df[new_df["store_no"] == 77].groupby(new_df['date'].dt.month).\
    agg({"total_sales": "sum", "loyalty_card_no": "nunique", "transaction_id": "nunique",'product_quantity':'sum'})
store77_data["Avg_transaction_per_cust"] = store77_data["transaction_id"] / store77_data["loyalty_card_no"]


store64_data = new_df[new_df["store_no"] == 64].groupby(new_df['date'].dt.month).\
    agg({"total_sales": "sum", "loyalty_card_no": "nunique", "transaction_id": "nunique",'product_quantity':sum})
store64_data["Avg_transaction_per_cust"] = store64_data["transaction_id"] / store64_data["loyalty_card_no"]

store88_data = new_df[new_df["store_no"] == 88].groupby(new_df['date'].dt.month).\
    agg({"total_sales": "sum", "loyalty_card_no": "nunique", "transaction_id": "nunique",'product_quantity':sum})
store88_data["Avg_transaction_per_cust"] = store88_data["transaction_id"] / store88_data["loyalty_card_no"]

store162_data = new_df[new_df["store_no"] == 162].groupby(new_df['date'].dt.month).\
    agg({"total_sales": "sum", "loyalty_card_no": "nunique", "transaction_id": "nunique",'product_quantity':sum})
store162_data["Avg_transaction_per_cust"] = store88_data["transaction_id"] / store88_data["loyalty_card_no"]

# Rename the columns
store77_data.columns = ['total_sales','total_no_customers','total_transaction','product_quantity','Avg_transaction_per_cust']
store64_data.columns = ['total_sales','total_no_customers','total_transaction','product_quantity','Avg_transaction_per_cust']
store88_data.columns = ['total_sales','total_no_customers','total_transaction','product_quantity','Avg_transaction_per_cust']
store162_data.columns = ['total_sales','total_no_customers','total_transaction','product_quantity','Avg_transaction_per_cust']

# Find the metric driving sales for each store
def sales_driver(df,y,z):
    x = df.drop(y,axis='columns')
    y = df[y]
    x_scaled = scaler.fit_transform(x)
    lr.fit(x_scaled,y)
    r_sq = lr.score(x_scaled,y)
    slope = list(lr.coef_)
    driver = max(slope)
    driver_loc = slope.index(driver)
    variables = x.columns.to_list()
    driver_var = variables[driver_loc]
    sns.barplot(x=variables, y = slope)
    plt.figure(figsize=(18,8))  
    plt.title(f'Sales Driver for store {z}')
    plt.xticks(rotation=45)
    plt.show()
    return f'The Top driver of sale for the store {z} is:\n{driver_var} ({round(driver,2)})'#\n{driver2_var}:{round(driver2,2)}'

# using the function
print(sales_driver(store77_data,'total_sales',77))
print('\n')
print(sales_driver(store64_data,'total_sales',64))
print('\n')
print(sales_driver(store88_data,'total_sales',88))
print('\n')
print(sales_driver(store162_data,'total_sales',162))
