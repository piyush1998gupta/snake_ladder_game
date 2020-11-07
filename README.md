# snake_ladder_game
 Automatic Snake ladder game showing each move taken by each player
 
# Read the documentation for depth knowledge of game and board

 ### ----------Board indexing Format how giti moves ---------
   eg :-  6*6
        36 35 34 33 32 31 
        
        25 26 27 28 29 30 
        
        24 23 22 21 20 19
        
        13 14 15 16 17 18
        
        12 11 10 9  8  7
  
  home  1  2  3  4  5  6
### ----------------------------------------


   value at particular

 -1 denotes no snake or ladder at that position
 
 value: denotes rather there is snake or ladder
 
  if value is greater than index than ladder
  
  if value is less than index than snake

 eg:

 ### snake - (34,16) , (20,3)
 
### ladder - (5,23) , (10,32)

 -1 -1 16 -1 -1 -1
 
 -1 -1 -1 -1 -1 -1
 
 -1 -1 -1 -1  3 -1
 
 -1 -1 -1 -1 -1 -1
 
 -1 -1 32 -1 -1 -1
 
 -1 -1 -1 -1 23 -1
 
 # Rules
  ### 1 . player open its gits only on 1 or 6 
  ### 2. player gets another chance when it gets 6 on dice or cuts the git of another player
  ### 3 player which giti cutted move to home and start from the beginnig
