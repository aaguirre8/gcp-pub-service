from src.api.controller import AnalyticsController
from src.api.service import AnalyticsService


class AnalyticsModule:
    def __init__(self):
        self.providers = [AnalyticsService]
        self.controllers = [AnalyticsController]