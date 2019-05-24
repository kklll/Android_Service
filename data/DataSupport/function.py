# coding=utf-8
import types


def to_dict(dumyself):
    result = {}
    for a in dir(dumyself):

        # filter inner field by fieldname
        if a.startswith('_') or a == 'metadata':
            continue

        v = getattr(dumyself, a)

        # filter inner field by value type
        if callable(v):
            continue

        if type(v) not in (types.NoneType, types.IntType, types.LongType, types.StringType, types.UnicodeType):
            continue

        result[a] = getattr(dumyself, a)

    return result