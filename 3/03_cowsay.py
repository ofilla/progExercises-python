'''
Created on May 24, 2018

@author: of
'''

from sys import argv

cow = """
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
"""


speech_bubble_top_symbol = '_'
speech_bubble_bottom_symbol = '-'

def cowsay(tosay):
    length = len(tosay)
    speech = '  ' + speech_bubble_top_symbol * length + "\n"
    speech += '< ' + tosay + " >"
    speech += '\n  ' + speech_bubble_bottom_symbol * length 
    print speech + cow

def get_tosay():
    if len(argv) > 1:
        return argv[1]
    
    got = raw_input("What shall the cow say?\n> ")
    print
    return got

if __name__ == "__main__":
    tosay = get_tosay()
    cowsay(tosay)