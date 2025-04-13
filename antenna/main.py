import logging
import sys

from antenna.antenna import Antenna

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        stream=sys.stdout,
    )
    if len(sys.argv) != 2:
        raise Exception('Usage: antenna <build.xml path>')
    Antenna().up(sys.argv[1])
