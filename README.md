# N-Queens-Game
It's a university project of Artificial intelligence course
Problem Description:
The "N-Queens Problem" is to arrange the n queens on a n × n chessboard so that none of them can attack 
one another by being in the same row, column, or diagonal.
Distinguishing features of Our project:
In our project, we have defined different functions and class.
1. Screen1():
This function creates the first screen of the game which shows two buttons which will ask the user 
“Get Help” or “Start”.
2. Screen2():
This function withdraws the previous window(screen) and opens only if the user selects “Get Help” 
from the first screen. Here, the user will get “Instructions” which will help better understand the 
game and then at the bottom of the screen the user will find a button “Got It” which will take the 
user to the next screen.
3. Screen3():
This screen opens when the user clicks the “Got It” button from screen-2 or the “Start” button 
directly from the screen-1. It destroys the screen-2 and creates another screen which will ask the 
user for the number of queens which the user is willing to play with.
4. get_input ():
This function takes the entry for the number of queens the user has entered and passes the 
entered quantity to the main screen function which will create the board according to the entered 
value.
5. Main ():
This is the main functions which creates the main board where the actual game will be played. 
This function calls two more functions within itself “create_board(n)” and 
“solve_n_queens(board)”.
ARTIFICIAL INTELLIGENCE SEMESTER PROJECT REPORT
NED University of Engineering & Technology 
6. Create_board (n):
This function is called by the main () function. It takes one argument “n” which indicates the 
number of queens which will be played in the game. It actually initializes the variable “board” 
which is a list. Later on, rows are appended to the list making it a nested list and help it creating a 
playing board.
7. solve_n_queens (board):
This function is also called by the main () function. Here, it is taking one argument which is “board” 
which is actually a variable that contains the quantity of queens. This function itself calls another 
function named as “problem_util (board, col)”.
8. problem_util (board, col):
This function uses a built-in function of Pygame “time.clock ()” which helps in the delay of 
displaying screen. This function again takes help from two more functions “is_safe ()” and “draw 
()”. Both of them help it to check if the queen is placed in the right position according to the 
game’s requirement and “draw ()” inserts the queen’s image on the right place where the 
algorithm tells it to place. 
9. Is_safe ():
This function facilitates the game to decide whether it is safe to place the queen in a particular 
place or not. It checks the upper and lower diagonals and also rows and make sure that no queen is 
placed on those positions otherwise it will return false and wont place any queen. If the functions 
return True then the function indicates that it is now safe for the queen to place here.
10. Draw ():
This function is called by problem_util () function. It places the image of queen whenever the 
is_safe () function returns True otherwise it fills the cell (block) with white color when no queen 
can take place.
11. Btn ():
This function is customized and fashioned according to the game. This function is utilized in all the 
buttons in the entire game.
ARTIFICIAL INTELLIGENCE SEMESTER PROJECT REPORT
NED University of Engineering & Technology 
12. Class BulletLabel:
This is a class implementation for all the Labels in the game. It is used for the customization of the 
text and labels.
Flow of the project including Class Diagram:
• The flow starts from the first screen where the user will be asked to select one of the two options 
(buttons) and the user will click the button as per their requirement. 
ARTIFICIAL INTELLIGENCE SEMESTER PROJECT REPORT
NED University of Engineering & Technology 
• The user can go either with the “Start” button or “Get Help” button.
• If the user chooses the “Start” button then they will be directed to the window where they will start 
play right then.
• But if the user clicks the “Get Help” button then they will land on the screen which will instruct 
them and give them a better guide of how this game works. 
ARTIFICIAL INTELLIGENCE SEMESTER PROJECT REPORT
NED University of Engineering & Technology 
• After getting the better understanding of the game, they will start the game.
• A new screen will be opened which will ask the user for the number of queens which the user will 
be willing to play with.
• After selecting the number of queens, a huge number of classes and functions will begin to execute 
and the AI with the help and implementation of the “Backtracking Algorithm” will start playing the 
n-queen game on the board which will be created by one of the functions mentioned above.
• The mentioned functions will check the queen’s position and will place the queen which will not 
come in upper and lower diagonal and in the same row of the other queen.
• This checking and placing of queens will be continued till all the queens are placed on their right 
positions.
Most challenging part while working on the project:
The implementation of the backtracking algorithm was the most challenging part for all the group 
members. It was creating some bugs but later on, the whole group studied the algorithm again and found 
some syntax errors and fixed it.
New Thing Learnt in Python while working on the project:
The entire group got a terrific introduction to exploring more Python libraries and pre-built modules. 
Turtle, Tkinter, Pygame, and many more were carefully examined, but Tkinter and Pygame are the 
foundation of the game.
