#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading

def show_ramen():
    print u"--------------------------------------------------------------------------------"
    print u"|                                                                              |"
    print u"|                                                                              |"
    print u"|                           ,, -―-、                                           |"
    print u"|                      ／         ヽ                                           |"
    print u"|              ／￣￣／    ／i⌒ヽ､|        おぇーー！！！！                    |"
    print u"|            /    （゜）/     ／  /                                            |"
    print u"|          /         ト､.,../  ,ー-､                                           |"
    print u"|        =彳           ＼＼‘ﾟ。､｀ ヽ。、ｏ                                    |"
    print u"|        /                  ＼＼ﾟ。､。、ｏ                                     |"
    print u"|      /                  /⌒ ヽ ヽU    ｏ                                      |"
    print u"|     /                  │      `ヽU  ∴ｌ                                      |"
    print u"|    │                  │          U  ：l                                      |"
    print u"|                                        |：!                                  |"
    print u"|                                        Ｕ                                    |"
    print u"--------------------------------------------------------------------------------"

print "timer start"
timer = threading.Timer(3.0, show_ramen)
timer.start()

