# Odoo-Challenge solution for the challenge number 10

<img src="/assets/challenge10.png" width=80% height=80%> 

This is a simple algorithm understanding problem, the password and unaccessible, a series of commands are called and we need to find the key.
Each command reveals a portion of the key, and they can be summed up as:
- print(r(pwd, 0, 4, 1)): print the pwd, starting from index 0, ending in index 4, every one letter.
We can then therefore assume that the first 4 letters of the pwd are:

"e62e"

- print(r(pwd, 4, 20, 2)): print the pwd, starting from index 4, ending in index 20, every 2 letters
Using the previously gained knowledge, we add the information gathered, and so on.

The key for me was:
"e62e91f7a92c049fb80848ade47f659483263907"
