#!/usr/bin/env sh
sqlcipher signal.sqlite "PRAGMA key = \"x'$1'\";PRAGMA cipher_plaintext_header_size = 32;ATTACH DATABASE 'signal.db' AS plaintext KEY '';SELECT sqlcipher_export('plaintext');"