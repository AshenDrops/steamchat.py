import curses
FLIST_WIDTH = 40

class View:
    def main(self, stdscr):
        self.resize()
        self.stdscr = stdscr
        while self.running:
            self.stdscr.refresh()
            self.flist.refresh()
            self.chat.refresh()
            self.test.refresh()
            self.handler(self.stdscr.getch())

    def __init__(self):
        print('inited')

    def resize(self):
        # Resizing doesn't even come close to fucking working
        self.width = curses.COLS
        self.height = curses.LINES
        curses.resizeterm(curses.LINES, curses.COLS)
        if hasattr(self, 'flist'):
            del self.flist
        self.flist = curses.newwin(self.height, FLIST_WIDTH, 0, 0)
        self.flist.border(0)
        if hasattr(self, 'chat'):
            del self.chat
        self.chat = curses.newwin(self.height, self.width-FLIST_WIDTH-1, 0, FLIST_WIDTH+1)
        self.chat.border(0)
        if hasattr(self, 'test'):
            del self.test
        self.test = curses.newwin(self.height - 15, self.width - FLIST_WIDTH - 3, 1, FLIST_WIDTH+2)
        self.test.border(0)

    def start(self):
        self.running = True
        curses.wrapper(self.main)

    def handler(self, char):
        if char == ord('p'):
            self.running = False
        elif char == curses.KEY_RESIZE:
            self.resize()

View().start()
