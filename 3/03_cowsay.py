'''
Created on May 24, 2018

@author: of
'''

cow = """
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
"""


speech_bubble_top_symbol = """_"""
speech_bubble_bottom_symbol = """-"""

def main():
    tosay = "Python rocks!"
    length = len(tosay)
    speech = '  ' + speech_bubble_top_symbol * length + "\n"
    speech += '< ' + tosay + " >"
    speech += '\n  ' + speech_bubble_bottom_symbol * length 
    print speech + cow

if __name__ == "__main__":
    main()