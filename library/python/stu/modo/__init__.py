#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function

import lx
import lxu

import logging


def select_items(items, hi=False):
    lx.eval('select.drop item')
    lx.eval('select.item "{0}" set'.format(items[0]))
    for n in items:
        lx.eval('select.item "{0}" add'.format(n))

    if hi:
        lx.eval("select.itemHierarchy")


def get_selected(types=[]):
    # 選択済みアイテムをリスト化
    itmsel = lxu.select.ItemSelection()
    selected_items = []
    for _s in itmsel.current():
        if types and _s.Type() not in types:
            continue

        selected_items.append(_s.UniqueName())

    return selected_items


def get_geoms(selected=False):
    selected_nodes = []
    if selected:
        # TODO(rt): マクロに変更する。 grouplocator,locator,mesh
        selected_nodes = get_selected(types=[17, 3, 4])

        logging.debug(selected_nodes)
        return selected_nodes

    geoms = []
    group_num = lx.eval('query sceneservice group.N ?')
    for _i in range(0, group_num):
        group_name = lx.eval("query sceneservice group.name ? {0}".format(_i))

        if selected and group_name not in selected_nodes:
            continue

        geoms.append(group_name)

    return geoms


def get_groups(selected=False):
    selected_groups = []
    if selected:
        selected_groups = get_selected(types=[1, ])  # TODO(takahashi_r): マクロに変更する。 group
        logging.debug(selected_groups)
        return selected_groups

    groups = []
    group_num = lx.eval('query sceneservice group.N ?')
    for _i in range(0, group_num):
        group_name = lx.eval("query sceneservice group.name ? {0}".format(_i))

        if selected and group_name not in selected_groups:
            continue

        groups.append(group_name)

    return groups
