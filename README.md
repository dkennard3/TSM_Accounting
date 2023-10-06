# TSM_Accounting
A series of Python scripts that take exported TradeSkillMaster .csv file(s) as input and aggregates the csv data into high-level summaries.
Multiple formats can then be used to visualize this high-level data.
## Features
* converts csv data from TSM into SQL 'insert' statements
* SQL 'insert' statements are created with additional instructions for initializing an SQL table using SQL syntax
* works with 5 types of exchanges available from TSM exports:
    * Auction House Sales
    * Auction House Purchases
    * Player-Trading Sales
    * Player-Trading Purchases
    * NPC-Trading Expenses
* optional feature for visualizing csv exports generated by custom user-aggregated SQL views (such as PostgreSQL) produceds 'pretty' tables on user's terminal


