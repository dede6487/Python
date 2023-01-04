class Aggregator:

    def __init__(self, agg_type: type, ignore_errors: bool = True):
        self.agg_type = agg_type
        self.ignore_errors = ignore_errors
        self.agg = None

    def _call_add_helper(self, *args):
        for arg in args:
            if self.agg is None:
                self.agg = arg
            else:
                self.agg += arg

    def __call__(self, *args):
        if self.ignore_errors:
            nargs = [value for value in args if type(value) == self.agg_type]
            # just stores the elements of args which are of type agg_type
            for arg in nargs:
                if self.agg is None:
                    self.agg = arg
                else:
                    self.agg += arg
        else:
            for arg in args:
                if not isinstance(arg, self.agg_type):
                    raise TypeError(f"aggregation only works on type '{self.agg_type}', not '{type(arg)}'")
                else:
                    if self.agg is None:
                        self.agg = arg
                    else:
                        self.agg += arg
        return self.agg
