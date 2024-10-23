# Customer Behavior Analytics

# Introduction
In today's highly competitive retail landscape, understanding customer behavior and product preferences are critical for businesses to thrive and remain profitable. For companies in the Fast-Moving Consumer Goods (FMCG) sector, gaining insight into customer purchasing behavior is essential to developing effective strategies that drive sales, revenue growth, and customer satisfaction.

The objective of this analysis was to:

understand the types of customers who purchase Chips and their purchasing behaviour within the business region.
identify new trial layouts for some identified control layout using similarity calculations
test the impact of the new trial layouts with a data-driven recommendation as to whether or not the trial layout should be rolled out to all their stores.
provide insights provide data-driven recommendations to inform strategic decision-making and improve sales and customer satisfaction.

# Outcomes
This project was a great opportunity for me to apply my data analysis skills and knowledge to a real-world business problem. I learned how to use various techniques such as similarity calculation to explore and evaluate the effectiveness of a new store layout. Through this project, I was able to demonstrate my ability to provide valuable insights and recommendations that can help the retailer improve their sales and customer satisfaction. This project also helped me enhance my data storytelling, communication and presentation skills, as I had to explain my findings and suggestions in a clear and concise manner.

# Methodology
# Data Preparation
For this analysis, the GigShot customer data and transactions data were provided. Before performing any analysis, I performed the following steps to clean and transform the data:

I Checked the shape of the data and looked for any missing values. I found that there were no nulls in the dataset, so I did not need to impute or drop any rows or columns.

I Standardized the column names by converting them to lowercase and giving them more descriptive names. For example, I renamed the column LYLTY_CARD_NBR to loyalty_card_no and changed data type to its correct format.

I Extracted two new columns from the product column: brand and pack_size. I assumed that the brand name was the first word in the product name, and the pack size was the last word ending with g or G. I also removed any extra spaces and punctuation from the product name and created a new column product_name that contained only the product name without the pack size.

I Standardized the spelling and formatting of the brand, product, and product_name columns. I used a dictionary to map different spellings of the same brand or product to a single standard name. For example, I mapped compny to company, chps to chips,  hrbs to herbs and so on. I also added spaces between words that were concatenated.

I Detected and removed outliers in the product_quantity and total_sales columns using the Tukey Fences method1 This method defines outliers as values that are more than 1.5 times the interquartile range (IQR) away from the first or third quartile. I used a more conservative threshold of 3 times the IQR to identify outliers. I found that about 11% of the values in the product_quantity column and less than 1% of the values in the total_sales column were outliers. Since the two columns had a moderate positive correlation, I decided to remove only the outliers in the total_sales column, as they could skew the results of the analysis. I kept the outliers in the product_quantity column, as dropping or imputing them could introduce bias or reduce information.

# Data Exploration
After cleaning and transforming the data, I performed some exploratory data analysis to answer the following questions:

What are the frequently purchased brands?
Who are the most frequent customers?
How many customers are there in total?
What are the most popular brands?
What are the proportion of each customer segment?
What is the relationship between product quantity and total sales?
How does sales differ by brands and customer segments?
What is the average monthly sales by customer segments?

To answer these questions, I used various techniques such as descriptive statistics, bar charts, pie charts, scatter plots, and correlation coefficients. I also used some domain knowledge to interpret the results and provide insights. For example, I found that the most frequently purchased brands were Kettle, Smith, and Dorito. I also found that the most frequent customers were those in the mainstream segment, who made up 38.5% of the total customer base. I also discovered that there was a moderate positive correlation between product quantity and total sales, which indicated that customers tended to buy more products when they spent more money.

In order to identify the control store for each trial store, I used the Manhattan similarity measure, which is a distance metric that measures the similarity between two data points. It is also known as the L1 distance or taxicab distance. This measure was chosen because it is simple, efficient, robust, and scale-invariant. The formula for the Manhattan similarity measure is:

d(x,y)=i=1∑n​∣xi​−yi​∣

where x and y are two data points with n dimensions.

Using this measure, I calculated the distance between each trial store and every other store in the dataset,  and selected the store with the smallest distance as the control store. The control stores for the trial stores 77, 86, and 88 were 64, 122, and 162, respectively.

I used t-tests to test the hypotheses drawn from the exploration. The null hypothesis was that there was no significant difference between the average sales of the trial and control stores. The alternative hypothesis was that there was a significant difference between the average sales of the trial and control stores. I used a two-sample t-test to compare the means of the two samples, and set the significance level at 0.05. The decision rule was:

If p-value <= 0.05, reject the null hypothesis and conclude that there is a significant difference between the average sales of the trial and control stores.
If p-value > 0.05, fail to reject the null hypothesis and conclude that there is no significant difference between the average sales of the trial and control stores.

The results of the t-tests were as follows:

For trial store 77 and control store 64, the p-value was 0.000, which was less than 0.05. Therefore, I rejected the null hypothesis and concluded that there was a significant difference between the average sales of the trial and control stores.
For trial store 86 and control store 122, the p-value was 0.606, which was greater than 0.05. Therefore, I failed to rejected the null hypothesis and concluded that there was no significant difference between the average sales of the trial and control stores.
For trial store 88 and control store 162, the p-value was 0.000, which was less than 0.05. Therefore, I rejected the null hypothesis and concluded that there was a significant difference between the average sales of the trial and control stores.

