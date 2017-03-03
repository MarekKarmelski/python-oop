#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rpsls.element import Element

"""Spock class."""


class Spock(Element):

    name = 'SPOCK'
    traversed_by = ['LIZARD', 'PAPER']
    beats = ['SCISSORS', 'ROCK']
