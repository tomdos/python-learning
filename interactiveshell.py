#!/usr/bin/env python2
import cmd
import os
import readline
import re
import sys

class InteractiveShell(cmd.Cmd):
    cwd = "/"
    
    def __init__(self):
        cmd.Cmd.__init__(self)

        
    def do_exit(self, line):
        pass
        
    def do_cwd(self, line):
        print self.cwd
        
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
    
    def do_put(self, line):
        print "put ", line
        
    def complete_put(self, text, line, begidx, endidx):
        return self.complete_cd(text, line, begidx, endidx)
            
    
    def do_cd(self, line):
        """
        CD autocompletion - unfortunately it it is not working as I wish. I am 
        searching for similar solution as in shell. I got very similar behaviour 
        however autocompleted path is not relative path but absolut.
        """
        if not line:
            newCwd = '.'
        else:
            newCwd = line
        
        try:
            os.chdir(newCwd)
            self.cwd = os.path.join(self.cwd,newCwd)
        except OSError:
            print "No such file or directory: ", newCwd
        
    
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

        
        
    def do_EOF(self, line):
        return True
        
        
if __name__ == "__main__":
    # threat '/' as part of the word 
    # http://stackoverflow.com/questions/5637124/tab-completion-in-pythons-raw-input/5638688#5638688
    readline.set_completer_delims(' \t\n;') 
    InteractiveShell().cmdloop()