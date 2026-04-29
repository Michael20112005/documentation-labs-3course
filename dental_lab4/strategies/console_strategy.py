from strategies.output_strategy import OutputStrategy


class ConsoleOutputStrategy(OutputStrategy):
    def output(self, rows):
        for row in rows:
            print(row)