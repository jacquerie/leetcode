# -*- coding: utf-8 -*-

from unittest.mock import Mock, call
from threading import Event, Thread


class FooBar(object):
    def __init__(self, n):
        self.fe = Event()
        self.be = Event()
        self.n = n

    def foo(self, printFoo):
        for i in range(self.n):
            if i > 0:
                self.fe.wait()
            self.fe.clear()
            printFoo()
            self.be.set()

    def bar(self, printBar):
        for i in range(self.n):
            self.be.wait()
            self.be.clear()
            printBar()
            self.fe.set()


if __name__ == '__main__':
    mock = Mock(return_value=None)

    def printFoo():
        mock('foo')

    def printBar():
        mock('bar')

    foobar = FooBar(2)
    ft = Thread(target=foobar.foo, args=(printFoo,))
    bt = Thread(target=foobar.bar, args=(printBar,))
    ft.start()
    bt.start()

    ft.join()
    bt.join()
    assert [
        call('foo'),
        call('bar'),
        call('foo'),
        call('bar'),
    ] == mock.mock_calls
