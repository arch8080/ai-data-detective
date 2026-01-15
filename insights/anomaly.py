import pandas as pd
import numpy as np

def detect_anomalies(df: pd.DataFrame, z_threshold: float = 3.0):
    anomalies = {}

    numeric_cols = df.select_dtypes(include="number")

    for col in numeric_cols.columns:
        series = numeric_cols[col].dropna()
        if series.empty:
            continue

        z_scores = np.abs((series - series.mean()) / series.std())
        outliers = series[z_scores > z_threshold]

        if not outliers.empty:
            anomalies[col] = {
                "count": len(outliers),
                "examples": outliers.head(5).tolist()
            }

    return anomalies
