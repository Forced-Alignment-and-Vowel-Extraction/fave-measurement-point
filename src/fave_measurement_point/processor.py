from fave_measurement_point.formants import FormantArray
import yaml
import re
import functools

def rgetattr(obj, 
             attr : str, 
             *args):
    """_gets object attribute from string_

    Args:
        obj (_type_): _object_
        attr (_str_): attribute path attr.attr.attr
    """
    def _getattr(obj, attr: str):
        try:
            return getattr(obj, attr, *args)
        except:
            return ''
    return functools.reduce(_getattr, [obj] + attr.split('.'))

