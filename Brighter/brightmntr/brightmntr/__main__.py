"""
File         : __init__.py
Author           : ian
Created          : 06-20-2015

Last Modified By : ian
Last Modified On : 06-20-2015
***********************************************************************
The MIT License (MIT)
Copyright © 2014 Ian Cooper <ian_hammond_cooper@yahoo.co.uk>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
***********************************************************************

Usage:
  brightmntr.py [options]

Options:
  -b --batch                            Don't accept command-line input; intended to send output to a file (or command).
  -d SECONDS --delay=SECONDS            Specific delay between refreshes (otherwise 5 seconds).
  -n TIMES --updates=TIMES              Update display n times, then exit.
  -p PAGESIZE --pagesize=PAGESIZE       Try to show this number of items from the queue, when the interval is triggered
  -s SERVICENAME --service=SERVICENAME  Filter output to this serviceName only
  _m MACHINENAME --machine=MACHINENAME  Filter output to this machine only
  -h --help     Show this screen.


"""

import sys

from docopt import docopt
from time import sleep
from threading import Thread


def read_monitoring_messages():
    # read the next batch number of monitoring messages from the control bus
    # evaluate for color coding (error is red)
    # print to stdout
    for x in range(1, 100):
        print(x, flush=True, end=" Monitoring message\n")
        sleep(5)

def run(cmdlne_arguments):
    # start a monitor output thread, this does the work, whilst the main thread just acts as a control
    worker = Thread(target=read_monitoring_messages)
    worker.daemon = True
    worker.start()

    # may need to demonize as the q ends up interrupting the messages
    while True:
        try:
            # just sleep unless we receive an interrupt i.e. CTRL+C
            sleep(1)
        except KeyboardInterrupt:
            sys.exit(1)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Brighter Management v0.0')
    run(arguments)
