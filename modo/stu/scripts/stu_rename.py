#!/usr/bin/env python
# coding=utf-8

u"""
stu.node.renameコマンドで作成したGUIに関連した処理を行うスクリプト
"""

from __future__ import absolute_import, division, print_function

import argparse
import logging
import subprocess

import lx

import stu.modo
import stu.name


COMMAND = u"@stu_rename.py"
URL = u"https://readthedocs.org"
DESCRIPTION = u"stu.node.rename"

SUBCOMMANDS = [
    u"replace",
    u"openhelp",
    u"setdefault",
]

logger = logging.getLogger(u"stu.rename")


def _safe_rename(node, new_name):
    if node == new_name:
        return

    # 対象以外の選択状態を保存
    other_selection = []
    _sel = stu.modo.get_selected()
    for s in _sel:
        if s != node:
            other_selection.append(s)

    try:
        stu.modo.select_items([node, ])
        lx.eval('item.name {0} xfrmcore'.format(new_name))
        new_name = lx.eval('item.name ?')
    except RuntimeError as e:
        logger.warn(u"{0}: {1}".format(node, e))

    # 選択状態を復元
    stu.modo.select_items(other_selection + [new_name, ])


def replace(target_nodes, replace_search, replace_text, replace_regex, dry=False):
    new_name = stu.name.replace(target_nodes, replace_search, replace_text, replace_regex)

    messages = []
    for index, node in enumerate(target_nodes):
        if node == new_name[index][1]:
            continue

        if dry:
            messages.append(u"{0} --> {1}".format(node, new_name[index][1]))
        else:
            _safe_rename(node, new_name[index][1])

            msg = u"rename {0} --> {1}".format(node, new_name[index][1])
            logger.info(msg)
            messages.append(msg)

    return messages


def open_help():
    subprocess.Popen([u"start", u"dummy title", URL], shell=True)


def set_default():
    pass


def replace_command(dry=False):
    replace_search = lx.eval('user.value stuRename_replace_search ?')
    replace_text = lx.eval('user.value stuRename_replace_text ?')
    replace_regex = lx.eval('user.value stuRename_replace_regex ?')

    target_nodes = stu.modo.get_selected()

    messages = replace(target_nodes, replace_search, replace_text, replace_regex, dry)

    if dry:
        for m in messages:
            logger.info(m)


def _init_logger(name=u"", develop=False):
    if develop:
        log_format = u"%(asctime)s %(name)s [%(levelname)s] %(filename)s:%(lineno)d %(message)s"
        log_level = logging.DEBUG
    else:
        log_format = u"[%(levelname)s] %(message)s"
        log_level = logging.INFO

    _logger = logging.getLogger(name)
    _logger.propagate = False
    _logger.handlers = []
    _stream_handler = logging.StreamHandler()
    _formatter = logging.Formatter(log_format)
    _stream_handler.setFormatter(_formatter)
    _logger.addHandler(_stream_handler)
    _logger.setLevel(log_level)


def main():
    parser = argparse.ArgumentParser(prog=COMMAND, description=DESCRIPTION)
    parser.add_argument(
        dest=u"command",
        default=None,
        metavar=u"COMMAND",
        choices=SUBCOMMANDS,
        help=u"sub command."
    )
    parser.add_argument(
        u"--dry",
        dest=u"dry",
        action=u"store_true",
        default=False,
        help=u"dry run."
    )
    parser.add_argument(
        u"-D", u"--debug",
        dest=u"debug",
        action=u"store_true",
        default=False,
        help=u"debug mode."
    )
    args = parser.parse_args(lx.args())

    _init_logger(u"stu", develop=args.debug)
    _init_logger(u"apps", develop=args.debug)
    logger.debug(args)

    if args.command == u"replace":
        replace_command(args.dry)
    elif args.command == u"openhelp":
        open_help()
    elif args.command == u"setdefault":
        set_default()


if __name__ == u"__main__":
    main()
