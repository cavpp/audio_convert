#!/usr/local/bin/python
import sys

__title__ = 'Audio Convert'
__author__ = 'Henry Borchers'
__version__ = '0.1.1'
__license__ = 'GPL'

# import Queue
from os import walk
import os
import argparse
# sys.path.insert(0, os.path.abspath('..'))
from audio_convert.scripts.modules.Audio_factory import AudioFactory


line = "--------------------------------------------------"





def openingBanner():
    print"\n"
    print "Audio converter script for CAVPP. \n" \
          "Dependencies: \n" \
          "Python 2.7 \n" \
          "OneSheet \n" \
          "ffmpeg \n" \
          "LAME \n" \
          "\n" \
          "Programmed by Henry Borchers\n"


def main(input_argument):

    derivative_maker = AudioFactory(verbose=True)
    # input_argument = str(argv[1])

    if os.path.isdir(input_argument):
        for root, dir, files in walk(input_argument):
            for file in files:
                if ".wav" in file:
                    # print "Adding \"" + path.join(root, file) + "\" to the queue."
                    derivative_maker.add_audio_file(os.path.join(root, file))
                    # print "found one"
    elif os.path.isfile(input_argument):
            if ".wav" in input_argument:
                print "Converting: " + os.path.join(input_argument)
                derivative_maker.add_audio_file(input_argument)
            else:
                # display_usage("This program only works with .wav files.")
                sys.stderr.write("This program only works with .wav files.")
    else:
        # display_usage("Not a valid file or directory")
        sys.stderr.write("Not a valid file or directory")

    # current_queue =         # display_usage("Missing directory or file")
    # for queue in derivative_maker.preview_queues():
    #     print queue[0], queue[1]

    # print "\nencoding next\n"
    while derivative_maker.hasTasks:
        derivative_maker.encode_next()
        # encode_next
    # derivative_maker.daemon = True
    # derivative_maker.start()
    # derivative_maker.join()
    for queue in derivative_maker.preview_queues():
        print queue[0], queue[1]



def installed_start():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="File or folder name", nargs='?', default="", type=str)
    parser.add_argument("-g", "--gui", help="EXPERIMENTAL: Loads the graphical user interface.", action='store_true')
    ars = parser.parse_args()
    openingBanner()
    if ars.gui:
        print "Starting graphical user interface!"
        # sys.path.insert(0, os.path.abspath('..'))
        from gui.gui import startup

        if ars.input:
            startup(ars.input)
        else:
            startup()

    elif ars.input == "":
        parser.print_help()
    else:
        main(ars.input)
        # print ars.input

if __name__ == '__main__':

   installed_start()