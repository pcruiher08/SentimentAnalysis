import sys, getopt
from Method import call

def main(filename,argv):
    method = ''
    counter = 100
    #first we try to get aguments from the inline call
    try:
        opts, args = getopt.getopt(argv,"m:c:h",["method=","counter=","help"])
    except getopt.GetoptError:
        print('usage: {} -m <method>'.format(filename))
        print('usage: {} -m <twitter|youtube|voice>'.format(filename))
        print('usage: {} -m <twitter|youtube|voice> -c 100'.format(filename))
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: {} -m <twitter|youtube|voice>'.format(filename))
            sys.exit()
        elif opt in ("-m", "--method"):
            method = arg
        elif opt in ("-c", "--counter"):
            counter = int(arg)
    print(counter, method)
    return method, counter

if __name__ == '__main__':
    method, counter = main(sys.argv[0],sys.argv[1:])
    call(method, counter)

