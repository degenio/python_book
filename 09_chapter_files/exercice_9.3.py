# Solution returning only the length
def calculate_file_length(file):
    maximum = ""
    for line in open(file):
        if len(line) > len(maximum):
            maximum = line
    return len(maximum)

# Solution returning both length and the line itself
def calculate_file_stats(file):
    max_line = ""
    for line in open(file):
        if len(line) > len(max_line):
            max_line = line
    return len(max_line), max_line

def main():
    max_length = calculate_file_length("stats.txt")
    print("Maximum length:", max_length)

    max_length, max_line = calculate_file_stats("stats.txt")
    print("Maximum length:", max_length)
    print("Line with maximum length:", max_line)

if __name__ == '__main__':
    main()
