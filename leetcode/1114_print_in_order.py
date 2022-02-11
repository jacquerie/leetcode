# -*- coding: utf-8 -*-

from unittest.mock import Mock, call
from threading import Barrier, Thread
from typing import Callable


class Foo:
    def __init__(self):
        self.fb = Barrier(2)
        self.sb = Barrier(2)

    def first(self, printFirst: "Callable[[], None]") -> None:
        printFirst()
        self.fb.wait()

    def second(self, printSecond: "Callable[[], None]") -> None:
        self.fb.wait()
        printSecond()
        self.sb.wait()

    def third(self, printThird: "Callable[[], None]") -> None:
        self.sb.wait()
        printThird()


if __name__ == "__main__":
    mock = Mock(return_value=None)

    def printFirst():
        mock("first")

    def printSecond():
        mock("second")

    def printThird():
        mock("third")

    foo = Foo()
    ft = Thread(target=foo.first, args=(printFirst,))
    st = Thread(target=foo.second, args=(printSecond,))
    tt = Thread(target=foo.third, args=(printThird,))
    ft.start()
    st.start()
    tt.start()

    ft.join()
    st.join()
    tt.join()
    assert [
        call("first"),
        call("second"),
        call("third"),
    ] == mock.mock_calls

    mock.reset_mock()

    foo = Foo()
    ft = Thread(target=foo.first, args=(printFirst,))
    st = Thread(target=foo.second, args=(printSecond,))
    tt = Thread(target=foo.third, args=(printThird,))
    ft.start()
    tt.start()
    st.start()

    ft.join()
    st.join()
    tt.join()
    assert [
        call("first"),
        call("second"),
        call("third"),
    ] == mock.mock_calls
