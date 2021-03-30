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
        return "Error RNA nucleobases found!"
    return output

numSequences = input()

for i in range(int(numSequences)):
    input() #b/c the method doesn't need length, but it still gets inputted
    print(returnOutput(input()))