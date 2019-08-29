from six import with_metaclass


class __MetaVoid(type):
    def __getattr__(cls, *args, **kwargs):
        return cls

    def __call__(cls, *args, **kwargs):
        return cls

    def __getitem__(cls, *args, **kwargs):
        return cls

    def __setitem__(cls, *args, **kwargs):
        pass

    def __enter__(cls, *args, **kwargs):
        return cls

    def __exit__(cls, *args, **kwargs):
        return None

    def __str__(cls, *args, **kwargs):
        return 'Void'

    def __repr__(cls, *args, **kwargs):
        return ''

    def __iter__(cls, *args, **kwargs):
        return cls

    def __next__(cls, *args, **kwargs):
        raise StopIteration

    def next(cls, *args, **kwargs):
        return cls.__next__(cls, *args, **kwargs)

    def __lt__(cls, _):
        return True

    def __le__(cls, _):
        return True

    def __gt__(cls, _):
        return False

    def __ge__(cls, _):
        return False

    def __int__(cls):
        return 0

    __add__ = __sub__ = __mul__ = __pow__ = __truediv__ = __floordiv__ = __getattr__
    __mod__ = __lshift__ = __rshift__ = __getattr__
    __and__ = __or__ = __xor__ = __invert__ = __getattr__
    __pos__ = __neg__ = __getattr__
    __long__ = __float__ = __oct__ = __hex__ = __int__


class Void(with_metaclass(__MetaVoid, object)):
    def __new__(cls, *args, **kwargs):
        return cls
