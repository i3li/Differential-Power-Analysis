# Differential Power Analysis

In this project I use [Power analysis - Wikipedia](https://en.wikipedia.org/wiki/Power_analysis) to guess the length of a password stored in plain text. Most string comparison algorithms check for the length of the strings before comparing them (if two strings are of different lengths, then no need to compare characters). Therefore, comparing two strings with different lengths is faster than comparing two strings with the same length. We coluld use this information to guess a string length. 

**The same method can be used to guess passwords stored in plain text. When we compare two strings we could know if they have a common prefix or not by analyzing the execution time.**



Inspired by this amazing video: [Intro to Hardware Security -- Nate Graff](https://www.youtube.com/watch?v=6KHbTpudQnk&t=2180s).

---

## Usage

Just run `cracker.py` and it will output the guessed length of the password stored at `login_simulator.py`.

**If the guess is wrong, then maybe changing these two parameters -in the `cracker.py` file- would help:**

1. `number`: at the 19th line, `exec_time = timeit.timeit(stmt, setup, number=100)`

2. `repeats`: at the 24th line, `repeats = 100` 

Of course figuring out good parameters could be automated.


