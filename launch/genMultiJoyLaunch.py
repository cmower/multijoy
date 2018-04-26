from sys import argv

def printHelp():
    print "Usage:"
    print "  $ python genMultiJoyLaunch.py N\n"
    print "N is the number of joysticks"

def writeJoy(f, n):
    f.write('  <node pkg="joy" type="joy_node" name="joy{}">\n'.format(n))
    f.write('    <remap from="joy" to="joy/{}"/>\n'.format(n))
    f.write('    <param name="dev" type="string" value="/dev/input/js{}"/>\n'.format(n-1))
    f.write('    <param name="deadzone" value="0.0" />\n')
    f.write('    <param name="autorepeat_rate" value="100.0" type="double"/>\n')
    f.write('  </node>\n')

def genLaunch(N):
    filename="joysticks{}.launch".format(N)
    out=open(filename, 'w')
    
    out.write('<launch>\n')
    out.write('  <param name="njoy" type="int" value="{}"/>\n'.format(N))
    for n in xrange(1, N+1):
        writeJoy(out, n)
    out.write('  <node pkg="multijoy" name="multijoy_node" type="multijoy_node.py" output="screen"/>\n')
    out.write('</launch>')
    out.close()
    print "MultiJoy launch created: {}".format(filename)

if __name__=='__main__':

    if len(argv)!=2:
        printHelp()
        quit()

    if argv[1]=='-h':
        printHelp()
    else:
        N=int(argv[1])
        genLaunch(N)
        

    
