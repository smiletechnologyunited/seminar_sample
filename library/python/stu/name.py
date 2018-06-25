#!/usr/bin/env python
# coding=utf-8

u"""
ノード名などの操作
"""

from __future__ import absolute_import, division, print_function

import doctest
from logging import getLogger
import re


logger = getLogger(u"stu.name")

POSITION_START = u"^"
POSITION_END = u"$"


def _replace_magic_word(name_list):
    u"""特殊文字の置き換えを行なう。

    ### 3桁のユニークな数字
    #### 4桁のユニークな数字

    番号は見つかった順に割り当てられる。桁の違いは関係なく通し番号となる。

    >>> _replace_magic_word([u"hi", u"hello####", u"world###"])
    [u'hi', u'hello0001', u'world002']
    """
    result = []

    current_number = 1
    for name in name_list:
        m = re.search(u"#+", name)
        if not m:
            result.append(name)
        else:
            start_pos = m.start(0)
            end_pos = m.end(0)
            # word = m.group(0)

            num = u"{0:0{width}}".format(current_number, width=int(end_pos - start_pos))

            new_name = u"{0}{1}{2}".format(name[:start_pos], num, name[end_pos:])

            result.append(new_name)

            current_number += 1

    return result


def rename(name_list, text_word):
    u"""リネームを行なう。

    >>> rename([u"aaa", u"bbb"], u"hello####")
    [[u'aaa', u'hello0001'], [u'bbb', u'hello0002']]
    """
    # マジックワードの置換だけ行なう
    new_name_list = _replace_magic_word([text_word for n in name_list])

    result = []
    for index, name in enumerate(name_list):
        result.append([name, new_name_list[index]])

    return result


def replace(name_list, search_word, text_word, regex=False):
    u"""置換を行なう。

    :type name_list: list of unicode
    :type search_word: unicode
    :type text_word: unicode
    :type regex: bool
    :rtype regex: list of tuple

    >>> replace([u"aaab", u"bbbb"], u"bb", u"hello####")
    [[u'aaab', u'aaab'], [u'bbbb', u'hello0001bb']]
    >>> replace([u"aaab", u"bbbb"], u"a{2}b", u"hello####", True)
    [[u'aaab', u'ahello0001'], [u'bbbb', u'bbbb']]
    >>> replace([u"helloTAKAHASHIworld", u"helloRYOworld"], r"hello(.*)world", r"\g<1>", True)
    [[u'helloTAKAHASHIworld', u'TAKAHASHI'], [u'helloRYOworld', u'RYO']]
    >>> replace([u"helloTAKAHASHIworld", u"helloRYOworld"], r"hello(.*)world", r"\g<1>##", True)
    [[u'helloTAKAHASHIworld', u'TAKAHASHI01'], [u'helloRYOworld', u'RYO02']]
    >>> replace([u"aaab", u"bbbb"], u"bb", u"hello##")
    [[u'aaab', u'aaab'], [u'bbbb', u'hello01bb']]
    """
    new_name_list = []
    r = re.compile(search_word)
    for name in name_list:
        if regex:
            new_name = r.sub(text_word, name)
        else:
            start_pos = name.find(search_word)
            if start_pos >= 0:
                end_pos = start_pos + len(search_word)
                new_name = "{0}{1}{2}".format(name[:start_pos], text_word, name[end_pos:])
            else:
                new_name = name
        new_name_list.append(new_name)

    # マジックワードの置換
    new_name_list = _replace_magic_word(new_name_list)

    result = [[name, new_name_list[index]] for index, name in enumerate(name_list)]
    return result


def add(name_list, text_word, position=POSITION_START):
    u"""追加を行なう。

    :type name_list: list of unicode
    :type text_word: unicode
    :type position: unicode
    :rtype: list of tuple

    >>> add([u"aaa", u"bbb"], u"Pre##_")
    [[u'aaa', u'Pre01_aaa'], [u'bbb', u'Pre02_bbb']]
    >>> add([u"aaa", u"bbb"], u"Pre##_", POSITION_END)
    [[u'aaa', u'aaaPre01_'], [u'bbb', u'bbbPre02_']]
    """
    new_name_list = []
    r = re.compile(position)
    for name in name_list:
        new_name = r.sub(text_word, name)
        new_name_list.append(new_name)

    # マジックワードの置換
    new_name_list = _replace_magic_word(new_name_list)

    result = [[name, new_name_list[index]] for index, name in enumerate(name_list)]
    return result


def search(name_list, search_word, regex=False):
    u"""検索を行なう。

    :type name_list: list of unicode
    :type search_word: unicode
    :type regex: bool
    :rtype: list of tuple

    >>> search([u"aaab", u"bbbb"], u"bb")
    [[u'aaab', False], [u'bbbb', True]]
    >>> search([u"aaab", u"bbbb"], u"a{3}b", True)
    [[u'aaab', True], [u'bbbb', False]]
    """
    result = []
    r = re.compile(search_word)
    for name in name_list:
        if regex:
            m = r.search(name)
            find_flag = True if m else False
        else:
            m = name.find(search_word)
            find_flag = True if m >= 0 else False

        result.append([name, find_flag])

    return result


if __name__ == u"__main__":
    doctest.testmod()
