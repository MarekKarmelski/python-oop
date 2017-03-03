#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rpsls.element import Element

"""Paper class."""


class Paper(Element):

    name = 'PAPER'
    traversed_by = ['LIZARD', 'SCISSORS']
    beats = ['ROCK', 'SPOCK']
