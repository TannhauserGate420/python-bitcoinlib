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

## Selecting the chain to use

Do the following:

    import litecoin
    litecoin.SelectParams(NAME)

Where NAME is one of 'testnet', 'mainnet', 'signet', or 'regtest'. The chain currently
selected is a global variable that changes behavior everywhere, just like in
the Satoshi codebase.
