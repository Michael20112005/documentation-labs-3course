from strategies.output_strategy import OutputStrategy


class KafkaOutputStrategy(OutputStrategy):
    def output(self, rows):
        for row in rows:
            print(f"[Kafka] Sending row to Kafka: {row}")