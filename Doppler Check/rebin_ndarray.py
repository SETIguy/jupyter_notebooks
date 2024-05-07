
def rebin_ndarray(ndarray, new_shape, operation='sum'):
    """
    Modified version of https://gist.github.com/derricw/95eab740e1b08b78c03f
    Rebins an ndarray in all axes based on the target shape, by summing or
        averaging, or local minimum/maximum.
    Number of output dimensions must match number of input dimensions.
    Example
    -------
    >>> m = np.arange(0,100,1).reshape((10,10))
    >>> n = bin_ndarray(m, new_shape=(5,5), operation='sum')
    >>> print(n)
    [[ 22  30  38  46  54]
     [102 110 118 126 134]
     [182 190 198 206 214]
     [262 270 278 286 294]
     [342 350 358 366 374]]
    """
    if not operation.lower() in ['sum', 'mean', 'average', 'avg', 'min', 'max', 'median']:
        raise ValueError("Operation {} not supported.".format(operation))
    if ndarray.ndim != len(new_shape):
        raise ValueError("Shape mismatch: {} -> {}".format(ndarray.shape,
                                                           new_shape))
    compression_pairs = [(d, c//d) for d, c in zip(new_shape,
                                                   ndarray.shape)]
    flattened = [l for p in compression_pairs for l in p]
    flattened=[1 if x == 0 else x for x in flattened]
    print (flattened)
    ndarray = ndarray.reshape(flattened)
    for i in range(len(new_shape)):
        if operation.lower() == "sum":
            ndarray = ndarray.sum(-1*(i+1))
        elif operation.lower() == "max":
            ndarray = ndarray.max(-1*(i+1))
        elif operation.lower() == "min":
            ndarray = ndarray.min(-1*(i+1))
        elif operation.loger() == "median":
            ndarray = ndarray.median(-1*(i+1))
        elif operation.lower() in ["mean", "average", "avg"]:
            ndarray = ndarray.mean(-1*(i+1))
    return ndarray

