import json

import google.cloud.pubsub_v1 as pubsub
from nest.core import Controller, Depends, Post

from src.api.service import AnalyticsService


@Controller("analytics")
class AnalyticsController:

    service: AnalyticsService = Depends(AnalyticsService)

    @Post("/publish_analytics")
    async def publish_analytics(self):
        request = {
            "data": {"": ""},
            "ties": True,
            "target_col": "Electric Vehicles Revenue",
            "date_col": "Calendar Date",
            "user_id": "user1",
            "session_id": "session1",
            "external_data_id": "data1",
        }

        publisher = pubsub.PublisherClient()
        topic_path = "projects/ezml-dev-417920/topics/run-xicorr"
        payload = json.dumps(request).encode("utf-8")
        future = publisher.publish(topic_path, data=payload)
        return {"message": f"Published message ID {future.result()}"}
