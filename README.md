# DragonRidersWebBot
The DragonRidersWebBot is a bot enabling to play autoplay dragon handler webbased game.

The high level architecture of the application functionality:

1. Log in using provided by user credentials.
2. Gather all the infomration about the user in-game profile.
3. Display all key topics in readable table for the suer in the console.
4. Avaiability to choose one of few options:
  1. Train your dragon:
     When user chooses to train the dragon will be moved to nex table which will show how many times can train what characteristics of the dragon, then bot will train dragon exact amount of times user desires.
     In case of wrong input the bot will respond with failure message and request to repeat the action or choose other.
  2. Fight with your dragon:
     When user chooses to fight with the dragon new table will be shown with the names of all of user dragons and their stamina level in percentage.
     Then the user will be able to choose which dragons user want to fight with and for each dragon will be able to precise how much stamina user wants to use.
     On top of those two decisions there will be third one to choose between ranked and casual game. Then Bot will sort the dragons into casual and ranked queues, and first fight in casual fights and then ranked ones.
     Additionaly there will be special option "All Dragons/Whole Stamina" which will only enable user to choose between casual and ranked types of fights and then throw all dragons into the fighting pit untill whole stamina is expired.
  3. Send your dragon to expedition:
     User will be able to see the table that will show which dragon is in which state (on expedition and if so for how long) or if is resting.
     Then the option will be provided to chose which resting dragons user want to send to expedition, where, and how much time (intervals of 2 from 2h to 12h).
5. The application can be closed whenever user desires.

v. 0.0.1
