import unittest
import pytest

type = pytest.config.option.type
env = pytest.config.option.env

print('type',type)
print('env',env)


if __name__ == '__main__':
    unittest.main()
