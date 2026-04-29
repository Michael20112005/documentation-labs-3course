import json

from reader.csv_reader import CSVReader
from service.inspection_service import InspectionService

from strategies.console_strategy import ConsoleOutputStrategy
from strategies.file_strategy import FileOutputStrategy
from strategies.kafka_strategy import KafkaOutputStrategy
from strategies.redis_strategy import RedisOutputStrategy


def create_strategy(config):
    strategy_name = config["output_strategy"]

    if strategy_name == "console":
        return ConsoleOutputStrategy()

    if strategy_name == "file":
        return FileOutputStrategy(config["output_file"])

    if strategy_name == "kafka":
        return KafkaOutputStrategy()

    if strategy_name == "redis":
        return RedisOutputStrategy()

    raise ValueError(f"Unknown output strategy: {strategy_name}")


def main():
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)

    reader = CSVReader(
        file_path=config["input_file"],
        limit=config["limit"]
    )

    strategy = create_strategy(config)

    service = InspectionService(reader, strategy)
    service.process()

    print("DONE: Data processed successfully")


if __name__ == "__main__":
    main()