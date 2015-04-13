#!/usr/bin/env python2
import cmd
import os
import readline
import re

class InteractiveShell(cmd.Cmd):
    cwd = "/"
        
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
            
    
    def do_cd(self, line):
        if not line:
            newCwd = '/'
        else:
            newCwd = line
        
        try:
            os.chdir(newCwd)
            self.cwd = os.path.join(self.cwd,newCwd)
        except OSError:
            print "No such file or directory: ", newCwd
        
    
    def complete_cd(self, text, line, begidx, endidx):
        #print "\n=== text:", text, " line:", line, " begidx:", begidx, " endidx:", endidx
        
        if not text:
            dirname = self.cwd
            prefix = "."
        else:
            dirname = os.path.dirname(text)
            if not dirname:
                dirname = self.cwd
                
            prefix = os.path.basename(text)
            if not prefix:
                prefix = '.'
            
        pattern = "".join(["^", prefix, ".*"])
        completions = [os.path.join(dirname,name) for name in os.listdir(dirname) if os.path.isdir(os.path.join(dirname,name)) and re.search(pattern, name)]
        return completions

        
        
    def do_EOF(self, line):
        return True
        
        
if __name__ == "__main__":
    # threat '/' as part of the word 
    # http://stackoverflow.com/questions/5637124/tab-completion-in-pythons-raw-input/5638688#5638688
    readline.set_completer_delims(' \t\n;') 
    InteractiveShell().cmdloop()