## About

*Conan recipe for [QuickFIX (The QuickFIX Software License)](https://github.com/quickfix/quickfix)*

The recipe currently supports two options: build with emx and build with ssl, both defaulted to false. With ssl enabled openssl will be installed as a dependency, so there is no reliance on any existing openssl installation.

The recipe requires Conan 1.20.0 or higher.

The recipe supports only Windows atm.
Tested on [Windows, Visual Studio 15]

Example:
```
conan create <path-to-recipe> quickfix/1.15.1@<username>/<channel> -o emx=True -o ssl=True
```