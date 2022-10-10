import unittest

from elastic_tabs import BlockSplitter, Line, Block

blank = Line("", "\n")
foo = Line("foo", "\n")
v_bar = Line("\vbar", "\n")
bar_v = Line("bar\v", "\n")
baz = Line("bar", "\n")


class ChunkSplitterTest(unittest.TestCase):
    def test_vertical_tab_beginning(self):
        splitter = BlockSplitter()
        splitter.add_lines([foo, v_bar, baz])
        splitter.flush()
        self.assertEqual([Block([foo]), Block([v_bar, baz])], splitter.blocks())

    def test_vertical_tab_end(self):
        splitter = BlockSplitter()
        splitter.add_lines([foo, bar_v, baz])
        splitter.flush()
        self.assertEqual([Block([foo, bar_v]), Block([baz])], splitter.blocks())

    def test_blank_line(self):
        splitter = BlockSplitter()
        splitter.add_lines([foo, blank, baz])
        splitter.flush()
        # TODO should the blank line be in a separate block?
        self.assertEqual([Block([foo, blank]), Block([baz])], splitter.blocks(clear=False))
        self.assertEqual([Block([foo, blank]), Block([baz])], splitter.blocks())
        self.assertEqual([], splitter.blocks())


if __name__ == '__main__':
    unittest.main()
