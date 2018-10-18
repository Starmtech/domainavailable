#!/usr/bin/python

import socket
import os
import sys


def coloriage(s, color, bold=False):
   colors = {'red': 31, 'green': 32, 'yellow': 33,
             'blue': 34, 'magenta' : 36}
   if os.getenv('ANSI_COLORS_DISABLED') is None and color in colors:
       if bold:
           return '\033[1m\033[%dm%s\033[0m' % (colors[color], s)
       else:
           return '\033[%dm%s\033[0m' % (colors[color], s)
   else:
       return s

def tries(tab,toplevel):
    for n in toplevel:
        for i in tab:
            for p in tab:
                if i in p:
                    pass
                else:
                    domainall = i+p+n
                    requestdns(domainall)

def requestdns(host):
        try:
            adresseip = socket.gethostbyname(host)
            print host +" = "+ coloriage(" Le nom de domaine n'est pas utilisé","red","False")
        except socket.gaierror:
            print host + " = " + coloriage(" Le nom de domaine est utilisé","green","False")

def main():
    tab = ['net','secu','info','network','security']
    toplevel = ['.com','.fr','.org','.net','.int','.info','.paris','.edu','.uk']
    cpt = 0
    h = 0
    for l in sys.argv:
        cpt += 1
        v = 0
        if l in '-t' or l in '-T':
            toplevel = []
            toplevel.append(str(sys.argv[cpt]))
        elif l in '-d' or l in '-D':
            tab = sys.argv[cpt]
            tab = tab.split(',')

        if l in '-h' or l in '-H':
            h + 1
            print '''Utilisation:
            domainavailable.py
            domainavailable.py -t .com -d ['test','je','suis']'''
    if h < 1:
       tries(tab,toplevel)



if __name__=="__main__":
    main()
