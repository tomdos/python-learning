#!/usr/bin/env python2
import readline
import sys
import os
import re

class ReadLineCompleter:
    def __init__(self):
        self.commands = ['start', 'stop', 'stat', 'list', 'print']
        readline.parse_and_bind('tab: complete')
        readline.set_completer(self.complete)
        readline.set_completer_delims('\n')
    
    def complete_path(self, current_path, prefix):
        pass
    
    def get_commands(self):
        return [name[4:] for name in dir(self) if name.startswith("cmd_")]
        
    def cmd_start(self, origline, complete_word):
        print "START"
        pass
    def cmd_stop(self):
        pass
    def cmd_stat(self):
        pass

    def cmd_exit(self):
        pass  
        
    def cmd_ls(self):
        pass        
    
    def cmd_cd(self, origline, complete_word):
        return self.complete_cd(origline, complete_word)
        
    def complete_cd(self, origline, complete_word):
        #print "\n=== text:", text, " line:", line, " begidx:", begidx, " endidx:", endidx
        self.cwd = "/"
        
        if not complete_word:
            dirname = self.cwd
            prefix = "."
        else:
            dirname = os.path.dirname(complete_word)
            if not dirname:
                dirname = self.cwd
                
            prefix = os.path.basename(complete_word)
            if not prefix:
                prefix = '.'
            
        pattern = "".join(["^", prefix, ".*"])
        completions = [name for name in os.listdir(dirname) if os.path.isdir(os.path.join(dirname,name)) and re.search(pattern, name)]
        
        return completions
        
        
    def complete(self, text, state):
        # TODO - completer (readline) will not raise exception???
        try:
            origline = readline.get_line_buffer()
            words = origline.split()
            begin = readline.get_begidx()
            end = readline.get_endidx()
            
            print text
            print begin
            print end
            
            if not origline or origline.find(" ") == -1:
                completions = [c for c in self.commands if c.startswith(text)]
            else:
                try:
                    fcnt = getattr(self, "cmd_" + words[0])
                    completions = fcnt(origline, words[-1])
                except:
                    print sys.exc_info()
                    raise
                
            print "\n", completions
            
            sys.stdout.write("> " + text)
            
            readline.redisplay()
            #readline.insert_text("ASDASD")
            
            return completions
        except:
            print "Complete exception: ", sys.exc_info()
        
        
    def loop(self):
        line = ''
        while line != 'stop':
            #sys.stdout.write("> ")
            self.line = raw_input("> ")
            print "line:", self.line
            


def main():
    rlc = ReadLineCompleter()
    print rlc.get_commands()
    rlc.loop()

if __name__ == "__main__":
    #readline.set_completer(ReadLineCompleter.complete)
    main()
    