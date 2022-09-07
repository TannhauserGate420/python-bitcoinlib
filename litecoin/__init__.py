# Copyright (C) 2012-2018 The python-litecoinlib developers
#
# This file is part of python-litecoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-litecoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.


import litecoin.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.12.0.dev0'

class MainParams(litecoin.core.CoreMainParams):
    MESSAGE_START = b'\xfb\xc0\xb6\xdb'
    DEFAULT_PORT = 9333
    RPC_PORT = 9332
    DNS_SEEDS = ('seed-a.litecoin.loshan.co.uk',
                 'dnsseed.thrasher.io',
                 'dnsseed.litecointools.com',
                 'dnsseed.litecoinpool.org',
                 'dnsseed.koin-project.com')
    BASE58_PREFIXES = {'PUBKEY_ADDR':48,
                       'SCRIPT_ADDR':50,
                       'SECRET_KEY' :176}
    BECH32_HRP = 'ltc'

class TestNetParams(litecoin.core.CoreTestNetParams):
    MESSAGE_START = b'\xfd\xd2\xc8\xf1'
    DEFAULT_PORT = 19333
    RPC_PORT = 19332
    DNS_SEEDS = ('testnet-seed.litecointools.com',
                 'seed-b.litecoin.loshan.co.uk',
                 'dnsseed-testnet.thrasher.io')
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':58,
                       'SECRET_KEY' :239}
    BECH32_HRP = 'tltc'

class SigNetParams(litecoin.core.CoreSigNetParams):
    MESSAGE_START = b'\x0a\x03\xcf\x40'
    DEFAULT_PORT = 39333
    RPC_PORT = 39332
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':58,
                       'SECRET_KEY' :239}

    BECH32_HRP = 'tltc'

class RegTestParams(litecoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xfa\xbf\xb5\xda'
    DEFAULT_PORT = 19444
    RPC_PORT = 19443
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':58,
                       'SECRET_KEY' :239}
    BECH32_HRP = 'ltcrt'

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
litecoin.core.params correctly too.
"""

params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    litecoin.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = litecoin.core.coreparams = MainParams()
    elif name == 'testnet':
        params = litecoin.core.coreparams = TestNetParams()
    elif name == 'regtest':
        params = litecoin.core.coreparams = RegTestParams()
    elif name == 'signet':
        params = litecoin.core.coreparams = SigNetParams()
    else:
        raise ValueError('Unknown chain %r' % name)
