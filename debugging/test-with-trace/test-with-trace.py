#!/usr/bin/env python

from __future__ import print_function
import sys
from test.unit.clarity_ext.dilution.test_dilutions import TestDilutionScheme
import unittest
import trace

def run_test(name, ignore):
    """Runs a unit test with tracing"""
    suite = unittest.TestLoader().loadTestsFromName(name)
    fn = lambda: unittest.TextTestRunner(verbosity=2).run(suite)
    # TODO: Ignore does not take full paths of modules!
    tracer = trace.Trace(ignoremods=ignore, ignoredirs=[sys.prefix, sys.exec_prefix],
                         trace=1,
                         count=0)
    tracer.runfunc(fn)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_name = sys.argv[1]
    ignore = sys.argv[2].split(",") if len(sys.argv) > 2 else list()
    run_test(test_name, ignore)

