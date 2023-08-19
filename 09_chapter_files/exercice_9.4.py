# Basic solution
def process_case_op1(infile, outfile):
    output = open(outfile, "w")
    for line in open(infile):
        print(line.strip())
        if not line.strip()[0] in "abcdefghijklmnopqrstuvwxyz":
            output.write(line)
    output.close()

# Solution 2 using the built-in isupper() function
def process_case_op2(infile, outfile):
    output = open(outfile, "w")
    for line in open(infile):
        if line.strip()[0].isupper():
            output.write(line)
    output.close()

# Solution 3 using with open for both files
def process_case_op3(infile, outfile):
    with open(outfile, "w") as output, open(infile, 'r', encoding='windows-1252') as input:
        for line in input:
            if line.strip()[0].isupper():
                output.write(line)

def main():
    process_case_op1("case.txt", "output1.txt")
    process_case_op2("case.txt", "output2.txt")
    process_case_op3("case.txt", "output3.txt")

if __name__ == '__main__':
    main()
