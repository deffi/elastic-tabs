from elastic_tabs import Filter
from elastic_tabs.text import splitlines


class StreamFilter:
    def __init__(self, stream):
        self.stream = stream
        self.filter = Filter()
        self._buffer = ""

    def __getattr__(self, name):
        return getattr(self.stream, name)

    def render_tables(self):
        for table in self.filter.render_tables():
            print(table, file=self.stream)

    def write(self, data):
        self._buffer += data
        lines, self._buffer = splitlines(self._buffer)

        for line in lines:
            self.filter.add_line(line)
        self.render_tables()
        # self.stream.flush()

    def flush(self):
        self.filter.flush()
        self.render_tables()

        self.stream.flush()

# sys.stdout = MyFilter(sys.stdout)
# sys.stderr = MyFilter(sys.stderr)
