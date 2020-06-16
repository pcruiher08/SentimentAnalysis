import sys, getopt
from Method import call

def main(filename,argv):
    method = ''
    #first we try to get aguments from the inline call
    try:
        opts, args = getopt.getopt(argv,"m:h",["method=","help"])
    except getopt.GetoptError:
        print('usage: {} -m <method>'.format(filename))
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: {} -m <method>'.format(filename))
            sys.exit()
        elif opt in ("-m", "--method"):
            method = arg
    
    return method

if __name__ == '__main__':
    method = main(sys.argv[0],sys.argv[1:])
    call(method)

