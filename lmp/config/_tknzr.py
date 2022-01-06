
import argparse

from config._base import BaseCfg
from lmp.dset import DSET_OPTS
import lmp

class TknzrCfg(BaseCfg):
    def __init__(self) -> None:
        super().__init__()
        self.parser = argparse.ArgumentParser()

    def train_parser(self, parser: argparse.ArgumentParser) -> None:
        
        # Required arguments.
        group = self.parser.add_argument_group('common arguments')
        group.add_argument(
            '--dset_name',
            choices=lmp.dset.DSET_OPTS.keys(),
            help='Name of the dataset which is used to train tokenizer.',
            required=True,
            type=str,
        )
        group.add_argument(
            '--exp_name',
            help='Name of the tokenizer training experiment.',
            required=True,
            type=str,
        )
        group.add_argument(
            '--max_vocab',
            help=' '.join([
                'Maximum vocabulary size.',
                'If set to `-1`, then include as many token as possible.',
            ]),
            required=True,
            type=int,
        )
        group.add_argument(
            '--min_count',
            help=' '.join([
                'Minimum token frequency for token to be included in',
                'vocabulary.',
            ]),
            required=True,
            type=int,
        )
        group.add_argument(
            '--ver',
            help='Version of the dataset which is used to train tokenizer.',
            required=True,
            type=str,
        )

        # Optional arguments.
        group.add_argument(
            '--is_uncased',
            action='store_true',
            help='Convert all text and tokens into lowercase if set.',
        )

    def get_parser(self) ->argparse.ArgumentParser:
        return self.parser