qeustions = [
    ["""Command for new folder in mac ?
    2. Makedir\n
    3. dir\n
    4. ls\n""", '1'],
    ["""define a text ?
    1. single quate\n
    2. double quate\n
    3. single and double quote\n
    4. text\n""", '3'],
    ["""Transfer number to string ?
    1. float\n
    2. str\n
    3. string\n
    4 .text\n""", '2'],
    ["""to compare a to b ?
    1. use =\n
    2. use ==\n
    3. use !=\n
    4. use <>\n""", '2'],
    [""" Bolean True Value ?
    1. true\n
    2. TRUE \n
    3. True\n
    4. truE \n""",'3'],
]
result = 0
for question, correct_answer in qeustions :
    answer = input(question)
    if answer == correct_answer:
        result = result + 1


print("your score is : {} out of Five qestions".format(result))



