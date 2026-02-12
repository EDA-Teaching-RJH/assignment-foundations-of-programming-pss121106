Old system Changes Breakdown
I will be explaining the chages that I made to the old system to allow it to run without crashing.
1. The first bug I fixed was on line 16 where I added a += 1 inside a while loop to stop a never finishing loop.
2. The second bug was on line 28 where I changed the colon to a compartor. From opt : "1" to opt == "1".
3. The next change that I made was on line 34 where I changed an indented elif statement.
4. On line 34 I changed the range(10) to (len(n)) to fix the index error.
5. On line 26 I changed another basic bug of changing a comparator to a operator.
6. On line 57 I changed the code as it showed and ran that commander is always true. I fixed this by changing the code from if rank == "Captain" or "Commander": to if rank == "Captain" or rank == "Commander":. I added that rank == to fix the bug.
7. On line 59 I changed the print( + count) to str(count) as before the change the code was trying to add a number to the string. The str is a string converter to change the variable.
8. The last change that I found in the old system was that there were no parenthesis at the end of the code and they are neccessary to execute the code.
9. My ninth Change is adding an if __name__ == "__main__": at the end of the code as it allows the code to be controlled exactly when it runs. It also separates the definitions of the functions from the execution.

I only found 9 bugs in the old system but it worked correctly without crashing.  
