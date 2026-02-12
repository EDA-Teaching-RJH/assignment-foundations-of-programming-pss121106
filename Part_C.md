# Old system Changes Breakdown
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

2. parallel lists

# Dangers of using parallel lists
The main dangers of using parallel lists is that the data could desynchronise as there is nothing keeping the lists together. The lists have no anchor keeping them down an together. If one of the lists is changed or edited without the other lists, then the data inside the lists would be corrupted. 

2. If someone removes the name but not the ID it would corrupt the logic in the code as the ID would be assigned to a different person. Another effect would be the system crashing and not running correctly. An index  error will come up as the system crashes.

3. My code prevented this as I used a shared index variable. When the remove member code is running I have an index() which finds the ID and the name of the persone associated with that ID. 



