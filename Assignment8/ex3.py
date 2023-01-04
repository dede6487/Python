class Aggregator:

    def __init__(self, agg_type: type, ignore_errors: bool = True):
        self.agg_type = agg_type
        self.ignore_errors = ignore_errors

    def __call__(self, *args):

