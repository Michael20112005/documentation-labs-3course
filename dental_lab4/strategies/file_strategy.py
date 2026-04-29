from strategies.output_strategy import OutputStrategy


class FileOutputStrategy(OutputStrategy):
    def __init__(self, output_file):
        self.output_file = output_file

    def output(self, rows):
        with open(self.output_file, "w", encoding="utf-8") as file:
            for row in rows:
                file.write(str(row) + "\n")