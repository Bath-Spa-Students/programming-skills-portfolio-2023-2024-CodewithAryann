# Define a glossary using a dictionary
glossary = {'Variables':'A variable is a storage space in a programme that retains a value.',
            'Values':'A block of structured, reusable code that accomplishes a given task.',
            'Comments':'A programming construct that repeats a piece of code until a certain condition is fulfilled.',
            'Print':'It is a function that prints the provided message on the screen or other standard output device.',
            'Lists':'It is a set of stuff contained in [] and separated by commas.'}
    
# A list of Python phrases that will be added to the dictionary.
glossary['Dictionary'] = 'A data structure in Python that holds key-value pairs.'
glossary['Loop'] = 'A control structure that lets a computer to run a block of code several times when a certain condition is true.'
glossary['Float'] = 'A numerical value including a decimal component.'
glossary['Conditional Test'] = 'A comparison of two values.'
glossary['Module'] = 'A Python code file that may be imported and executed in other Python projects. Modules are a means of organizing code into reusable components.'

# Print each word and its meaning by using a loop
for words, meanings in glossary.items():
    print(f"{words}:\n{meanings}\n")