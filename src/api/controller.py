from nest.core import Controller, Depends, Post

from src.api.service import AnalyticsService


@Controller("analytics")
class AnalyticsController:

    service: AnalyticsService = Depends(AnalyticsService)

    @Post("/publish_analytics")
    async def publish_analytics(self):
        payload = [{
            "data": {"": ""},
            "ties": True,
            "target_col": "Electric Vehicles Revenue",
            "date_col": "Calendar Date",
            "user_id": "user1",
            "session_id": "session1",
            "external_data_id": "data1",
        }]
        return payload
