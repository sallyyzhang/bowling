
Create Game
POST /api/games/
Response
Success Response 201
{
   "success": true,
   "data": {
       "name": "My bowling game, new",
       "gameId": 1,
       "isComplete": false,
       "players": []
   }
}


Create Player
POST /api/players/
Response 
Success Response 201
{
   "success": true,
   "data": {
       "gameID": 31,
       "name": "Example",
       "players": [
           {
               "name": "David",
               "score": 92,
               "frame1": {
                   "firstRoll": [
                       7,
                       4,
                       2,
                       1,
                       3,
                       5
                   ],
                   "secondRoll": [
                       8,
                       9,
                       6
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "mutable": true,
                   "score": 9
               },
               "frame2": {
                   "firstRoll": [
                       10,
                       1,
                       2,
                       3,
                       4,
                       5,
                       6,
                       7,
                       8,
                       9
                   ],
                   "secondRoll": [],
                   "thirdRoll": [
                       -1
                   ],
                   "mutable": true,
                   "score": 29
               },
               "frame3": {
                   "firstRoll": [
                       4,
                       2,
                       1
                   ],
                   "secondRoll": [
                       10,
                       3,
                       5,
                       6,
                       7,
                       8,
                       9
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "mutable": true,
                   "score": 43
               },
               "frame4": {
                   "firstRoll": [
                       7,
                       4,
                       2,
                       1
                   ],
                   "secondRoll": [],
                   "thirdRoll": [
                       -1
                   ],
                   "mutable": true,
                   "score": 47
               },
               "frame5": {
                   "firstRoll": [],
                   "secondRoll": [],
                   "thirdRoll": [
                       -1
                   ],
                   "mutable": true,
                   "score": 47
               },
               "frame6": {
                   "firstRoll": [
                       7,
                       4,
                       2,
                       1,
                       3,
                       5,
                       6
                   ],
                   "secondRoll": [
                       8,
                       9
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "mutable": true,
                   "score": 56
               },
               "frame7": {
                   "firstRoll": [
                       10,
                       1,
                       2,
                       3,
                       4,
                       5,
                       6,
                       7,
                       8,
                       9
                   ],
                   "secondRoll": [],
                   "thirdRoll": [
                       -1
                   ],
                   "mutable": true,
                   "score": 80
               },
               "frame8": {
                   "firstRoll": [
                       7,
                       4,
                       2,
                       1,
                       3
                   ],
                   "secondRoll": [],
                   "thirdRoll": [
                       -1
                   ],
                   "mutable": true,
                   "score": 84
               },
               "frame9": {
                   "firstRoll": [
                       1,
                       4,
                       2,
                       3
                   ],
                   "secondRoll": [
                       10,
                       5,
                       6,
                       9
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "mutable": true,
                   "score": 92
               },
               "frame10": {
                   "firstRoll": [
                       7,
                       4,
                       2,
                       1,
                       3
                   ],
                   "secondRoll": [
                       8,
                       5,
                       6
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "mutable": true,
                   "score": 100
               }
           }
       ],
       "isComplete": false
   }
}
 


Post frame
POST /api/frames/
Success response 201
{
   "success": true,
   "data": {
       "frame1": {
           "firstRoll": [
               3,
               5,
               7
           ],
           "secondRoll": [
               1,
               8
           ],
           "thirdRoll": [
               -1
           ],
           "score": 5,
           "mutable": true
       }
   }
}



getGame
GET /api/games/<int:game_id>/
{
   "success": true,
   "data": {
       "gameID": 4,
       "name": "My bowling game",
       "players": [
           {
               "name": "Berk",
               "score": 5,
               "frame1": {
                   "frame1": {
                       "firstRoll": [
                           3,
                           5,
                           7
                       ],
                       "secondRoll": [
                           1,
                           8
                       ],
                       "thirdRoll": [
                           -1
                       ],
                       "mutable": true,
                       "score": 5
                   }
               },
               "frame2": {
                   "firstRoll": [
                       -1
                   ],
                   "secondRoll": [
                       -1
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "score": 0,
                   "mutable": true
               },
               "frame3": {
                   "firstRoll": [
                       -1
                   ],
                   "secondRoll": [
                       -1
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "score": 0,
                   "mutable": true
               },
               "frame4": {
                   "firstRoll": [
                       -1
                   ],
                   "secondRoll": [
                       -1
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "score": 0,
                   "mutable": true
               },
               "frame5": {
                   "firstRoll": [
                       -1
                   ],
                   "secondRoll": [
                       -1
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "score": 0,
                   "mutable": true
               },
               "frame6": {
                   "firstRoll": [
                       -1
                   ],
                   "secondRoll": [
                       -1
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "score": 0,
                   "mutable": true
               },
               "frame7": {
                   "firstRoll": [
                       -1
                   ],
                   "secondRoll": [
                       -1
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "score": 0,
                   "mutable": true
               },
               "frame8": {
                   "firstRoll": [
                       -1
                   ],
                   "secondRoll": [
                       -1
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "score": 0,
                   "mutable": true
               },
               "frame9": {
                   "firstRoll": [
                       -1
                   ],
                   "secondRoll": [
                       -1
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "score": 0,
                   "mutable": true
               },
               "frame10": {
                   "firstRoll": [
                       -1
                   ],
                   "secondRoll": [
                       -1
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "score": 0,
                   "mutable": true
               }
           }
       ],
       "isComplete": false
   }
}
 

deleteGame
DELETE /api/games/<int: game_id>/
{
   "success": true,
   "data": {
       "name": "My bowling game, new",
       "gameId": 1,
       "isComplete": false,
       "players": [
           {
               "name": "Sally",
               "score": 5,
               "frame1": {
                   "firstRoll": [
                       3,
                       5,
                       7
                   ],
                   "secondRoll": [
                       1,
                       8
                   ],
                   "thirdRoll": [
                       -1
                   ],
                   "score": 5,
                   "mutable": true
               }
           }
       ]
   }
}


________________________________________________________________________________________
Routes are self-descriptive and titled with what they should do.
Database has classes for Game, Frame, and Player Players and games have a 1-to-many relationship, because players can play more than one game.
There are multiple frames in a game
