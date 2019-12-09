# IPL-Auctions

Indian is the second largest country in terms of population with 1.27 billion people. And these
people are captured by the fever of cricket and especially the IPL. Yes, cricket is the most loved
sport in India and it is watched, played and witnessed by millions of people. From the children
playing gully cricket in your neighborhood to the national cricket team of India, everyone is
mesmerized by the beauty of this game.
Next year we will witness the 13th edition of Indian Premiere League. Unfortunately, Richard
Madley, the IPL Auctioneer is not available next year. So it is now your responsibility to form the
teams.

Rules

• Every Team can have atleast x and atmost y Overseas Players (not Indian).
• Every team can have atleast x and atmost y bowlers
• Every team can have atleast x and atmost y batsmen.
• Every team can have atleast x and atmost y Wicket Keepers.
• Every team can have atleast x and atmost y all rounders.
• Any player can be included for only 1 Ability. (Example : Shakib can be included either as a
Bowler or All Rounder or Batsman)
• No player can be a part of more than 1 team.
• The team size is 18 members.
• Values of x and y will be specified in the config.txt file (read below)

Input Files :

dataset.txt : contains information of players in the following format

Player Name:Country:Ability:Fees

dataset link : ---

config.txt : contains all the parameters as explained above.

overseas:4:7

bowlers:4:6

batsmen:5:7

wicketkeepers:1:2

allrounders:2:4

teams:8

team_names:

Chennai Super Kings

Delhi Capitals

Kings XI Punjab

Kolkata Knight Riders

Mumbai Indians

Rajasthan Royals

Royal Challengers Bangalore

Sunrisers Hyderabad


Output Files :

Total n files, where n is the number of teams specified in the config.txt fileOne text file for each
team containing player information in the following format.

Chennai Super Kings.txt

Team: Chennai Super Kings

Player 1

Name : Sachin Tendulkar

Country : India

Ability : Batsman

Fees : 700000


Player 2

Name : Virendra Sehwag

Country : India

Ability : Batsman

Fees : 600000
