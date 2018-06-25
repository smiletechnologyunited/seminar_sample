# !/usr/bin/env python
# coding=utf-8

import logging

import maya.utils
import pymel.core as pm


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
    _stream_handler = maya.utils.MayaGuiLogHandler()
    _formatter = logging.Formatter(log_format)
    _stream_handler.setFormatter(_formatter)
    _logger.addHandler(_stream_handler)
    _logger.setLevel(log_level)


_init_logger(u"stu", develop=True)
_init_logger(u"apps", develop=True)
