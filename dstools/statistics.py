from pandas import Series


def typical_range(series: Series, interpolation: str = 'midpoint') -> tuple:
    """Return "minimum" and "maximum" of data sample.

    These values are whiskers in a box plot and can be used to identify outliers.
    First is Q1 - 1.5*IQR (interquartile range: Q3 - Q1), second -- Q3 + 1.5*IQR.

    >>> typical_range(Series([1,2,3,4,5,6,7]))
    (-2.0, 10.0)
    """
    q1, q3 = list(series.quantile([.25, .75], interpolation=interpolation))
    one_and_half_iqr = 1.5 * (q3 - q1)
    return (q1 - one_and_half_iqr, q3 + one_and_half_iqr)


def has_outliers(series: Series) -> bool:
    """Return whether any value in data sample is out of typical range.

    >>> has_outliers(Series([1,2,3,4,5,6,7]))
    False

    >>> has_outliers(Series([1,2,3,4,5,6,12]))
    True
    """
    lower, upper = typical_range(series)
    return series.min() < lower or series.max() > upper


def loc_outliers(series: Series) -> list:
    """Return a boolean array to locate outliers in `pandas.Series` data sample

    >>> loc_outliers(Series([1,2,3,4,5,6,12]))
    [False, False, False, False, False, False, True]
    """
    lower, upper = typical_range(series)
    return [item < lower or item > upper for item in series]


def expected_value(series: Series) -> float:
    """Return mathematical expectation of indexed value in serie of it's probabilities

    >>> round(expected_value(Series([.5,.3,.2], [1,2,3])), 1)
    1.7
    """
    return sum([v*p for v,p in series.items()])
