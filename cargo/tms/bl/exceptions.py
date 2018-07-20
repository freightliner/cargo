#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class IllegalStateException(RuntimeError):
    def __init__(self, msg):
        super.__init(msg)
        

class OperationNotAllowedException(RuntimeError):
    def __init__(self, msg):
        super.__init__(msg)

