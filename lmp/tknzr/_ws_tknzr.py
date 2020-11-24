r"""Whitespace :term:`tokenizer` class."""

import re
from typing import List, Sequence

from lmp.tknzr._base_tknzr import BaseTknzr


class WsTknzr(BaseTknzr):
    r"""Whitespace :term:`tokenizer` class.

    Tokenize text into (unicode) whitespace seperate tokens.
    No whitespace will be preserved after tokenization.

    Parameters
    ==========
    is_uncased: bool
        See attributes for details.
    max_vocab: int
        See attributes for details.
    min_count: int
        See attributes for details.
    tk2id: Dict[str, int], optional
        Token (a string) to id (an integer) lookup table.
        If ``tk2id is not None``, then initialize lookup table with ``tk2id``.
        Otherwise initialize lookup table with special tokens only.
        See attributes for details.

    Attributes
    ==========
    bos_tk: ClassVar[str]
        Token which represents the begining of a text.
        Text will be prepended with ``self.__class__.bos_tk`` when encoded by
        ``self.enc()``.
    bos_tkid: ClassVar[int]
        Token id of ``self.__class__.bos_tk``.
    eos_tk: ClassVar[str]
        Token which represents the end of a text.
        Text will be appended with ``self.__class__.eos_tk`` when encoded by
        ``self.enc()``.
    eos_tkid: ClassVar[int]
        Token id of ``self.__class__.eos_tk``.
    file_name: ClassVar[str]
        Tokenizer's configuration output file name.
    id2tk: Dict[int, str]
        Id (an integer) to token (a string) lookup table.
    is_uncased: bool
        When performing ``self.norm()``, convert text into lowercase if
        ``self.is_uncased == True``.
    max_vocab: int
        Maximum vocabulary size.
    min_count: int
        Minimum token frequency for each token to be included in tokenizer's
        vocabulary.
    pad_tk: ClassVar[str]
        Token which represents paddings of a text.
        Text may be appended with ``self.__class__.pad_tk`` when encoded by
        ``self.enc()``.
    pad_tkid: ClassVar[int]
        Token id of ``self.__class__.pad_tk``.
    tk2id: Dict[str, int]
        Token (a string) to id (an integer) lookup table.
    tknzr_name: ClassVar[str]
        Display name for tokenizer on CLI.
        Used only for command line argument parsing.
    unk_tk: ClassVar[str]
        Token which represents unknown tokens in a text.
        Tokens in text may be replaced with ``self.__class__.unk_tk`` when
        encoded by ``self.enc()``.
    unk_tkid: ClassVar[int]
        Token id of ``self.__class__.unk_tk``.
        Token ids in a sequence may be replaced with
        ``self.__class__.unk_tkid`` when decoded by ``self.dec()``.

    Raises
    ======
    TypeError
        When parameters are not confront their respective type annotation.

    Examples
    ========
    >>> from typing import List, Sequence
    >>> from lmp.tknzr import WsTknzr
    >>> tknzr = WsTknzr(is_uncased=False, max_vocab=10, min_count=2)
    >>> tknzr.tknz('a b c')
    ['a', 'b', 'c']
    >>> tknzr.dtknz(['a', 'b', 'c'])
    'a b c'
    """

    def tknz(self, txt: str) -> List[str]:
        r"""Perform whitespace :term:`tokenization` on text.

        Text will first be normalized and then be tokenized using whitespace
        as separation.

        Parameters
        ==========
        txt: str
            Text to be tokenized.

        Returns
        =======
        List[str]
            List of normalized tokens tokenized from text.
            No whitespace will be preserved after tokenization.

        See Also
        ========
        lmp.tknzr.WsTknzr.dtknz
        lmp.tknzr.BaseTknzr.norm

        Examples
        ========
        >>> from lmp.tknzr import WsTknzr
        >>> tknzr = WsTknzr(is_uncased=False, max_vocab=10, min_count=2)
        >>> tknzr.tknz('a b c')
        ['a', 'b', 'c']
        >>> tknzr.tknz('abc def')
        ['abc', 'def']
        """
        # First do normalization, then perform tokenization.
        tks = re.split(r'\s+', self.norm(txt))

        # Return empty list when `txt` is empty string.
        # This is needed since `re.split(r'\s+', '')` return `['']` instead of
        # `[]`.
        if tks == ['']:
            return []
        return tks

    def dtknz(self, tks: Sequence[str]) -> str:
        r"""Convert :term:`tokens` back to one and only one text.

        Tokens are simply joined with single whitespace and then normalized.

        Parameters
        ==========
        tks: Seqeuence[str]
            Sequence of tokens to be detokenized.

        Returns
        =======
        str
            Normalized text with whitespaces in between each token.

        See Also
        ========
        lmp.tknzr.WsTknzr.tknz
        lmp.tknzr.BaseTknzr.norm

        Examples
        ========
        >>> from lmp.tknzr import WsTknzr
        >>> tknzr = WsTknzr(is_uncased=False, max_vocab=10, min_count=2)
        >>> tknzr.dtknz(['a', 'b', 'c'])
        'a b c'
        >>> tknzr.dtknz(['abc', 'def'])
        'abc def'
        """
        # First perform detokenization, then do normalization.
        return self.norm(' '.join(tks))
