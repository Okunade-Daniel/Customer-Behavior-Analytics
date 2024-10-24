# Cleaning the customer data
# Check the shape of the data
display(customer_df.shape)

# Convert column names to lower case
customer_df.columns = customer_df.columns.str.lower()

# Rename columns
customer_df.rename(columns={'lylty_card_nbr':'loyalty_card_no','lifestage':'lifestage',\
                            'premium_customer':'customer_segment'}, inplace=True)
# Check for duplicates
print(f'There are {customer_df.duplicated().sum()} duplicates in this data')

# Check the loyalty_card_no column to know the total number of customers in the data
print(f"\nThere are {customer_df['loyalty_card_no'].nunique()} customers in the data")

# Edit the lifestage column so that all the values are converted to lower case
customer_df['lifestage'] = customer_df['lifestage'].str.lower()

# Check for the number of segments in the customer_segment column
display(customer_df['customer_segment'].unique())

#Check for nulls
customer_df.isna().sum()

#Cleaning the transaction table
display(transaction_df.head(15))
print(f"\nThe Transaction data contains {transaction_df.shape[0]} rows and {transaction_df.shape[1]} columns")
print(f'\nNulls in the Transaction data are as follows \n{transaction_df.isna().sum()}')

# Convert column names to lower case
transaction_df.columns = transaction_df.columns.str.lower()

# Clean the date column
transaction_df['date'] = pd.to_datetime(transaction_df['date'])
transaction_df.insert(1,'month',transaction_df['date'].dt.month)

# Rename the columns
transaction_df.rename(columns={'date':'date','store_nbr':'store_no','lylty_card_nbr':'loyalty_card_no',\
                               'txn_id':'transaction_id','prod_nbr':'product_no','prod_name':'product_name',\
                                'prod_qty':'product_quantity','tot_sales':'total_sales'}, inplace = True)
    
# Extracting the brand name and packsize

transaction_df['brand'] = transaction_df['product_name'].str.extract(r'^(\w+)\s.*')
transaction_df['pack_size (g)'] = transaction_df['product_name'].str.extract(r'(\d+)[gG]')

#Correcting Spelling of brand names

brands ={'Infzns':'Infuzions','Doritos':'Dorito', 'WW':'Woolworths', 'Snbts':'Sunbites','Smiths':'Smith','GrnWves':'Grain Waves'}
for brand in brands:
    transaction_df['brand'] = transaction_df['brand'].str.replace(brand, brands[brand], case=False)

# Correcting spellings and standardizing the product name column

corrections = {'compny': 'Company','chps':'Chips', 'chp':'chip', 's/cream':'Sour Cream','jlpno':'Jalapeno','hny':'Honey',\
               'gcamole':'Guacamole','hrb':'Herb','spce':'Spice','orgnl':'Original','swt':'Sweet','siracha':'Sriracha',\
               'infzns':'Infuzions','grnWves':'Grain Waves','btroot':'Beetroot','snbts':'Sunbites','whlgrn':'Wholegrain',\
               'whlegrn':'Wholegrain','frch/onin':'French/Onion'}
for word in corrections:
    transaction_df['product_name'] = transaction_df['product_name'].str.replace(word,corrections[word],case = False).str.strip()
transaction_df['product_name'] = transaction_df['product_name'].str.replace('&', ' & ')
transaction_df['product_name'] = transaction_df['product_name'].str.replace(r'\s+', ' ',regex=True)
transaction_df['product_name'] = transaction_df['product_name'].str.replace(r'([a-z])([A-Z])', r'\1 \2',regex=True)
transaction_df['product_name'] = transaction_df['product_name'].str.replace(r'([a-z])([0-9])', r'\1 \2',regex=True)
transaction_df['product_name'] = transaction_df['product_name'].str.extract(r'(\w.*)\s\d+[gG]',expand=True).iloc[:,0]

print(transaction_df.info())
display(transaction_df.head(10))

# Treating Numerical Columns
# see the summary statistics of the columns

display(transaction_df[['product_quantity','total_sales']].describe())

print(f"Unique Values in Product Quantity columns are: {transaction_df['product_quantity'].unique()}")

print(f"Unique Values in Total Sales columns are: {transaction_df['total_sales'].unique()}")

# Using Tukey's fences, identify outliers in the columns
def find_outliers(df,cols):
    for col in cols:
        # Calculate the quartiles
        q1 = np.percentile(df[col], 25)
        q3 = np.percentile(df[col], 75)
        # Calculate the IQR
        iqr = q3 - q1
        # Calculate the Tukey's fences
        lower_fence = q1 - 3 * iqr
        upper_fence = q3 + 3 * iqr
        # Identify the outliers
        outliers = df[(df[col] < lower_fence) | (df[col] > upper_fence)]
        print(f'the outliers in {col} are {outliers[col].unique()}')
        print(f'the percentage is {len(outliers)/len(df)}\n')
# Use the defined function
find_outliers(transaction_df, ['product_quantity','total_sales'])

# The outliers in the product quantity column are about 11 percent of the data, dropping them could cause us to loose
# meaningful data, however, Seeing that d % of outliers in d total sales column is minute we could filter them out instead

sns.histplot(x=transaction_df['total_sales'], bins = 10)
plt.title('Distibution of Total sales with Outliers')
plt.show()

transaction_df = transaction_df[transaction_df['total_sales']<21]

sns.histplot(x=transaction_df['total_sales'], bins = 10)
plt.title('Distibution of Total sales without Outliers')
plt.show()

print(f'The total number of observations after filtering out outliers is {len(transaction_df)}')

# Merge the dataframes together
new_df = transaction_df.merge(customer_df,on='loyalty_card_no')
# Check the merged data
new_df.isna().sum()

# Save the data
new_df.to_csv(r'C:\Users\DELL\Desktop\DASL 5 folder\dasl_final.csv')

# View the newly merged dataframe 
display(new_df.head())

# View the shape of the newly merged dataframe
print(new_df.shape)
