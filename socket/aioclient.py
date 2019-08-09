#!/usr/bin/python

import asyncio
import sys
import os
import socket
from cmd import Cmd

class Connection(Cmd):
    prompt = 'conection > ' 

    def __init__(self, so):
        self.so = so
        super().__init__()
    
    def do_send(self, arg):
        self.so.sendall(arg.encode()+b'\n')

    def do_close(self, arg):
        self.so.close()
        return True

class Shell(Cmd):

    prompt = f'({socket.gethostname()})> '

    def do_echo(self, arg):
        '''echoes the arguments'''
        print(arg)

    def do_socketconnect(self, arg):
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
        i = Connection(so)
        i.cmdloop()

    def do_asyncconnect(self, arg):
        '''connects to server via python asyncio'''

    def do_exit(self, arg):
        '''exits the shell'''
        return True

if __name__=='__main__':
    
    Shell().cmdloop()

