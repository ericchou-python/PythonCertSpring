#!/usr/bin/env python

"""
example code for properties
"""

class C(object):
    _x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "docstring")

if __name__ == "__main__":
    c = C()
    c.x = 5
    print c.x
    c.x = 3
    print c.x

