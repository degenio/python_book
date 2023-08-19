def process_case(input_file, output_file):
    with open(input_file) as fi:
        with open(output_file, 'w') as fo:
            for line in fi:
                if not line.strip().islower():
                    fo.write(line)


if __name__ == '__main__':
    process_case('case.txt', 'output.txt') 