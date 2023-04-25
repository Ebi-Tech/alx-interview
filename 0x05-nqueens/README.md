# Queens

The program checks if the user called the program with the correct number of arguments, and if the argument is an integer greater or equal to 4. If the argument is invalid, it prints an error message and exits with status 1.
The program defines a function is_safe which takes a chess board, a row and a column, and returns True if it is safe to place a queen at that position, and False otherwise. The function checks if there is no other queen on the same row, on the same diagonal or on the same anti-diagonal as the given position.
The program defines a recursive function solve which takes a chess board, a column, and a list of solutions, and adds all possible solutions to the list. The function works by trying to place a queen on every row of the current column, and recursively calling itself with the updated board and the next column. If a solution is found, it is added to the list of solutions.
The program initializes a chess board with all squares set to 0, and calls the solve function with the board, the first column, and an empty list of solutions. The solve function adds all solutions to the list of solutions.
Finally, the program prints every solution in the list, one solution per line, in the format specified in the problem statement.
Here's an example of how to run the program:
	
	$ ./nqueens.py 4
	0100,0001,1000,0010
	0010,1000,0001,0100

	$ ./nqueens.py 5
	00001,10000,01000,00100,00010
	00010,00100,10000,01000,
