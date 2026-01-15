import plotly.express as px
import pandas as pd
from visualization.visual_spec import VisualizationSpec


def create_plot(df: pd.DataFrame, spec: VisualizationSpec):
    chart_type = spec.chart_type

    if chart_type == "line":
        return px.line(
            df,
            x=spec.x,
            y=spec.y,
            title=spec.title
        )

    if chart_type == "bar":
        return px.bar(
            df,
            x=spec.x,
            y=spec.y,
            title=spec.title
        )

    if chart_type == "scatter":
        return px.scatter(
            df,
            x=spec.x,
            y=spec.y[0] if spec.y else None,
            title=spec.title
        )

    if chart_type == "histogram":
        return px.histogram(
            df,
            x=spec.x,
            title=spec.title
        )

    if chart_type == "heatmap":
        corr = df.corr(numeric_only=True)
        return px.imshow(
            corr,
            text_auto=True,
            title=spec.title
        )

    return None
