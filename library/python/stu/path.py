#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function

import ctypes
from logging import getLogger
import os
import stat


logger = getLogger(u"stu.path")


def normpath(path):
    u"""ファイルパスを正規化する。

    >>> normpath(u'C:/hello/world.png')
    u'C:\\\\hello\\\\world.png'
    >>> normpath(u'c:\\hello\\world.png')
    u'C:\\\\hello\\\\world.png'
    >>> normpath(u'c:/hello/world.png')
    u'C:\\\\hello\\\\world.png'
    >>> normpath(u'C:\\hello\\world.png')
    u'C:\\\\hello\\\\world.png'
    >>> normpath(u'C:\\hello\\..\\hello\\world.png')
    u'C:\\\\hello\\\\world.png'
    """
    # パス区切り文字を正規化する
    n = os.path.normpath(os.path.abspath(path))

    # ドライブレターを大文字に統一する
    _drive, _p = os.path.splitdrive(n)
    return _drive.upper() + _p


def makedir_if_not_exists(filename):
    u"""指定したファイルパスのディレクトリが無ければ作成する。"""
    dirpath = os.path.dirname(os.path.abspath(filename))
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
        logger.info(u"make directory. ({0})".format(dirpath))


def change_stat_if_not_writable(filename):
    u"""指定したファイルに書き込み属性が無ければ追加する。"""
    if os.path.exists(filename):
        mode = os.stat(filename)[stat.ST_MODE]
        if not stat.S_IMODE(mode) & stat.S_IWRITE:
            logger.info(u"add write flag. ({0})".format(filename))
            os.chmod(filename, stat.S_IWRITE)


def iswritable(filename):
    mode = os.stat(filename)[stat.ST_MODE]
    if stat.S_IMODE(mode) & stat.S_IWRITE:
        return True

    return False


def expand_short_filename(path):
    u"""8.3形式の短いファイル名を長いファイル名に展開する"""
    buf = ctypes.create_unicode_buffer(500)
    WinPath = ctypes.windll.kernel32.GetLongPathNameW
    WinPath(unicode(path), buf, 500)
    return buf.value
