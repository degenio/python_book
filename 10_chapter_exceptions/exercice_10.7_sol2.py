# Handling FileNotFoundError
def process_case(input_file, output_file):
    try:
        with open(input_file) as input_f:
            with open(output_file, 'w') as output_f:
                for line in input_f:
                    if not line.strip().islower():
                        output_f.write(line)
    except FileNotFoundError as e:
        print('File problem')

if __name__ == '__main__':
    process_case('case.txt', 'output.txt')
