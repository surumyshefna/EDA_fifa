# -*- coding: utf-8 -*-
"""EDA fifa FA3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EMYCjhFjtlP-fnc2kV8ffpteziieq0gg

Using the below dataset of fifa players dataset. Perform Exploratory data analysis and find the following insights:
1.Which country has the most number of players (score :1)
2.Plot a bar chart of 5 top countries with the most number of players. (score :1)
3.Which player has the highest salary? (score :1)
4.Plot a histogram to get the salary range of the players. (score :1)
5.Who is the tallest player in the fifa? (score :1)
6.Which club has the most number of players? (score :1)
7.Which foot is most preferred by the players?Draw a bar chart for preferred foot (score :1)

In addition,
Data Story
Describe the insights you gained from each question.  (score :2)
Timely submission (score :1)
Total score : 10
Dataset :
https://drive.google.com/file/d/10oyIT1KPdwUqeU9-2LX0xE5-ZytNn9su/view?usp=share_link
"""

import pandas as pd
import numpy as np

# Load the dataset
fifa_data = pd.read_csv("//content//drive//My Drive//dataset//fifa_data.csv")

fifa_data

fifa_data.info()

"""##1.Which country has the most number of players"""

# Find the country with the most number of players
country_counts = fifa_data['Nationality'].value_counts()
most_players_country = country_counts.idxmax()
most_players_country_count = country_counts.max()

most_players_country, most_players_country_count

"""ENGLAND has the most number of football players

##2.Plot a bar chart of 5 top countries with the most number of players.
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Get the top 5 countries with the most players
top_5_countries = country_counts.head(5)

# Plot the bar chart
plt.figure(figsize=(10, 6))


top_5_countries.plot(kind='bar', color='skyblue')
plt.title('Top 5 Countries with the Most Number of Players')
plt.xlabel('Country')
plt.ylabel('Number of Players')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.show()

"""England has 1662 players

Germany has 1198 players

Spain has 1072 players

Argentina has 937 players

France has 914 players

3.Which player has the highest salary?
"""

fifa_data['Wage'] = fifa_data['Wage'].astype(str).str.replace('€', '').str.replace('K', '000')
fifa_data['Wage'] = fifa_data['Wage'].astype(float)
fifa_data['Name'][fifa_data['Wage']==fifa_data['Wage'].max()]

Max_sal=fifa_data['Wage'].max()
index_sal=fifa_data['Wage'].idxmax()
Player_sal=fifa_data.loc[index_sal,"Name"]
print("\n The highest paid Player is",Player_sal,"\n Salary is €",Max_sal,"K")

"""##4.Plot a histogram to get the salary range of the players.

"""

plt.figure(figsize=(10, 6))
plt.hist(fifa_data['Wage'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Players' Salaries")
plt.xlabel('Salary (K)')
plt.ylabel('Number of Players')
plt.grid(True)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()

Ht=fifa_data.sort_values(by=["Wage"], ascending=False)
Ht[['Name', 'Wage']]
plt.hist(fifa_data['Wage'])
plt.title('Salary Range of the Fifa Player')
plt.xlabel('Salary(k)')
plt.ylabel('Number of Players')
plt.grid(True)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()

"""Most of the players are getting the salary around 50000.

##5.Who is the tallest player in the fifa?
"""

ht=fifa_data[['Name','Height']]

SORTht=ht.sort_values(by='Height',ascending =False)
sh=SORTht.head()
sh

sns.scatterplot(x='Name',y='Height',data=sh,color='olive',marker="o")
plt.title('PLAYERS WITH GREATEST HIGHT',color='purple')
plt.xlabel('NAME',color='b')
plt.ylabel("HEIGHT",color="b")
plt.show()

"""T. Holý and D. Hodzic are heighest among FIFA players.Both T. Holý and D. Hodzic have 6'9 feet height.

##6.Which club has the most number of players?
"""

club=fifa_data['Club'].value_counts()
c=club.head(30)
c

sns.lineplot(data=c,color='cyan',marker='>')
plt.title('Club - No of players GRAPH',color='purple')
plt.xticks(rotation=90)
plt.show()

"""From FIFA dataset we can see that 26 club has the most number of players.Each 26 club contains 33 players.

Name of that 26 club is given below

1.FC Barcelona

2.Valencia CF

3.Fortuna Düsseldorf

4.Cardiff City

5.Rayo Vallecano

6.CD Leganés

7.Frosinone

8.Newcastle United

9.Southampton

10.Burnley

11.Eintracht Frankfurt

12.Wolverhampton Wanderers

13.TSG 1899 Hoffenheim

14.Everton

15.AS Monaco

16.RC Celta

17.Empoli

18.Manchester City

19.Manchester United

20.Borussia Dortmund

21.Real Madrid

22.Atlético Madrid

23.Tottenham Hotspur

24.Chelsea

25.Liverpool

26.Arsenal

##7.Which foot is most preferred by the players?Draw a bar chart for preferred foot
"""

# Find the most preferred foot
preferred_foot_counts = fifa_data['Preferred Foot'].value_counts()
preferred_foot_counts

# Plot the bar chart
most_preferred_foot = preferred_foot_counts.idxmax()
most_preferred_foot_count = preferred_foot_counts.max()
plt.figure(figsize=(8, 6))
preferred_foot_counts.plot(kind='bar', color='skyblue')
plt.title('Preferred Foot of Players')
plt.xlabel('Preferred Foot')
plt.ylabel('Number of Players')
plt.xticks(rotation=0)
plt.show()

most_preferred_foot, most_preferred_foot_count

"""From above visualization, We can conclude that most of the players prefer their right foot to kick the ball. Near 14K(13948) players uses their right foot.

Left foot is preferred by only 4211 players.

##Data Story
Describe the insights you gained from each question.

1. **Country with Most number of Players: **
---

The country with the most number of players is England, having 1662 players.
"""



"""**2. 5 top countries with the most number of players.**

---

England has 1662 players

Germany has 1198 players

Spain has 1072 players

Argentina has 937 players

France has 914 players

**3. Highest Salary Player:**

---


The player with the highest salary is L. Messi with a salary of € 565000.0 K. This reflects the player's market value and demand.

**4. salary range of the players**

---
Most of the players are getting the salary around 50000.

**5.Who is the tallest player in the fifa?**

---

T. Holý and D. Hodzic are heighest among FIFA players.Both T. Holý and D. Hodzic have 6'9 feet height.

**6.Which club has the most number of players? **

---

From FIFA dataset we can see that 26 club has the most number of players.Each 26 club contains 33 players.

Name of that 26 club is given below

1.FC Barcelona

2.Valencia CF

3.Fortuna Düsseldorf

4.Cardiff City

5.Rayo Vallecano

6.CD Leganés

7.Frosinone

8.Newcastle United

9.Southampton

10.Burnley

11.Eintracht Frankfurt

12.Wolverhampton Wanderers

13.TSG 1899 Hoffenheim

14.Everton

15.AS Monaco

16.RC Celta

17.Empoli

18.Manchester City

19.Manchester United

20.Borussia Dortmund

21.Real Madrid

22.Atlético Madrid

23.Tottenham Hotspur

24.Chelsea

25.Liverpool

26.Arsenal

**7. Preferred Foot:**

---

The most preferred foot among players is Right, with
13948 players favoring it. The bar chart illustrates the preference between left and right foot, showing a dominant trend.
"""