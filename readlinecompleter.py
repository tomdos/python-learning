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
        self.cwd = '.'
    
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
    def cmd_something(self):
        pass

    def cmd_exit(self):
        pass  
        
    def cmd_ls(self):
        pass
    
    def cmd_cd(self):
        pass
        
    def complete_ls(self, line, word):
        return self.complete_cd(line, word)
        
    def complete_cd(self, line, word):
        #print "\n=== text:", text, " line:", line, " begidx:", begidx, " endidx:", endidx
        #self.cwd = "/"
        
        if not word:
            dirname = self.cwd
            prefix = "."
        else:
            dirname = os.path.dirname(word)
            if not dirname:
                dirname = self.cwd
                
            prefix = os.path.basename(word)
            if not prefix:
                prefix = '.'
            
        pattern = "".join(["^", prefix, ".*"])
        completions = [name+os.sep for name in os.listdir(dirname) if os.path.isdir(os.path.join(dirname,name)) and re.search(pattern, name)]
        
        if word:
            dirname = os.path.dirname(word)
            completions = [os.path.join(dirname,name) for name in completions]
        
        return completions
        
        
    def complete(self, text, state):
        # TODO - completer (readline) will not raise exception???
        if state != 0:
            return None
            
        try:
            origline = readline.get_line_buffer()
            words = origline.split()
            begin = readline.get_begidx()
            end = readline.get_endidx()
            
            #print
            #print text
            #print begin
            #print end
            
            if not origline or origline.find(" ") == -1:
                completions = [c for c in self.get_commands() if c.startswith(text)]
            else:
                try:
                    fcnt = getattr(self, "complete_" + words[0])
                    completions = fcnt(origline, words[-1])
                    completions = [origline[0:-len(words[-1])] + i for i in completions]
                except:
                    print sys.exc_info()
                    raise
                
            print "\n", completions
            
            sys.stdout.write("> " + text)
            
            #readline.redisplay()
                        
            #return completions
            if len(completions) == 1:    
                return completions[0]
            else:
                return os.path.commonprefix(completions)
                
        except:
            print "Complete exception: ", sys.exc_info()
    
    def cmd(self, line):
        words = line.split();
        
        if words[0] == "cd":
            if len(words) > 1:
                newCwd = words[1]
            else:
                newCwd = "/"
                
            try:
                os.chdir(words[1])
                self.cwd = os.path.join(self.cwd, newCwd) #FIXME
            except OSError:
                print "No such file or directory: ", newCwd
                
        elif words[0] == "ls":
            if len(words) > 1:
                directory = words[1]
            else:
                directory = self.cwd
                
            try:
                for name in os.listdir(directory):
                    print name
            except OSError:
                print "No such file or directory: ", directory
    
        
    def loop(self):
        line = ''
        while line != 'stop':
            #sys.stdout.write("> ")
            self.line = raw_input("> ")
            self.cmd(self.line)
            print "line:", self.line
            


def main():
    rlc = ReadLineCompleter()
    print rlc.get_commands()
    rlc.loop()

if __name__ == "__main__":
    #readline.set_completer(ReadLineCompleter.complete)
    main()
    