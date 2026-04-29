class InspectionService:
    def __init__(self, reader, output_strategy):
        self.reader = reader
        self.output_strategy = output_strategy

    def process(self):
        rows = self.reader.read()
        self.output_strategy.output(rows)