###Final Project
----

####Find the unique and total artist count in a survey dataset. 


1. Download Data File (original fils is a csv), then upload into database/airtable via SQL

respondent ID | name | Age | zipcode | Favorite Music Artist
---| ---- | ---- | ---- | ---- 
bigint | string | int | int | huge text string = "My favorite artist is Fetty Wap because I cannot understand any of his lyrics. Taylor Swift is good because shes cute. Beyoncé is queen."

2. Import csv/SQL table into python

3. turn each respondent/row into an object in a class? 

4. turn text box into one string: 

5. remove punctuation, capitalizaiton, symbols, spaces

6. Count number of unique music artists listed, find the strongest correlated word with each artist, find sentiment of each artist/text entry 

7. Create new columns for each new variable in SQL table

respondent ID | name | Age | zipcode | Favorite Music Artist | Favorite Music Artist String | Unique Artist(s) and Count | Sentiment Value | Most common collacated word
---| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
bigint | string | int | int | huge text string = "My favorite artist is Fetty Wap because I cannot understand any of his lyrics. Taylor Swift is good because shes cute. Beyoncé is queen." | myfavoriteartistisfettywapbecauseicannotunderstandanyofhislyricstaylorswiftisgoodbecausesheiscutebeyoncisqueen' | [ [fettywap, 1], [taylorswift, 1], [beyonc, 1] ] | .567 | [ [fettywap, 'favorite'], [taylorswift, 'cute'], [beyonc, 'queen'] ] 

8. Summarize survey data by repondent age and zip and gender. 

####*Potential Errors:*
- Only count each artist per row once, artist may be listed multiple times...should only count artist once per row
