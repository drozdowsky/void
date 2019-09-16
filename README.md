## Void
Void object in Python
[pypi](https://pypi.org/project/void/)

## Installation
```shell
pip install void
```

## Example usage
```python
from void import Void

In [1]: Void is Void() is Void.method()
Out[1]: True

In [2]: Void['get']['void'] is Void
Out[2]: True

In [3]: [for x in Void]
Out[3]: []

In [4]: Void['set'] = 123
        Void['set'] is Void
Out[4]: True

In [5]: int(Void)
Out[5]: 0
```

## TODO
- [] more tests around arithetic operations
- [] str should return '', repr 'Void'
- [] consider int(Void) to return Void
