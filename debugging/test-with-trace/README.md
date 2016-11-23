Tool for tracing individual python unit tests between branches and comparing the trace.
Requires that you've got the unit test available in two git branches.

usage: test-with-trace <unit-test> <branch1> <branch2>
    - Runs the unit-test on both branches, writing the trace out to <branch1>.txt and <branch2>.txt

usage: test-with-trace.py <some-unit-test>
       - Writes out the trace from running the unit test

