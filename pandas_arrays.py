#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Pandas."""

import pandas as pd
from pprint import pprint


class PandasOOP:

    def ex_one(self):
        """Task #1"""
        df = pd.read_excel('pandas_data/data.xls', sheetname='Sheet1')
        pprint(df)

    def ex_two(self):
        """Task #2"""
        df = pd.read_excel('pandas_data/data.xls', sheetname='Sheet1')
        pprint(df.groupby('sex#')['age'].mean())

    def ex_three(self):
        """Task #3"""
        df = pd.read_excel('pandas_data/data.xls', sheetname='Sheet1')
        pprint(df.groupby('sex#')['brainwt'].max())

    def ex_four(self):
        """Task #4"""
        df = pd.read_excel('pandas_data/data.xls', sheetname='Sheet1')
        pprint(df[(df['ID'] == 1709)]['sex'])

    def ex_five(self):
        """Task #5"""
        df = pd.read_excel('pandas_data/data.xls', sheetname='Sheet1')
        pprint(df[(df['brainwt'] == df['brainwt'].max())]['ID'])

    def ex_six(self):
        """Task #6"""
        df = pd.read_excel('pandas_data/data.xls', sheetname='Sheet1')
        pprint(df['sex#'].value_counts())

    def ex_seven(self):
        """Task #7"""
        df = pd.read_excel('pandas_data/data.xls', sheetname='Sheet1')
        df_strains = df['Strain'].unique()
        pprint(df_strains)
        pprint(len(df_strains))

    def ex_eight(self):
        """Task #8"""
        df = pd.read_excel('pandas_data/data.xls', sheetname='Sheet1')
        pprint(df.groupby('sex#')['brainwt', 'bodywt'].mean())

pandas_oop = PandasOOP()
pandas_oop.ex_one()
pandas_oop.ex_two()
pandas_oop.ex_three()
pandas_oop.ex_four()
pandas_oop.ex_five()
pandas_oop.ex_six()
pandas_oop.ex_seven()
pandas_oop.ex_eight()
