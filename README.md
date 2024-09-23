# Isa_Alnoaimi_Portfolio
Welcome to my portfolio! Below is a summary of the Python and Excel projects I created. Feel free to dive into any project in the Python and Excel folders.
## Python Projects
### [Value at Risk (VaR) Estimation through Monte Carlo Simulation](Python%20Projects/Value%20at%20Risk%20%28VaR%29%20Estimation%20through%20Monte%20Carlo%20Simulation.ipynb)
The Value at Risk (VaR) of a $1,000,000 portfolio that includes 50% equities, 30% bonds, and 20% commodities over a 10-day period was identified. The log returns of each underlying asset were calculated to construct a covariance matrix, which was essential for identifying the portfolio's standard deviation. A Monte Carlo simulation was run 10,000 times to assess the range of the portfolio's potential losses and gains based on specific inputs. Next, a confidence interval of 0.95 was utilized, indicating that there is a 95% confidence that the portfolio losses will not exceed -$72,622 over the 10-day period. Finally, the Monte Carlo simulation was plotted to visualize the VaR.
<div align="center">
	<img src="https://github.com/user-attachments/assets/c779618c-bf7f-42e4-ba91-d8c9a1a9be46" width="50%">
</div>

### [Correlation Analysis of the S&P 500 Sector ETFs](Python%20Projects/Correlation%20Analysis%20of%20the%20S%26P%20500%20Sector%20ETFs.ipynb)
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


### [Portfolio Risk Management: Portfolio Optimization](Excel%20Projects/Portfolio%20Risk%20Management%20-%20Portfolio%20Optimization.xlsx)
The weights of the selected stocks in the portfolio were optimized by using historical data and statisitcal tools. By determining the optimal weights of the stocks using the solver feature in Excel, the standard deviation (risk) was minimzed and the expected return and sharpe ratio of the portfolio were maximized. To further prove that the portfolio was optimized, random weights were assigned to each stock in the portfolio 10,000 times. Next, the portfolios' respective standard deviations and expected returns were calculated. Finally, an efficient frontier was constructed to visualize the 10,000 portfolios' risk to reward possibilites. 

<p align="center">
  <img src="https://github.com/user-attachments/assets/4cfa7ee8-1869-4a12-a20d-a0a3249947e9" width="34%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://github.com/user-attachments/assets/c1590f3d-7511-409e-ab21-88f960b3bf0b425" width="52.5%">
</p>

### [Optimizing Inventory Management: Identifying Order Quantity and Reorder Points](Excel%20Projects/Optimizing%20Inventory%20Management%20-%20Identifying%20Order%20Quantity%20and%20Reorder%20Points.xlsx)
The optimal order quantity and reorder point of an inventory were identified by utilizing the Monte Carlo simulation and scenario analysis. A 28 day demand forecast was constructed by utilizing probabilistic assumptions based on the inputs set in the model to determine the total cost (holding cost + stockout cost + order cost) incurred by the respective order quantity and reorder point. To ensure the accuracy of the results that were obtained by the probabilistic assumptions, a Monte Carlo simulation was run 300 times to determine the average total cost of the model. Next, a scenario analysis was conducted to identify the total cost incurred by different order quantities and reorder points. Finally, the order quantity and reorder point that yielded the lowest total cost were deemed as optimal.
<div align="center">
	<img src="https://github.com/user-attachments/assets/b1ff7226-a98d-4b0e-a3bc-7c63983bd985" width="50%">
</div>

