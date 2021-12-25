import importlib


def str_to_class(package, class_name):
    module = importlib.import_module(f'{package}.{class_name}')
    return getattr(module, class_name)
