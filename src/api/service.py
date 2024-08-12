import google.cloud.pubsub_v1 as pubsub


class AnalyticsService:

    def input_analytics(self, payload):
        with open("payload.json", "w") as f:
            f.write(str(payload))
        
    
    def publish_analytics(self):
        publisher = pubsub.PublisherClient() 
        topic_path = publisher.topic_path("ezml-dev-417920", "run-xicorr")
        for payload in self.input_analytics():
            publisher.publish(topic_path, data=payload)
        return "Published analytics"

