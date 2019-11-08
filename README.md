## About

*Conan recipe for [QuickFIX (The QuickFIX Software License)](https://github.com/quickfix/quickfix)*

The recipe supports only Windows atm.

The recipe currently supports two options: build with emx and build with ssl, both defaulted to false. With ssl enabled openssl will be installed as a dependency, so there is no reliance on any existing openssl installation.

Example:
```
conan create <path-to-recipe> quickfix/1.15.1@<username>/<channel> -o emx=True -o ssl=True
```