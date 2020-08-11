r"""Test `lmp.tokenizer.WhitespaceListTokenizer.reset_vocab`.

Usage:
    python -m unittest \
        test/lmp/tokenizer/_whitespace_list_tokenizer/test_reset_vocab.py
"""

# built-in modules

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import gc
import inspect
import unittest

# self-made modules

from lmp.tokenizer import WhitespaceListTokenizer


class TestResetVocab(unittest.TestCase):
    r"""Test case for `lmp.tokenizer.WhitespaceListTokenizer.reset_vocab`."""

    def setUp(self):
        r"""Setup both cased and uncased tokenizer instances."""
        self.cased_tokenizer = WhitespaceListTokenizer()
        self.uncased_tokenizer = WhitespaceListTokenizer(is_uncased=True)
        self.tokenizers = [self.cased_tokenizer, self.uncased_tokenizer]

    def tearDown(self):
        r"""Delete both cased and uncased tokenizer instances."""
        del self.tokenizers
        del self.cased_tokenizer
        del self.uncased_tokenizer
        gc.collect()

    def test_signature(self):
        r"""Ensure signature consistency."""
        msg = 'Inconsistent method signature.'

        self.assertEqual(
            inspect.signature(WhitespaceListTokenizer.reset_vocab),
            inspect.Signature(
                parameters=[
                    inspect.Parameter(
                        name='self',
                        kind=inspect.Parameter.POSITIONAL_OR_KEYWORD,
                        default=inspect.Parameter.empty
                    ),
                ],
                return_annotation=None
            ),
            msg=msg
        )

    def test_token_to_id_existence(self):
        r"Test whether create `token_to_id` in `reset_vocab`"
        msg1 = 'Missing class attribute `{}`.'
        msg2 = 'Class attribute `{}` must be an instance of `{}`.'
        msg3 = 'Class attribute `{}` must be `{}`.'

        examples = (
            (
                'token_to_id',
                ['[BOS]', '[EOS]', '[PAD]', '[UNK]']
            ),
        )

        for attr, attr_val in examples:
            for tokenizer in self.tokenizers:
                self.assertTrue(
                    hasattr(tokenizer, attr),
                    msg=msg1.format(attr)
                )
                self.assertIsInstance(
                    getattr(tokenizer, attr),
                    type(attr_val),
                    msg=msg2.format(attr, type(attr_val).__name__)
                )
                self.assertEqual(
                    getattr(tokenizer, attr),
                    attr_val,
                    msg=msg3.format(attr, attr_val)
                )


if __name__ == '__main__':
    unittest.main()
