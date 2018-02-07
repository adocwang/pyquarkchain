import unittest
from quarkchain.config import DEFAULT_ENV
from quarkchain.core import RootBlock, MinorBlock, Branch
from quarkchain.genesis import create_genesis_root_block, create_genesis_minor_block, create_genesis_blocks
import copy


class TestGenesisRootBlock(unittest.TestCase):

    def testBlockSerialization(self):
        block = create_genesis_root_block(DEFAULT_ENV)
        s = block.serialize(bytearray())
        nblock = RootBlock.deserialize(s)
        self.assertEqual(block, nblock)

    def testGensisBlocks(self):
        rBlock, mBlockList = create_genesis_blocks(DEFAULT_ENV)
        self.assertEqual(len(rBlock.minorBlockHeaderList), DEFAULT_ENV.config.SHARD_SIZE)


class TestGenesisMinorBlock(unittest.TestCase):

    def testBlockSerialization(self):
        env = copy.copy(DEFAULT_ENV)
        env.config.setShardSize(8)
        block = create_genesis_minor_block(env, 3)
        self.assertEqual(block.header.branch, Branch.create(8, 3))
        nblock = MinorBlock.deserialize(block.serialize())
        self.assertEqual(block, nblock)