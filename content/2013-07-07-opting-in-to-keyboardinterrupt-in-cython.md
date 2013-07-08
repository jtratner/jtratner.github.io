Layout: post
Title: Opting in to KeyboardInterrupt in Cython
Date: 2013-07-07 20:52
Comments: true
Category: Python
Tags: Cython,Python

One side-effect of using Cython is that code won't stop when you try to stop it
with `^C` (because it ignores `KeyboardInterrupt`). Simple to handle, but it
took me a while to figure out just the right commands. You just need to use
`PyErr_CheckSignals` from `cpython.exc`. You either want to wrap in `try/except`
clause or put it outside of wherever you want to handle your loop. It also
doesn't call the GIL so it's safe to call.

```cython
from cpython.exc cimport PyErr_CheckSignals
```

This adds very little overhead. If you compare two functions:

```cython
cpdef raise_on_error(): PyErr_CheckSignals()
cpdef reference(): pass
```

You see a *very* small overhead for calling `PyErr_CheckSignal`. 

```ipython
In [4]: %timeit check_signal()
10000000 loops, best of 3: 72.8 ns per loop

In [5]: %timeit reference()
10000000 loops, best of 3: 67.6 ns per loop
```
