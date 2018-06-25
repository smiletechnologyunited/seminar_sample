#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function

import traceback

import maya.cmds as cmds
from pymel import core as pm
from stu.maya import error


def undoable(func):
    u"""Undoチャンクを開いて閉じるデコレータ。コールバック関数に指定する。

    （注意）
    例外をキャッチして握りつぶしてしまうため、
    ユーザーが実行する最上位のメソッドにのみ使用可。
    """

    def wrapper(*args, **kwargs):
        pm.undoInfo(openChunk=True)
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(traceback.format_exc())
            error(str(e))
        finally:
            pm.undoInfo(closeChunk=True)

    return wrapper


def keep_selection(func):
    u"""セレクションを保持して元に戻すデコレータ。コールバック関数に指定する。

    ノードを削除・移動・リネームするような関数には使用してはいけない。

    （注意）
    例外をキャッチして握りつぶしてしまうため、
    ユーザーが実行する最上位のメソッドにのみ使用可。
    """

    def wrapper(*args, **kwargs):
        sel = cmds.ls(sl=True, l=True)
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(traceback.format_exc())
            error(str(e))
        finally:
            pm.select(sel, noExpand=True)

    return wrapper


def wait_cursor(func):
    u"""ウェイトカーソルを挟み込む

    （注意）
    例外をキャッチして握りつぶしてしまうため、
    ユーザーが実行する最上位のメソッドにのみ使用可。
    """

    def wrapper(*args, **kwargs):
        is_batch = pm.about(batch=True)
        if not is_batch:
            pm.waitCursor(state=True)

        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(traceback.format_exc())
            error(str(e))
        finally:
            if not is_batch:
                pm.waitCursor(state=False)

    return wrapper
