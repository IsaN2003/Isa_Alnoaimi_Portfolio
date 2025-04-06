# Isa_Alnoaimi_Portfolio
Welcome to my portfolio! Below is a summary of the Python and Excel projects I created. Feel free to explore any project in the Python and Excel folders, or click on the hyperlinks provided.
## Programming Projects
### [Designing an Optimal Preventive Maintenance Plan for Pump Systems in a Urea Production Plant Using NSGA-II (Python and Excel)](Programming%20Projects/NSGA%20II%20-%20PM%20Frequency%20Optimization.ipynb)

Maintenance is essential for ensuring an efficient and streamlined operational process in the manufacturing industry. By maximizing the reliability of equipment, it is almost certain that there will be an increase in productivity, reduction of downtime, improved resource allocation, and consistency in workforce schedules. However, to achieve the highest rate of reliability, expenditures are necessary. Thus, this project aims to find the optimal preventive maintenance (PM) frequency to minimize the total cost incurred and maximize the reliability of pump systems in a Urea Production Plant by utilizing NSGA-II, a multi-objective optimization (MOO) algorithm. To quantify the reliability of the pump systems under the current PM plan, the Weibull distribution was implemented. This distribution models the failure behavior and the lifetime of the equipment by identifying the shape and scale parameters. Upon identifying the parameters and the cost of the current PM plan, a MOO problem was developed to employ NSGA-II. Following the implementation, a recommended optimal PM plan was identified, which could lead to a reduction of total costs by 14.1% and a 2.05% increase in reliability. 
<div align="center">
	<img src="https://github.com/user-attachments/assets/2a9e0d82-b7ac-4957-a134-df8208c339a9" width="50%">
</div>

### [Exploring Sampling Techniques to Enhance Credit Card Fraud Detection Accuracy Using Machine Learning (MATLAB)](Programming%20Projects/Exploring%20Sampling%20Techniques%20to%20Enhance%20Credit%20Card%20Fraud%20Detection%20Accuracy%20Using%20Machine%20Learning.ipynb)
Credit card fraud stands as a significant challenge in the financial industry. Consequently, machine learning can be utilized to mitigate the risk of fraudulent transactions. A dataset obtained from Kaggle was utilized to employ machine learning techniques on credit card fraud in MATLAB. First, a data quality report was generated to identify the data quality issues within the dataset. It was revealed that the target feature (fraud), which categorized a transaction as fraudulent or not, was highly imbalanced. Therefore, sampling techniques were implemented to tackle this issue, allowing the creation of three datasets, including the imbalanced dataset, undersampling dataset, and oversampling dataset. Next, machine learning algorithms, namely logistic regression, Naive Bayes, SVM, random forests, and decision trees, were implemented on the three datasets with MATLAB's GUI. Finally, the accuracy, F1-score, and prediction speed of the three datasets were obtained, as shown in the bar charts below. This illustrates that the machine learning algorithms successfully predicted the status of the credit card transaction.
<p align="center">
    <img src="https://github.com/user-attachments/assets/b04a45cd-a3b4-45d1-a348-9c0320c72bd3" alt="Image 1" width="250" style="margin: 0 10px;">
    <img src="https://github.com/user-attachments/assets/a0471351-6d10-4889-a3f9-bc641b679044" alt="Image 2" width="250" style="margin: 0 10px;">
    <img src="https://github.com/user-attachments/assets/0c09c07e-b937-4446-a4b9-f1d6e1b4cfa0" alt="Image 3" width="250" style="margin: 0 10px;">
</p>


### [Value at Risk (VaR) Estimation through Monte Carlo Simulation (Python)](Programming%20Projects/Value%20at%20Risk%20%28VaR%29%20Estimation%20through%20Monte%20Carlo%20Simulation.ipynb)
The Value at Risk (VaR) of a $1,000,000 portfolio that includes 50% equities, 30% bonds, and 20% commodities over a 10-day period was identified. The log returns of each underlying asset were calculated to construct a covariance matrix, which was essential for identifying the portfolio's standard deviation. A Monte Carlo simulation was run 10,000 times to assess the range of the portfolio's potential losses and gains based on specific inputs. Next, a confidence interval of 0.95 was utilized, indicating that there is a 95% confidence that the portfolio losses will not exceed -$72,622 over the 10-day period. Finally, the Monte Carlo simulation was plotted to visualize the VaR.
<div align="center">
	<img src="https://github.com/user-attachments/assets/c779618c-bf7f-42e4-ba91-d8c9a1a9be46" width="50%">
