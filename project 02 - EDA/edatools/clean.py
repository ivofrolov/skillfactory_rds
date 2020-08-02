from pandas import DataFrame


def check_anomalies(df: DataFrame, actions: dict) -> dict:
    """Returns values from the dataset that do not meet certain restrictions

    Key of `actions` dict is a column name, and value is a dict of any supported actions:
        `restrict`: tuple -- restrict field to a list of possible values
    """
    result = {}
    for column, action in actions.items():
        possible_values = set(action.get('restrict'))
        if possible_values:
            diff = set(df.loc[:, column].dropna().unique()) - possible_values
            if diff:
                counts = df.loc[:, column].value_counts()
                result[column] = {value: counts[value] for value in diff}
    return result


def most_common(df: DataFrame, columns: list, threshold: float = .75) -> dict:
    """Yields most common values in each of nominative variables in dataset"""
    for column in columns:
        sample = df[column].agg(lambda s: s.value_counts() / s.count())
        result = sample[sample > threshold]
        if not result.empty:
            yield column, result.idxmax()
