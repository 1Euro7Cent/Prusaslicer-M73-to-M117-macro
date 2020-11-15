
"""
@author: SCHERIC
@forked: JaySNL

# Added beautification of Rxxx to D:HH:MM.
# changed m117 to M117 because case sensitive
# removed debug features
"""

import sys
import re
import time

time_start = time.time()

sourceFile = sys.argv[1]

add_count = 0

def pretty_time_delta(seconds):
    seconds = int(seconds)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if days > 0:
        return '%dD:%dH:%dM' % (days, hours, minutes)
    elif hours > 0:
        return '%dH:%dM' % (hours, minutes)
    elif minutes > 0:
        return '%dM' % (minutes)
    else:
        return '%ds' % (seconds,)

with open(sourceFile, "r") as file:
    lines = file.readlines()
    file.close()

with open(sourceFile, "w") as file:
    for line_number in range(len(lines)):
        new_line = lines[line_number]

        if len(new_line) > 0:
            # Write original line to buffer
            file.write(new_line)

            # find specific line
            stringMatch = re.search('^M73 P(.*) R(.*)', new_line)
            if stringMatch:
                # do something when hit

                # Parse gcode line
                string = stringMatch.string
                parsed = string.split(' ')

                parsed[1] = parsed[1][1:]
                parsed[2] = parsed[2][1:-1]
                
                time_minutes = int(parsed[2])
                time_seconds = int(time_minutes * 60)
                        
                time_math = pretty_time_delta(time_seconds)
                
                output = 'M117 ' + parsed[1] + '% ' + time_math + " left"

                if debug >= 2:
                    print(f"converted {stringMatch} to {output}")

                # save new line to file
                file.write(f"{output}\n")

                add_count = add_count + 1

# return file to proses
file.close()

time_end = time.time()