</div>

### [Correlation Analysis of the S&P 500 Sector ETFs (Python)](Programming%20Projects/Correlation%20Analysis%20of%20the%20S%26P%20500%20Sector%20ETFs.ipynb)
The correlation analysis of the S&P 500 and S&P 500 Sector ETFs offered a comprehensive understanding of the sector ETFs trends and their impact on the S&P 500. A correlation matrix was constructed to analyze the relationships between the returns of each sector. Interestingly, the S&P 500 Sector ETFs were positively correlated which can be explained by the fact that the ETFs replicate the S&P 500's movements as they hold the same underlying assets. This correlation also reflects on how the sectors' performance is affected by macroeconomic factors and market sentiment. The significant price decline during COVID, followed by the market recovery driven by macroeconomic factors and market sentiment, as shown in the line graph below, further emphasizes this relationship.
<p align="center">
	<img src="https://github.com/user-attachments/assets/caac22f9-b46c-4a6d-beb5-92cfde049f50"width="42.5%">
&nbsp; &nbsp; &nbsp; &nbsp;
	<img src="https://github.com/user-attachments/assets/94f39efa-ddb1-4323-9822-e3ad7a87baf6" width="40%">
</p>

## Excel Projects
### [A Statistical Approach to Setting Stop-Loss and Take-Profit Levels](Excel%20Projects/A%20Statistical%20Approach%20to%20Setting%20Stop-Loss%20and%20Take-Profit%20Levels.pdf)
The Monte Carlo simulation was utilized to mathematically set stop-loss and take-profit levels for the stocks which were selected in the portfolio. This simulation is a risk management tool which generates a total of 1000 random returns of a stock based on the mean and standard deviation of its two year daily returns. Then, the one percentile and 99 percentile of the randomly generated returns were used to set the stop-loss and take-profit levels. Finally, the data was visualized to represent the distribution of the simulated returns for each stock.

<div align="center">
	<img src="https://github.com/user-attachments/assets/04d47a50-8b3b-43c3-9528-0d64946966fb" width="50%">
</div>


### [Portfolio Risk Management - Portfolio Optimization](Excel%20Projects/Portfolio%20Risk%20Management%20-%20Portfolio%20Optimization.pdf)
The weights of the selected stocks in the portfolio were optimized by using historical data and statisitcal tools. By determining the optimal weights of the stocks using the solver feature in Excel, the standard deviation (risk) was minimzed and the expected return and sharpe ratio of the portfolio were maximized. To further prove that the portfolio was optimized, random weights were assigned to each stock in the portfolio 10,000 times. Next, the portfolios' respective standard deviations and expected returns were calculated. Finally, an efficient frontier was constructed to visualize the 10,000 portfolios' risk to reward possibilites. 

<p align="center">
  <img src="https://github.com/user-attachments/assets/4cfa7ee8-1869-4a12-a20d-a0a3249947e9" width="34%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://github.com/user-attachments/assets/e79434d2-34e8-41c1-af16-50b3052b7228" width="55%">
</p>

### [Optimizing Inventory Management - Identifying Order Quantity and Reorder Points](Excel%20Projects/Optimizing%20Inventory%20Management%20-%20Identifying%20Order%20Quantity%20and%20Reorder%20Points.pdf)
The optimal order quantity and reorder point of an inventory were identified by utilizing the Monte Carlo simulation and scenario analysis. A 28 day demand forecast was constructed by utilizing probabilistic assumptions based on the inputs set in the model to determine the total cost (holding cost + stockout cost + order cost) incurred by the respective order quantity and reorder point. To ensure the accuracy of the results that were obtained by the probabilistic assumptions, a Monte Carlo simulation was run 300 times to determine the average total cost of the model. Next, a scenario analysis was conducted to identify the total cost incurred by different order quantities and reorder points. Finally, the order quantity and reorder point that yielded the lowest total cost were deemed as optimal.
<div align="center">
	<img src="https://github.com/user-attachments/assets/b1ff7226-a98d-4b0e-a3bc-7c63983bd985" width="50%">
</div>

