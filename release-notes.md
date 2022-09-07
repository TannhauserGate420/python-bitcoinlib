# python-litecoinlib release notes

## v0.12.0-pending

* `CECKey` now rejects secrets that aren't exactly 32 bytes

## v0.11.2

* Fixed one remaining use of OpenSSL for RIPEMD-160

## v0.11.1

* Pure-python RIPEMD-160, for newer versions of OpenSSL without RIPEMD-160
  support.
* Signet support
