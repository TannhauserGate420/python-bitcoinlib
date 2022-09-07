# python-litecoinlib

This Python3 library provides an easy interface to the litecoin data
structures and protocol. The approach is low-level and "ground up", with a
focus on providing tools to manipulate the internals of how litecoin works.

## Requirements

    sudo apt-get install libssl-dev

The RPC interface, `litecoin.rpc`, is designed to work with Litecoin Core v0.18.
Older versions may work but there do exist some incompatibilities.


## Structure

Everything consensus critical is found in the modules under litecoin.core. This
rule is followed pretty strictly, for instance chain parameters are split into
consensus critical and non-consensus-critical.

    litecoin.core            - Basic core definitions, datastructures, and
                              (context-independent) validation
    litecoin.core.key        - ECC pubkeys
    litecoin.core.script     - Scripts and opcodes
    litecoin.core.scripteval - Script evaluation/verification
    litecoin.core.serialize  - Serialization

In the future the litecoin.core may use the Satoshi sourcecode directly as a
library. Non-consensus critical modules include the following:

    litecoin          - Chain selection
    litecoin.base58   - Base58 encoding
    litecoin.bloom    - Bloom filters (incomplete)
    litecoin.net      - Network communication (in flux)
    litecoin.messages - Network messages (in flux)
    litecoin.rpc      - Litecoin Core RPC interface support
    litecoin.wallet   - Wallet-related code, currently Litecoin address and
                       private key support

Effort has been made to follow the Satoshi source relatively closely, for
instance Python code and classes that duplicate the functionality of
corresponding Satoshi C++ code uses the same naming conventions: CTransaction,
CBlockHeader, nValue etc. Otherwise Python naming conventions are followed.


## Mutable vs. Immutable objects

Like the Litecoin Core codebase CTransaction is immutable and
CMutableTransaction is mutable; unlike the Litecoin Core codebase this
distinction also applies to COutPoint, CTxIn, CTxOut, and CBlock.


## Endianness Gotchas

Rather confusingly Litecoin Core shows transaction and block hashes as
little-endian hex rather than the big-endian the rest of the world uses for
SHA256. python-litecoinlib provides the convenience functions x() and lx() in
litecoin.core to convert from big-endian and little-endian hex to raw bytes to
accommodate this. In addition see b2x() and b2lx() for conversion from bytes to
big/little-endian hex.


## Module import style

While not always good style, it's often convenient for quick scripts if
`import *` can be used. To support that all the modules have `__all__` defined
appropriately.


## Selecting the chain to use

Do the following:

    import litecoin
    litecoin.SelectParams(NAME)

Where NAME is one of 'testnet', 'mainnet', 'signet', or 'regtest'. The chain currently
selected is a global variable that changes behavior everywhere, just like in
the Satoshi codebase.
