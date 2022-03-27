# Backing up Signal messages from IOS (using Frida)

This guide is inteded for the technically skilled.
Jailbreak, MacOS, Homebrew required

Signal doesn't provide any backup mechanisms for iOS.

## Getting the database key

1. Install Frida on [Mac](https://frida.re/docs/installation/) and your jailbroken [iPhone](https://frida.re/docs/ios/)
2. run `./getkey.py`

Ouptut should look something like

```text
$ ./getkey.py
Waiting for Signal to start...
Database file: /private/var/mobile/Containers/Shared/AppGroup/A26B1269-0C99-4465-A4D0-A39562DD8B9A/grdb/signal.sqlite
Database key: 4aed84f9e96323522***CENSORED***5111180bbd2fc53
```

## Getting the database data (rsync)

1. Install openssh and rsync from Cydia on your phone.
2. `rsync -av root:alpine@IP_OF_PHONE:/private/var/mobile/Containers/Shared/AppGroup/[UUID_FROM_GETKEY.PY] .`

## Decrypting the database

1. Install SQLCipher `brew install sqlcipher`
2. Put `signal.sqlite` in same folder as `decrypt.sh` and run `decrypt.sh KEY_FROM_GETKEY`.
