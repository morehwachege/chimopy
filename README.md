
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
[![Organization](https://img.shields.io/badge/Org-morehwachege-blue.svg)](https://github.com/morehwachege)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/morehwachege/pull/)

[![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/morehwachege/chimopy).

# chimopy
This is a wrapper providing convenient access to the Chimoney API for applications written in Python.

It has been tested with Python 3.xx

### Setup and Installation

```Bash
pip install chimopy
```
You can also clone or download the library package and install it using setuptools:
``` bash
git clone https://github.com/morehwachege/chimopy.git
cd chimopy
python setup.py install
```

### Usage

``` python
from chimopy.<API> import <API Class>
```
View [docs](./docs.md)


***API***
The following APIs are supported:
- [x] Account
- [x] Info
- [x] Mobile-Money
- [ ] Payment, all except airtime
- [ ] Redeem
- [x] Sub Account
- [x] Wallet

***API Class***
The following are the corresponding API classes:
- [x] Account
- [x] Info
- [x] Transaction
- [x] Pay
- [x] Redeem
- [x] SubAccount
- [x] Wallet



[![morehwachege](https://img.shields.io/badge/Engineer-morehwachege-blue.svg?style=for-the-badge)](https://github.com/morehwachege)
[![morehwachege](https://img.shields.io/badge/Maintainer-morehwachege-green.svg?style=for-the-badge)](https://github.com/morehwachege)

# Dependencies
 None at the moment


# How to Install from Source

## Building from Source for Developers

```Bash
git clone https://github.com/morehwachege/chymopy.git
cd chimopy
python setupy bdist_wheel
python setupy install
```

# Contributing
[See the Contributing File](CONTRIBUTING.rst)


[See the Pull Request File](PULL_REQUEST_TEMPLATE.md)

# Support
<a href="https://www.buymeacoffee.com/muriithigakuru" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
# LICENCE
- MIT