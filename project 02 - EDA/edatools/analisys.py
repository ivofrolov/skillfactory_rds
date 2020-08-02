from itertools import combinations
from pandas import DataFrame
from scipy.stats import ttest_ind


def stat_diff(
        df: DataFrame,
        var_col: str,
        char_col: str,
        max_chars: int = 10) -> bool:
    """Returns whether there is a statistical difference in the distribution
    of studied variable (`var_col`) by nominative characteristics (`char_col`)
    """
    char_sample = df.loc[:, char_col]
    char_combs = list(combinations(char_sample.value_counts().index[:10], 2))
    for comb in char_combs:
        result = ttest_ind(df.loc[char_sample == comb[0], var_col],
                           df.loc[char_sample == comb[1], var_col])
        # Bonferroni correction
        if result.pvalue <= 0.05 / len(char_combs):
            return True
    return False
