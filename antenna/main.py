import sys

from antenna.antenna import Antenna

if __name__ == '__main__':
    if len(sys.argv) > 2:
        raise Exception('Usage: antenna <build.xml path>')
    Antenna().up(sys.argv[1])
