#!/usr/bin/env python
# coding=utf-8

u"""
stu.renameコマンドを作成する
"""
from __future__ import absolute_import, division, print_function

import lx
import lxu.command


class NodeRename(lxu.command.BasicCommand):
    def basic_Execute(self, msg, flags):
        cmd = [
            u"layout.createOrClose",
            u"cookie:COOKIE_stuRename",
            u"layout:stuRenameLayout",
            u'title:"stuRename"',
            u"width:300",
            u"height:300",
            u"persistent:1",
            u"style:palette"
        ]
        lx.eval(" ".join(cmd))


lx.bless(NodeRename, u"stu.node.rename")
