r"""Test `lmp.model._res_lstm_block.py`.

Usage:
    python -m unittest test.lmp.model._res_lstm_block.__init__
"""

# built-in modules

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import inspect
import unittest


class TestResLSTMBlock(unittest.TestCase):
    r"""Test case for `lmp.model._res_lstm_block.py`."""

    def test_signature(self):
        r"""Ensure signature consistency."""
        msg = 'Inconsistent module signature.'

        try:
            # pylint: disable=C0415
            import lmp
            import lmp.model
            import lmp.model._res_lstm_block
            # pylint: enable=C0415

            # pylint: disable=W0212
            self.assertTrue(
                inspect.ismodule(lmp.model._res_lstm_block),
                msg=msg
            )
            # pylint: enable=W0212
        except ImportError:
            self.fail(msg=msg)

    def test_module_attributes(self):
        r"""Declare required module attributes."""
        msg1 = 'Missing module attribute `{}`.'
        msg2 = 'Module attribute `{}` must be a class.'
        msg3 = 'Inconsistent module signature.'
        examples = ('ResLSTMBlock',)

        try:
            # pylint: disable=C0415
            import lmp
            import lmp.model
            import lmp.model._res_lstm_block
            # pylint: enable=C0415

            for attr in examples:
                self.assertTrue(
                    hasattr(lmp.model._res_lstm_block, attr),
                    msg=msg1.format(attr)
                )
                self.assertTrue(
                    inspect.isclass(getattr(
                        lmp.model._res_lstm_block,
                        attr
                    )),
                    msg=msg2.format(attr)
                )
        except ImportError:
            self.fail(msg=msg3)


if __name__ == '__main__':
    unittest.main()
