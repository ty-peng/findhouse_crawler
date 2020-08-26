# -*- coding: utf-8 -*-
import base64
import io
import logging

from fontTools.ttLib import TTFont


def handle_58font(base64_str, to_decode):
    """ 处理58同城的字体加密.

    :param base64_str: 页面 script 中的 base64 字符串
    :param to_decode: 待解析的字符串
    :return: 解析结果
    """
    font = TTFont(io.BytesIO(base64.decodebytes(base64_str.encode())))
    cmap = font['cmap'].tables[0].ttFont.tables['cmap'].tables[0].cmap
    result = []
    try:
        for c in to_decode:
            if ord(c) in cmap:
                text = str(int(cmap[ord(c)][-2:]) - 1)
            else:
                text = c
            result.append(text)
    except Exception as e:
        logging.error(e)
    return ''.join(result)
