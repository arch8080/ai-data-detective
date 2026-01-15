import pandas as pd

def run_eda(df: pd.DataFrame) -> dict:
    summary = {}

    summary["rows"] = df.shape[0]
    summary["columns"] = df.shape[1]

    summary["missing_values"] = (
        df.isna().sum()
        .sort_values(ascending=False)
        .to_dict()
    )

    summary["numeric_columns"] = df.select_dtypes(include="number").columns.tolist()
    summary["categorical_columns"] = df.select_dtypes(exclude="number").columns.tolist()

    if summary["numeric_columns"]:
        summary["correlations"] = (
            df[summary["numeric_columns"]]
            .corr()
            .round(3)
            .to_dict()
        )
    else:
        summary["correlations"] = {}

    return summary
