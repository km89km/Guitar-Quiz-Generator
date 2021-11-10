#! python3
# A Quick quiz generator for guitar students to help them think about and memorise the musical notes
# of the guitar. Inspired by Al Sweigart's 'Automate the boring stuff'.
import random
# import string_notes function to create a dictionary for the desired string.
from string_func import string_notes
# Create the desired number of Quizzes and their corresponding answer files.
for quiz_number in range(#NUMBEROFQUIZZES):
    quiz_file = open(f'Quiz{quiz_number+1}.txt', 'w')
    quiz_file.write((' ' * 20) + f'Guitar Note Quiz (Form {quiz_number+1})\n\n')
    quiz_file.write('Write the corresponding musical note from the fret and string given. '
                    '(Flat and Sharp equivalents are accepted.)\n\n')

    answer_file = open(f'Answers{quiz_number+1}.txt', 'w')
    answer_file.write(f'Answers {quiz_number+1}\n\n')

    # Have a section for each of the 6 strings of the guitar.
    strings = ['E', 'B', 'G', 'D', 'A', 'E']
    # Using enumerate will iterate through the string letters but also give an index to help with the
    # string number to create a heading for each section for each string.
    for index, string in enumerate(strings):
        # index of strings list starts at 0 and actual strings begin from 1.
        string_number = index + 1
        # Some conditionals to help decide the correct suffix to create the correct ordinal.
        if string_number == 1:
            quiz_file.write(f'. {string_number}st String\n\n')
            answer_file.write(f'. {string_number}st String\n\n')
        elif string_number == 2:
            quiz_file.write(f'. {string_number}nd String\n\n')
            answer_file.write(f'. {string_number}nd String\n\n')
        elif string_number == 3:
            quiz_file.write(f'. {string_number}rd String\n\n')
            answer_file.write(f'. {string_number}rd String\n\n')
        else:
            quiz_file.write(f'. {string_number}th String\n\n')
            answer_file.write(f'. {string_number}th String\n\n')
        # Use function to create a dictionary of current string.
        string_dict = string_notes(string)
        # Randomly select 4 different frets for the basis of the questions.
        frets = random.sample(range(0, 22), 4)
        for fret in frets:
            quiz_file.write(f'  . {fret} = \n')
            # After the 11th fret the notes repeat themselves so rather than having extra information in the
            #  dictionary we can simply subtract 12 for the same result.
            if fret > 11:
                fret -= 12
            answer_file.write(f'  . {string_dict[fret]}\n')
        answer_file.write('\n')
        quiz_file.write('\n')
    quiz_file.close()
    answer_file.close()
