#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading

print "timer start"
timer = Timer(180.0, show_ramen)
timer.start

def show_ramen():
