#!/usr/bin/env python
import cmd
import os
import readline
import rlcompleter
import re
import sys

class InteractiveShell(cmd.Cmd):
    def __init__(self):
        self.cwd = "."

        if "libedit" in readline.__doc__:
            readline.parse_and_bind("bind '\t' rl_complete")
        else:
            readline.parse_and_bind('tab: complete')

        cmd.Cmd.__init__(self)


    def do_exit(self, line):
        return True

    def do_pwd(self, line):
        print self.cwd
    def do_get(self, line):
        print "=get"
    def do_put(self, line):
        print "=put"

    def do_ls(self, line):
        if not line:
            directory = self.cwd
        else:
            directory = line

        try:
            for name in os.listdir(directory):
                print name
        except OSError:
            print "No such file or directory: ", directory


    def do_cd(self, line):
        """CD to directory passed in line or to root /."""

        if not line:
            new_wd = '.'
        else:
            new_wd = line

        try:
            os.chdir(new_wd)
            self.cwd = os.path.join(self.cwd, new_wd)
        except OSError:
            print "No such file or directory: ", new_wd


    def complete_put(self, text, line, begidx, endidx):
        return self.complete_cd(text, line, begidx, endidx)


    def complete_cd(self, text, line, begidx, endidx):
        #print "\n=== text:", text, " line:", line, " begidx:", begidx, " endidx:", endidx

        dirname = os.path.dirname(text)
        if not dirname:
            dirname = self.cwd

        prefix = os.path.basename(text)
        if not prefix:
            prefix = '.'

        pattern = "".join(["^", prefix, ".*"])
        completions = [name+os.sep for name in os.listdir(dirname) if os.path.isdir(os.path.join(dirname,name)) and re.search(pattern, name)]

        try:
            #if len(completions) == 1:
            if text:
                dirname = os.path.dirname(text)
                completions = [os.path.join(dirname,name) for name in completions]
        except:
            print sys.exc_info()

        return completions

    #FIXME if we are able to add space after single returned command we will
    # automatically jump to a complete_X function.
    #def complete(self, text, state):
    #    print cmd.Cmd.complete(text, state)


    #def do_EOF(self, line):
    #    return True


if __name__ == "__main__":
    # threat '/' as part of the word
    # http://stackoverflow.com/questions/5637124/tab-completion-in-pythons-raw-input/5638688#5638688
    readline.set_completer_delims(' \t\n;')
    InteractiveShell().cmdloop()
