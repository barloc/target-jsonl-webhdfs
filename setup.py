#!/usr/bin/env python
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name='target-jsonl-webhdfs',
    version='0.1.4.1',
    description='Singer.io target for writing JSON Line files via webhdfs',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Stanislav Lysikov',
    author_email="stave.tx@gmail.com",
    url="https://github.com/barloc/target-jsonl-webhdfs",
    keywords=["singer", "singer.io", "target", "etl",],
    classifiers=['Programming Language :: Python :: 3 :: Only'],
    py_modules=['target_jsonl_webhdfs'],
    install_requires=[
        'jsonschema==2.6.0',
        'singer-python==5.8.0',
        'adjust-precision-for-schema==0.3.3',
        'hdfs==2.7.0',],
    entry_points='''
          [console_scripts]
          target-jsonl-webhdfs=target_jsonl_webhdfs:main
      ''',
)
