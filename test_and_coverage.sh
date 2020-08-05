#!/bin/sh

echo "\nTesting and checking coverage for Python code\n"

COV_THRESHOLD=100;
coverage run -m pytest
coverage report -m
