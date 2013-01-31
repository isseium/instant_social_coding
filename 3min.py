#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading

def show_ramen():
    print "--------------------------------------------------------------------------------"
    print "|                                                                              |"

print "timer start"
timer = threading.Timer(3.0, show_ramen)
timer.start()