Using linear regression, I identified the metrics that drove sales. Linear regression was selected in this case because there was a linear relationship between the dependent variable (total sales) and the independent variables. I fitted a multiple linear regression model using the following equation:

y=β0​+β1​x1​+β2​x2​+...+βn​xn​+ϵ

where y is the total sales, xi​ are the independent variables, βi​ are the coefficients, and ϵ is the error term.

The results of the linear regression model showed that the most significant predictor of total sales in stores 77 and 88 was total transaction, in store 64, it was the total number of customers and in store 162 it was product quantity. The coefficients of these variables indicated how much the total sales would change for a unit change in the variable, holding all other variables constant.

# Visualization and presentation
To present the findings of the data analysis, I used Power BI to create a dashboard that displayed the key metrics and insights. Power BI is a powerful tool that allows users to create interactive and dynamic visualizations from various data sources. I chose Power BI because it offers a variety of chart types, customization options, and interactivity features that can enhance the communication of the data story.

The dashboard I created consisted of several charts that answered the questions I posed in the data exploration section. For example, I used a column chart to show the frequently purchase frequency by customer segments brands, a stacked bar chart to show how each customer segment differs from each other in the kind of chips purchased, and a line chart to show the trend of how much each customer segment spends on chips every day of the week. 

You can interact with the power bi report at: https://app.powerbi.com/groups/me/reports/accb7ae3-0ae2-4c6b-bd06-9e6578fadd9c?ctid=a7b15ebf-f361-4934-86c8-43f76c182d96&pbi_source=linkShare

![Overview](https://github.com/Okunade-Daniel/Customer-Behavior-Analytics/blob/main/power%20bi%20report/overview.png)
![mainstream](https://github.com/Okunade-Daniel/Customer-Behavior-Analytics/blob/main/power%20bi%20report/mainstream%20customers.png)
![budget](https://github.com/Okunade-Daniel/Customer-Behavior-Analytics/blob/main/power%20bi%20report/budget%20customers.png)
![premium](https://github.com/Okunade-Daniel/Customer-Behavior-Analytics/blob/main/power%20bi%20report/premium%20customers.png)

To complement the dashboard, I also built a PowerPoint presentation that summarized the main findings and recommendations. PowerPoint is a widely used tool that enables users to create professional and engaging slideshows. I chose PowerPoint because it integrates well with Power BI and allows me to embed the dashboard into the presentation. I also used PowerPoint’s design features, such as themes, layouts, transitions, and animations, to make the presentation visually appealing and easy to follow.

# Insights
From the analysis conducted, the following are the insights generated:
-	Mainstream customer spends more on chips than any other segment of customers
-	Mainstream customer segment also purchase chips more often than any other group of customers.
-	Kettle Mozzarella Basil and Pesto is the most purchased kind of chips.
-	The most popular brand of chips among all consumers is kettle. However, on average, every customer segment spends more money on the "Old" brand.
-	On average, across all seven days of the week, mainstream customers spend more on chips than any other customer segment. With the exception of Monday, Wednesday, and Sunday, budget customers consistently spend more than premium customers.
-	Retention rate are higher on weekends than on weekdays for all customer segment
-	Store 226, is the most patronized for Mainstream customers, Store 165 is the most patronized for premium customers while store 93 is the most patronized for Budget customers.
-	Pack size 175g was the most purchased pack across all the customer segments.
-	Trial stores 77 and 88 performed significantly differently in terms of sales compared to their respective control stores 64 and 162 with both having a p-value of 0.000. However, with a p-value of 0.606, there isn’t enough evidence to conclude that trial stores 86 performed significantly differently compared to its control store 122.
-	The results of the experiment show that the trial stores 77 and 88 had significantly higher sales than their respective control stores. This is likely due to the new layout, which was designed to increase customer flow and impulse purchases. Hence, it is recommended that the trial layout should be implemented. 

# Recommendations
Based on the insights; the following recommendations are made.
-	Marketing and promoting chips to the mainstream customer segment should be prioritized as they spend more on chips and purchase them more often than any other group of customers.
-	Targeted advertisement should be used to promote Kettle Mozzarella Basil and Pesto chips as it is the most purchased kind of chips.
-	The ‘old’ brand should always be made available as this is the brand of chips customers spends money on.
-	The focus on budget customer segment should be increased as they have the highest retention rate and have the potential to drive more sales for the company.
-	The pack size 175g should always be available since it is the most purchased size
-	A promotional/bonus strategy should be done on weekends as it if found in the data that customers are retained more on weekends.
-	The results of the experiment show that the trial stores 77 and 88 had significantly higher sales than their respective control stores. This is likely due to the new layout, which was designed to increase customer flow and purchases. Hence, it is recommended that the trial layout should be implemented.
-	The business can also focus on improving average transaction per customer by offering discounts and other promotional strategy.

