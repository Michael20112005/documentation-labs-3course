from strategies.output_strategy import OutputStrategy


class RedisOutputStrategy(OutputStrategy):
    def output(self, rows):
        for index, row in enumerate(rows):
            print(f"[Redis] Saving row with key inspection:{index}: {row}")