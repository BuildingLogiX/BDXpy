# BDXpy: Building Data Exchange Python Package

![PyPI](https://img.shields.io/pypi/v/bdxpy?color=blue) ![GitHub license](https://img.shields.io/github/license/yourgithub/bdxpy) ![GitHub stars](https://img.shields.io/github/stars/yourgithub/bdxpy?style=social)

## Overview
**BDXpy** is a Python package for interacting with the **BuildingLogiX Data eXchange (BDX)** platform, providing access to building analytics, trending data, virtual hierarchies, and energy management insights. It simplifies **building data retrieval, trend analysis, and API integration** for smart buildings and energy efficiency applications.

## Features
✅ **Connect to BDX Platform** securely via API
✅ **Retrieve trending data** for energy and HVAC analysis
✅ **Navigate virtual hierarchies** of building components
✅ **Perform analytics** on real-time and historical data
✅ **Supports authentication** with credential management

## Installation
```sh
pip install bdxpy
```

## Quick Start
```python
from bdxpy import BDX, Authenticator

# Authenticate
auth = Authenticator(username="your_username", password="your_password")

# Connect to BDX Platform
bdx = BDX("https://your-bdx-server.com", auth)

# Retrieve trending data
trend = bdx.trending.trends(trend_id=1234)
data = trend.retrieve_data()
print(data.dataframe)
```

## Documentation
- [Reference]([https://github.com/yourgithub/bdxpy/wiki](https://buildinglogix.github.io/BDXpy/reference/))
- [Example Use Cases]([https://github.com/yourgithub/bdxpy/examples](https://buildinglogix.github.io/BDXpy/examples/))

## Contributing
We welcome contributions! Please check out the [Contributing Guide](CONTRIBUTING.md) for details.

## License
This package is distributed under a proprietary license. Contact BuildingLogiX for licensing information.

Learn more about BuildingLogiX Data Exchange (BDX) [here](https://buildinglogix.net/connected-buildings/buildinglogix-data-exchange-bdx/).
BDXpy on [pypi].(https://pypi.org/project/bdxpy/)


---
🚀 **BDXpy** helps streamline building analytics—get started today!
