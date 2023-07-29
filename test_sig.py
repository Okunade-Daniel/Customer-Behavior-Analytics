for i,x in control_stores.items():
    t1 = new_df[new_df['store_no']==i]['total_sales']
    c1 = new_df[new_df['store_no']==x]['total_sales']
    # Conduct the t-test
    t_statistic, p_value = stats.ttest_ind(t1, c1)
    print('For trial store {} and control store {},The results are ->\nt_statistic: {:.3f}\n p_value: {:.3f}'.\
          format(i,x,t_statistic, p_value))
    print('\n')

#Visually checking
for store1,store2 in control_stores.items():
    
    subset = new_df[(new_df['store_no']==store1)|(new_df['store_no']==store2)]
    #subset['month'] = subset['date'].dt.month
    subset_grouped = subset.groupby(['month','store_no'], as_index=False)['total_sales'].mean()
    plt.figure(figsize=(18,8))
    ax=sns.barplot(data=subset_grouped,x='month', y= 'total_sales', hue='store_no')
    plt.title(f'Comparison of Average sales between store {store1} and {store2} by month',fontsize=12)
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Average Sales', fontsize=14)
    for bar in ax.containers:
        ax.bar_label(bar, label_type='edge', fontsize=10,fmt='%.1f')
    plt.legend(loc='lower center',fontsize=14,title='Stores')
    plt.show()
