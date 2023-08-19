#Name of file is wrong and will cause an exception
import getpass
import socket
import csv

def write_log(log_file):
    username = getpass.getuser()
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    
    # Write the log
    with open(log_file, 'a', newline='\n') as fo:
        writer = csv.writer(fo, delimiter='|', quoting=csv.QUOTE_NONNUMERIC)
        try:
            writer.writerow((username, hostname, ip))
        except FileNotFoundError as e:
            print('Log file problem')

def process_case(input_file, output_file):
    try:
        with open(input_file) as input_f:
            with open(output_file, 'w') as output_f:
                for line in input_f:
                    if not line.strip().islower():
                        output_f.write(line)
    except FileNotFoundError as e:
        print('File problem')
        write_log('logs.csv')

if __name__ == '__main__':
    process_case('cass.txt', 'output.txt')
