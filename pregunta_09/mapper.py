#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:

        columns = line.strip().split('   ')
        
        sys.stdout.write("{}\t{}\t{}\n".format(columns[2],columns[0],columns[1]))
