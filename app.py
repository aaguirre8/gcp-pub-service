from nest.core.app import App

from src.api.module import AnalyticsModule

app = App(
    description="PyNest service",
    modules=[
        AnalyticsModule,
    ]
)
