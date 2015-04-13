#!/usr/bin/env python2
import cmd

class InteractiveShell(cmd.Cmd):
    def do_gree(self, line):
        print "hello"
        
    def do_EOF(self, line):
        return True
        
        
if __name__ == "__main__":
    InteractiveShell().cmdloop()        