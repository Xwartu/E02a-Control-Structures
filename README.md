
# E02a-Control-Structures

Let's start experimenting with some Python code! This is a set of exercises for MSCH-C220; they should give you the tools to help build your first game.
 
This exercise assumes that you have already installed Python, GitHub Desktop, and VS Code, and that you have already created a GitHub account. If that is not the case, please refer to previous exercises.

This repository contains several files that you will need to alter to complete the assignment. Fork this repository (instructions below) and edit the files. Commit and push the changes back to GitHub and turn in the URL to your repository on Canvas.

Comments in Python are marked by a # sign (for single-line comments) or three matching quotation marks (''' or """) if a comment requires more than one line. They should also appear in a different color in VS Code. The Python Interpreter ignores comments, so you can safely include any information you want there.

*If you wish your exercise to be graded, please edit the LICENSE file (add the current year and your name).*

Edit README.md to answer the following questions:

- Open main01.py. Before running it, what do you expect this program to do?
  #  I expect it to print and then ask for a color.
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.
  - What do you think the program did with what you typed in answer to the question?
  # There was indeed a print in the terminal, and it then asked for an input. It did nothing with the answer since there was no more code and it wasn't stored in a variable.
- Open main02.py. Before running it, describe how this is different than main01.py.
  # This is differnt from main01.py in that it will now store the value and then return the value through a print command. 
  - What do you think the color = input() will do? 
  # Store the value entered by the human into color. 
  - Run the program in the terminal and answer the question. Did the program do what you expected?
  # Yes
- Open main03.py. Before running it, describe how this is different than main02.py.
  # This is different from main02.py in that there is now a code block through the if - else statement.
  - What is happening on lines 9–12?
  # The computer is checking to see if the condition specified is met. If it isn't it will follow the structure outlined in the else code block. 
  - Why are lines 10 and 12 indented?
  # The Syntax of Python dictates that if else statements are followed with identations so the computer can distunguish what code to do from the other code.
  - Run the program and answer the question. What happens if you don’t capitalize Red?
  # It doesn't recgonize that was the correct answer because Python is case sensitive. 
  - What does this tell you about "color"?
  # Color has to be astring otherwise it can't compare it to the outlined string, and it has to be capitalized for this specfic code to recognize it. 
- Open main04.py. Before running it, describe how this is different than main03.py.
  # It's mostly the same with the exception of the new or statment in the if statement.
  - What problem is this trying to solve?
  # It's trying to solve the case-sensitive issues of Python. 
  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
  # It will then fail because it then becomes one of the two cases outlined in the if statement.
- Open main05.py. What do you expect line 9 to do?
  # I expect it try and make color lowercase, but I do not think it will work. 
  - What problem is it trying to solve?
  # It is still trying to solve the captialization issues present in previous "main.py"s.
  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
  # It fails again, but I was wrong about the lowercase command not working. I thought it looked like it was in the wrong area. 
  - Open main06.py. How is line 9 different than in main05.py?
   # There is a .strip added to the color.lower().
   - What would you guess .strip() is doing?
   # Stripping away the white space from the input. 
   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
   # Yes, (255, 000, 000), #ff0000, or just putting spaces between r e d. 
 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?
   # There is now an elif statment added to the other two statements, giving another possible set of insturctions to be followed through. 
   - What is happening on line 12?
   # If the user inputs pink the computer will tell them they are close to the right answer, but did not actual meet the condition in the if statement/original intent of the question. 
   - Run the program and answer the question.
 - Open main08.py. What is the purpose of line 9?
   # To continually repeat the question until the answer is correctly give, effectively giving unlimited tries.
   - Why are lines 10–17 indented?
   # The while loop needs to know what code to continually run over and over and the indentation seperates that code from the rest. 
   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
   # It would give an IndentationError
   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
 - Open main09.py. What is happening on line 13?
   # There is a count variable that ccontinually redfines what count means using the previous count variable to make the new one
   - What is the purpose of “count”?
   # To keep track of how many times the loop ran/how many attempts it took to guess correctly. 
   - What is happening on line 22?
   # For me there was nothing, but there was something on 21, so I'll assume it was that. That is a normal print statement using a different way to include strings into other strings after the fact. 
   - Run the program.
 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).
 - *Extra credit:* open main11.py. What is happening on lines 6-11?
 # There is a function being defined so that it can be called multiple times without having to repeat all the code each time. It's paranthesis nessicatates the variable last_color. In the function the possible choice of all the colors lies in a list format and then uses the random module to choose a random color from the list, having stored the last color uused in the varaible last_color, if it repeats then the while loop causes another color to be chosen until it's a new color and then c is returned to the new value of last_color which will then become match_color allowing the code to function fully. 
  
Commit your changes and push them back to the repository.
 

---

Instructions for forking this repository:
 
Log into your account on [github.com](https://github.com)

Go to the [exercise template page](https://github.com/BL-MSCH-C220-S20/E02a-Control-Structures) on GitHub

There is a button in the top right corner of the page labeled "Fork". Press that now

This will create an independent copy of this repository in your account that you can control and edit

Go to your GitHub home page, and select the new E02a-Control-Structures repository

On that page, you will see a green button labeled "Clone or download". Press that now. You will see a drop down box. Press the "Open in Desktop" button.

This should launch GitHub Desktop. It will ask you for a location (on your computer) where the repository may be cloned (downloaded). Choose a location that will be easy for you to find, and press the blue "Clone" button.

Once GitHub Desktop has cloned (downloaded) the code, it will be responsible for keeping the code on your local computer synchronized with the repository in your GitHub account. Now, open Visual Studio Code, and choose File->Open. Find the folder of the cloned repository and select Open.

In the left (File Explorer) panel, you should see a list of files that comprise this repository

First, edit the file called LICENSE. Replace year and name with the current year and your name. Save this file

Then open README.md. Feel free to remove any extraneous information, and then answer the questions posed in the file. You can add your answers after each question

When the time comes for you to run any of the python files, you can do so by clicking the green arrow in the top right corner of the window or by right-clicking on the code and selecting "Run Python File in Terminal". The results will appear at the bottom. If you don't see "Run Python File in Terminal" in the contextual menu, that is because VS Code doesn't have the Python extension installed. You can do that here: [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

When you are done editing the files, return to GitHub Desktop. In the left panel, you should see a list of the files that have changed

At the bottom of the leftmost area, you should see a text box labeled "Summary (required)". Add a message that describes what you have done; these messages are typically stated in the active-present tense. For example, "Updates the LICENSE, README.md, and completes the assignment." Push the blue "Commit to master" button

In the top bar of the window, you should see a button that is labeled "Push origin", push that now

Check out your page on GitHub. You should see the changes you made reflected there, Repeat steps 10 through 16 as necessary

When you are satisfied with your efforts, turn in a URL to your repository on Canvas

---
If you try to push your changes, and you receive a permission error, it is likely that you are trying to edit the BL-MSCH-C220-S20 copy of the repository rather than your own. Make sure you don't skip the step of forking your own copy and cloning that.

---

The grading criteria will be as follows:
 
[1 point] Repository contains a description of the project in README.md

1 point will be awarded for answering the questions associated with each of the files

10 points total (+2 points extra credit)
