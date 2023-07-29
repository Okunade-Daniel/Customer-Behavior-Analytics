# Define the function to calculate compare store
def compare_store(store1, store2):
    # Extract the monthly data for each store
    store1_data = new_df[new_df["store_no"] == store1].groupby('month').\
    agg({"total_sales": "sum", "loyalty_card_no": "nunique", "transaction_id": "nunique"})
    store2_data = new_df[new_df["store_no"] == store2].groupby('month').\
    agg({"total_sales": "sum", "loyalty_card_no": "nunique", "transaction_id": "nunique"})
    
    # Calculate the average number of transactions per customer for each store
    
    store1_data["Avg_transaction_per_cust"] = store1_data["transaction_id"] / store1_data["loyalty_card_no"]
    store2_data["Avg_transaction_per_cust"] = store2_data["transaction_id"] / store2_data["loyalty_card_no"]
    
    # Calculate the Pearson correlation coefficient for each metric
    
    if len(store1_data) == len(store2_data):
        
        sales_distance = np.sum(np.abs(np.array(store1_data["total_sales"]) - np.array(store2_data["total_sales"])))
        sales_similarity = 1 / (1 + sales_distance)
        cust_distance = np.sum(np.abs(np.array(store1_data["loyalty_card_no"]) - np.array(store2_data["loyalty_card_no"])))
        cust_similarity = 1 / (1 + cust_distance)
        tran_distance = np.sum(np.abs(np.array(store1_data["Avg_transaction_per_cust"]) - np.array(store2_data["Avg_transaction_per_cust"])))
        tran_similarity = 1 / (1 + tran_distance)
        similarity_score = (sales_similarity + cust_similarity + tran_similarity)/3
        return similarity_score
    else:
        pass
       
# Find the right control store for each Trial store
# List the trial stores
trial_stores = [77, 86, 88]
# List all stores
all_stores = new_df["store_no"].unique()
# Create an empty dictionary to store the control stores for each trial store
control_stores = {}
# Loop through each trial store
for trial_store in trial_stores:
    # Initialize the best score and the best control store
    best_score = 0
    best_control_store = None
    # Loop through each potential control store
    for potential_control_store in all_stores:
        # Skip if the potential control store is the same as the trial store
        if potential_control_store != trial_store:
            #pass
            # Calculate the similarity score between the trial store and the potential control store
            score = compare_store(trial_store, potential_control_store)
            #print(score)
            # Update the best score and the best control store if the score is higher than the current best score
            if score is not None and score > best_score:
                best_score = score
                best_control_store = potential_control_store
                # Store the best control store for the trial store in the dictionary
                control_stores[trial_store] = best_control_store

# Print the control stores for each trial store
print(control_stores)
