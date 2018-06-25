#!/usr/bin/env python
# coding=utf-8

u"""
ノードをリネームする
"""

from __future__ import absolute_import, division, print_function

from logging import getLogger

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin, MayaQWidgetDockableMixin
import maya.OpenMayaUI as omui
import pymel.core as pm
from Qt import QtCore, QtWidgets

import stu.maya.decorator
import stu.name

try:
    import apps.ui.PySide2.rename as ui_rename
except ImportError:
    import apps.ui.PySide.rename as ui_rename


logger = getLogger(u"apps.rename")


class ApplicationError(Exception):
    pass


class Rename(QtWidgets.QWidget, ui_rename.Ui_Form):
    TITLE = u"stuRename"
    URL = u"https://readthedoc.org"

    def __init__(self, parent=None):
        super(Rename, self).__init__(parent)
        self.setupUi(self)

        # オブジェクト名とタイトルの変更
        self.setObjectName(self.TITLE)
        self.setWindowTitle(self.TITLE)

        # コールバック関数の設定
        self.btn_preview.clicked.connect(self.callback_preview)
        self.btn_execute.clicked.connect(self.callback_execute)

        self.btn_help.clicked.connect(self.callback_help)
        self.btn_default.clicked.connect(self.callback_default)

    def callback_help(self):
        pass

    def callback_default(self):
        pass

    def callback_preview(self):
        replace_search = self.replace_search.text()
        replace_text = self.replace_text.text()
        replace_regex = self.replace_regex.checkState() == QtCore.Qt.CheckState.Checked

        target_nodes = self.get_target_nodes()

        msg = replace(target_nodes, replace_search, replace_text, replace_regex, True)

        self.print_preview(msg)

    @stu.maya.decorator.undoable
    def callback_execute(self):
        replace_search = self.replace_search.text()
        replace_text = self.replace_text.text()
        replace_regex = self.replace_regex.checkState() == QtCore.Qt.CheckState.Checked

        target_nodes = self.get_target_nodes()

        replace(target_nodes, replace_search, replace_text, replace_regex)

    def get_target_nodes(self):
        return pm.ls(selection=True)

    def print_preview(self, messages):
        logger.info(u"Rename preview ===")
        for m in messages:
            logger.info(m)


class Dialog(MayaQWidgetBaseMixin, Rename):
    pass


class DockableWidget(MayaQWidgetDockableMixin, Rename):
    pass


def _safe_rename(node, new_name):
    if node.nodeName() == new_name:
        return

    try:
        pm.rename(node, new_name)
    except RuntimeError as e:
        stu.maya.warn(u"{0}: {1}".format(node.longName(), e))


def replace(target_nodes, replace_search, replace_text, replace_regex, dry=False):
    u"""ノード名をリネーム。

    :type target_nodes: pm.nodetypes.PyNode
    :type replace_search: unicode
    :type replace_text: unicode
    :type replace_regex: bool
    :type dry: bool
    :rtype: list of unicode
    """
    new_name = stu.name.replace(
        [t.nodeName() for t in target_nodes],
        replace_search, replace_text, replace_regex)

    messages = []
    for index, node in enumerate(target_nodes):
        if node.nodeName() == new_name[index][1]:
            continue

        if dry:
            messages.append(u"{0} --> {1}".format(node.longName(), new_name[index][1]))
        else:
            _safe_rename(node, new_name[index][1])

            msg = u"rename {0} --> {1}".format(node.longName(), new_name[index][1])
            logger.info(msg)
            messages.append(msg)

    return messages


customMixinWindow = None


def uiscript(restore=False):
    global customMixinWindow

    if customMixinWindow is None:
        customMixinWindow = DockableWidget()

    if restore:
        restoredControl = omui.MQtUtil.getCurrentParent()
        mixinPtr = omui.MQtUtil.findControl(customMixinWindow.objectName())
        omui.MQtUtil.addWidgetToMayaLayout(long(mixinPtr), long(restoredControl))
    else:
        customMixinWindow.show(
            dockable=True,
            uiScript='import apps.rename; apps.rename.uiscript(restore=True)')

    return customMixinWindow


def main():
    win = Dialog()
    win.show()
