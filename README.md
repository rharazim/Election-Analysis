# Election-Analysis
Module 3 Election Analysis 
## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.
  1. Calculate the total number of votes cast.
  2. Get a complete list of candidates who received votes.
  3. Calculate the total number of votes each candidate received.
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.10, Visual Studio Code version 1.60.2

## Analysis Summary
The analysis of the election show that:

- There were 369,711 votes cast in the election.

- The counties in which votes were cast were:
  - Jefferson
  - Denver
  - Arapahoe

- The distribution of votes from each county was:
  - Jefferson accounted for 10.5% of the vote with 38,855 votes.
  - Denver accounted for 82.8% of the vote with 306,055 votes.
  - Arapahoe accounted for 6.7% of the vote with 24,801 votes.

- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
  - Diana DeGette received 73.8% of the vote with 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.

- The winner of the election was:
  - Diana DeGette who received 73.8% of the vote with 272,892 votes.

## Challenege Overview
Our initial audit summarized the candidates and their performance in this election. We counted the votes for each candidate, got their percentage share of the total vote count and declared a winner based on popular vote. However, the Colorado Board of Elections wanted some additional data to aid in the audit. They asked us to identify the counties involved in the election and find out which had the largest voter participation. We found that over 82% of votes came from Denver county. 

## Challenge Summary
The purpose of writing code to do this analysis rather than tallying the data by hand is that it is a repeatable process that has been optimized for future use. So, the Colorado Board of Elections should try to apply and adapt this code to be used for other Colorado elections. The code's use of "for" loops allows for any amount of possible candidates. If, however, there were too many candidates in the final printed analysis, we could add an "if" statement that could filter out any candidates that received less than 1% of the total vote for the final print. We could even take this code further and analyze each candidates' performance in each county to see which counties were more supportive of certain candidates. This could help assess county voter leanings and preference. 
