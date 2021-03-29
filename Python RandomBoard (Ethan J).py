'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def returnOutput(startDNA):
    output = ""
    for char in startDNA:
        if (char == "T"):
            output += "A"
            continue
        elif (char == "A"):
            output += "T"
            continue
        elif (char == "C"):
            output += "G"
            continue
        elif (char == "G"):
            output += "C"
            continue
        else:
            output = "Error RNA nucleobases found!"
            return output
    return output

numSequences = input()

i = 0
while i < int(numSequences):
    length = input()
    sequence = input()
    print (returnOutput(sequence))
    i += 1