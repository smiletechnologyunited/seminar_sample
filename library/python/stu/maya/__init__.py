#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function

import maya.mel


def _escape(msg):
    m = msg
    m = m.replace(u"\n", u"\\n")
    m = m.replace(u"\t", u"\\t")
    return m.replace(u"\"", u"'")


def error(msg):
    try:
        maya.mel.eval(u"error(\"{0}\")".format(_escape(msg)))
    except Exception:
        pass
