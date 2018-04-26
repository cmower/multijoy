from sys import argv

def genMsg(N):
    filename='MultiJoy{}.msg'.format(N)
    out=open(filename, 'w')
    out.write('Header header\n')
    for i in xrange(N):
        txt='sensor_msgs/Joy joy{}\n'.format(i+1)
        out.write(txt)
    out.close()
    print "MultiJoy msg created: {}".format(filename)
    print "[REMEMBER] add {} to CMakeLists.txt under add_message_files()"
    
def printHelp():
    print "Usage:"
    print "  $ python genMultiJoyMsg.py N\n"
    print "N is the number of joysticks"

if __name__=='__main__':

    if len(argv)!=2:
        printHelp()
        quit()

    if argv[1]=='-h':
        printHelp()
    else:
        N=int(argv[1])
        genMsg(N)
        
