#!/usr/bin/python

import asyncio
import sys
import os
import socket
from cmd import Cmd

class Shell(Cmd):

    prompt = f'({socket.gethostname()})> '

    so = None

    def do_echo(self, arg):
        '''echoes the arguments'''
        print(arg)

    def do_connect(self, arg):
        '''connects to server via python sockets'''
        
        arg = [i.strip() for i in arg.strip().split()]

        try: 
            if len(arg) != 2:
                raise Exception
            arg[1] = int(arg[1])
        except Exception:
            print('invalid arguments')
            return

        so = socket.socket()
        so.connect((arg[0], arg[1]))
        self.so = so

    def do_send(self, arg):
        '''sends data to server'''
        
        self.so.sendall(arg.encode()+b'\n')

    def do_close(self, arg):
        '''closes socket'''

        self.so.close()

    def do_exit(self, arg):
        '''exits the shell'''
        return True

if __name__=='__main__':
    
    Shell().cmdloop()

