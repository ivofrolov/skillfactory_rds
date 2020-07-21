import pandas as pd


def check_anomalies(df: pd.DataFrame, actions: dict) -> dict:
    """Check if some values are 

    Key of `actions` parameter is a column name, and value is a dict of any supported actions:
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
