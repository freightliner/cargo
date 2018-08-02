#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class IllegalStateException(RuntimeError):
    def __init__(self, str = ''):
        RuntimeError.__init__(self, str)
        
class OperationNotAllowedException(RuntimeError):
    def __init__(self, str = ''):
        RuntimeError.__init__(self, str)

class UnsupportedOperationException(RuntimeError):
    def __init__(self, str = ''):
        RuntimeError.__init__(self, str)
