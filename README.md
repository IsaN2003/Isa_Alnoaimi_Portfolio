# Isa_Alnoaimi_Portfolio
Welcome to my portfolio! Below is a summary of the Python and Excel projects I created. Feel free to dive into any project in the Python and Excel folders.
## Python Projects
### [Correlation Analysis of the S&P 500 Sector ETFs](Correlation%20Analysis%20of%20the%20S%26P%20500%20Sector%20ETFs/Correlation%20Analysis%20of%20the%20S%26P%20500%20Sector%20ETFs.ipynb)
The correlation analysis of the S&P 500 and S&P 500 Sector ETFs offered a comprehensive understanding of the sector ETFs trends and their impact on the S&P 500. To achieve that, a correlation matrix was constructed to analyze the relationships between the returns of each sector. Interestingly, the S&P 500 Sector ETFs were positively correlated which can be explained by 
<p align="left">
	<img src="https://github.com/user-attachments/assets/14a31a96-e04a-4105-874c-9b6ca993eee2"width="55%" height="250px">
&nbsp; &nbsp; &nbsp; &nbsp;
	<img src="https://github.com/user-attachments/assets/94f39efa-ddb1-4323-9822-e3ad7a87baf6" width="38.5%">
</p>

### Value at Risk (VaR) Estimation through Monte Carlo Simulation
SOON


## Excel Projects
### A Statistical Approach to Setting Stop-Loss and Take-Profit Levels
The Monte Carlo simulation was utilized to mathematically set stop-loss and take-profit levels for the stocks which were selected in the portfolio. This simulation is a risk management tool which generates a total of 1000 random returns of a stock based on the mean and standard deviation of its two year daily returns. Then, the one percentile and 99 percentile of the randomly generated returns were used to set the stop-loss and take-profit levels. Finally, the data was visualized by creating a normal distribution graph for each stock.

<div align="center">
	<img src="https://github.com/user-attachments/assets/04d47a50-8b3b-43c3-9528-0d64946966fb" width="50%">
</div>


### Portfolio Optimization: Maximizing Sharpe Ratio
The weights of the selected stocks in the portfolio were optimized by using historical data and statisitcal tools. By determining the optimal weights of the stocks using the solver feature in Excel, the standard deviation (risk) was minimzed and the expected return and sharpe ratio of the portfolio were maximized. To further prove that the portfolio was optimized, random weights were assigned to each stock in the portfolio 10,000 times. Next, the portfolios' respective standard deviations and expected returns were calculated. Finally, an efficient frontier was constructed to visualize the 10,000 portfolios' risk to reward possibilites. 

<p align="center">
  <img src="https://github.com/user-attachments/assets/4cfa7ee8-1869-4a12-a20d-a0a3249947e9" width="34%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://github.com/user-attachments/assets/c1590f3d-7511-409e-ab21-88f960b3bf0b425" width="52.5%">
</p>

### Optimizing Inventory Management: Identifying Order Quantity and Reorder Points
The optimal order quantity and reorder point of an inventory were identified by utilizing the Monte Carlo simulation and scenario analysis. A 28 day demand forecast was constructed by utilizing probabilistic assumptions based on the inputs set in the model to determine the total cost (holding cost + stockout cost + order cost) incurred by the respective order quantity and reorder point. To ensure the accuracy of the results that were obtained by the probabilistic assumptions, a Monte Carlo simulation was run 300 times to determine the average total cost of the model. Next, a scenario analysis was conducted to identify the total cost incurred by different order quantities and reorder points. Finally, the order quantity and reorder point that yielded the lowest total cost were deemed as optimal.
<div align="center">
	<img src="https://github.com/user-attachments/assets/b1ff7226-a98d-4b0e-a3bc-7c63983bd985" width="50%">
</div>

