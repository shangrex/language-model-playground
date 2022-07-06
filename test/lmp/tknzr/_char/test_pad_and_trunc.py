"""Test sequence padding and truncation.

Test target:
- :py:meth:`lmp.tknzr._char.CharTknzr.pad_to_max`.
- :py:meth:`lmp.tknzr._char.CharTknzr.trunc_to_max`.
"""

from lmp.tknzr._base import BOS_TKID, EOS_TKID, PAD_TKID, UNK_TKID
from lmp.tknzr._char import CharTknzr


def test_padding(is_uncased: bool, max_vocab: int, min_count: int) -> None:
  """Pad to specified length."""
  assert CharTknzr(
    is_uncased=is_uncased,
    max_vocab=max_vocab,
    min_count=min_count,
  ).pad_to_max(max_seq_len=2, tkids=[]) == [
    PAD_TKID,
    PAD_TKID,
  ]
  assert CharTknzr(
    is_uncased=is_uncased,
    max_vocab=max_vocab,
    min_count=min_count,
  ).pad_to_max(max_seq_len=5, tkids=[
    BOS_TKID,
    UNK_TKID,
    EOS_TKID,
  ]) == [
    BOS_TKID,
    UNK_TKID,
    EOS_TKID,
    PAD_TKID,
    PAD_TKID,
  ]


def test_truncation(is_uncased: bool, max_vocab: int, min_count: int) -> None:
  """Truncate to specified length."""
  assert CharTknzr(
    is_uncased=is_uncased,
    max_vocab=max_vocab,
    min_count=min_count,
  ).trunc_to_max(max_seq_len=5, tkids=[]) == []
  assert CharTknzr(
    is_uncased=is_uncased,
    max_vocab=max_vocab,
    min_count=min_count,
  ).trunc_to_max(max_seq_len=2, tkids=[
    BOS_TKID,
    UNK_TKID,
    EOS_TKID,
    PAD_TKID,
    PAD_TKID,
  ]) == [
    BOS_TKID,
    UNK_TKID,
  ]