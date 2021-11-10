# Guitar-Quiz-Generator
This program creates simple quizzes for guitar students to test them on their knowledge of the musical notes of each string. 

A frequent issue with guitar players is that although they might be technically sound on the instrument, the theory aspect of the instrument 
is given less importance and players tend to think of the notes that they are playing in terms of fret number rather than the actual musical 
note itself. By knowing the musical note it can only help to build a better musical foundation and a better understanding.

Each section focuses on a particular string (starting from the thinnest string; the 1st string or the high 'e' string) and 4 randomly 
selected frets form the basis of the questions. The program also creates an answer file for quick reference.

The desired number of quizzes is put into a for loop and then a quiz file and an answer file are created with the appropriate name and headings.
We then loop through a list of the strings of the instrument using an enumerate function. Having the index of the string is helpful in naming each
section of the string and the musical note of the string can be passed to a function string_notes() in the string_func.py file. This function
creates a dictionary from the passed string value of the chosen guitar string by pairing the fret numbers with their musical values through 
zipping the numbers 0-11 with the rearranged musical values determined by the passed value of the guitar sttring. With this dictionary created,
it is then down to a random.sample() call to create the basis of the questions and then the questions and their corresponding answers are
written to the relevant files.


