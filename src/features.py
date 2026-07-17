def anuity_per_income(df):
    df["annuity_to_income"] = df["AMT_ANNUITY"] / df["AMT_INCOME_TOTAL"]
    return df.groupby("TARGET")["annuity_to_income"].mean()
