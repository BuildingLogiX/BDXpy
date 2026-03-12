# BDXpy: Building Data Exchange Python Package - Complete Documentation

---

**Generated from GitHub Pages Documentation**

---

# Table of Contents

1. [Overview](#overview)
2. [Welcome to BDXpy Documentation](#welcome-to-bdxpy-documentation)
3. [Getting Started](#getting-started)
4. [Reference Guide](#reference-guide)
5. [Python Packages for BDXpy](#python-packages-for-bdxpy)
6. [Frequently Asked Questions](#frequently-asked-questions)
7. [Contributing to BDXpy](#contributing-to-bdxpy)
8. [Examples](#examples)
   - [Automated Reporting](#automated-reporting-examples)
   - [Dashboards](#dashboards)
   - [Data Service - Grafana](#data-service---grafana)
   - [Data Visualization](#data-visualization)
   - [LLM Integration](#llm-integration)

---

# Overview

![PyPI](https://img.shields.io/pypi/v/bdxpy?color=blue) ![GitHub license](https://img.shields.io/github/license/yourgithub/bdxpy) ![GitHub stars](https://img.shields.io/github/stars/yourgithub/bdxpy?style=social)

**BDXpy** is a Python package for interacting with the **BuildingLogiX Data eXchange (BDX)** platform, providing access to building analytics, trending data, virtual hierarchies, and energy management insights. It simplifies **building data retrieval, trend analysis, and API integration** for smart buildings and energy efficiency applications.

## Features

- **Connect to BDX Platform** securely via API
- **Retrieve trending data** for energy and HVAC analysis
- **Navigate virtual hierarchies** of building components
- **Perform analytics** on real-time and historical data
- **Supports authentication** with credential management

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

- Reference: https://buildinglogix.github.io/BDXpy/reference/
- Example Use Cases: https://buildinglogix.github.io/BDXpy/examples/

## License

This package is distributed under a proprietary license. Contact BuildingLogiX for licensing information.

Learn more about BuildingLogiX Data Exchange (BDX): https://buildinglogix.net/connected-buildings/buildinglogix-data-exchange-bdx/

BDXpy on PyPI: https://pypi.org/project/bdxpy/

---

# Welcome to BDXpy Documentation

`bdxpy` is a Python package designed to interface with BuildingLogiX Data Exchange (BDX), a building analytics platform developed by BuildingLogiX.

## Key Features

- **Access BDX trends and analytics:** Enables access to building information, trended data, equipment scores and energy analytics.
- **Handles BDX authentication:** Hides the complexity of BDX authentication and authorization mechanisms.
- **Provides data in native format:** Data series retrieved from BDX are available in Pandas DataFrame format, which enables intuitive processing in Python.

## Summary Overview and Concepts

This package allows users to interact with an API hosted on a BDX site. BDXpy is a Python library designed to facilitate interaction with BuildingLogiX's API for managing building data, trends, components, and hierarchies. This guide provides an overview of the library's features, including how to authenticate, retrieve data, and handle exceptions. It includes modules for authentication, session management, trend data retrieval, and component lookup.

Our goals with BDXpy are:

- Allow a *new canvas of opportunities for partners* - almost endless with python and package features.
- *Quicker development ideas with examples from partners* and internal BLX teams
- More "power" or experimentation on the end user.
- Take advantage of Open-Source capabilities and help *define what the future of FDD and Optimization could become at a lower cost*.
- Promote more advanced *Machine Learning and Energy savings outcomes* and grow the industry.
- Create a *library/standard of advanced visualization and analysis available to the greater community*.

## References

- https://buildinglogix.github.io/BDXpy/
- https://pypi.org/project/bdxpy/
- https://buildinglogix.net/

## Example Use Cases

- Automated custom reports
- Machine Learning Applications
- AI integrations (OpenAI, Gemini, etc.)
- Advanced/Custom Dashboards and Visualizations

---

# Getting Started

## Applications and Use Cases

BDXpy is a powerful companion tool for use with BDX installations. This tool designed for advanced users who need to interface with the BuildingLogiX Data Exchange (BDX) platform for retrieving, processing, and analyzing building performance data in a complex/customized way. While we prefer to develop all great ideas into the main BDX development roadmap, BDXpy gives use the ability NOW to bring their own ideas to life or create value in ways that might not make sense as a one off project in BDX.

Some key applications include:

- **As a Data Playground** - Automate the retrieval of historical and real-time energy consumption data for custom reporting and analysis.
- **As a Data Service** - run BDXpy inside automated reports or on servers as an API service. For example in Grafana dashboards or weekly energy/FDD summaries of your buildings major KPIs.
- **As an Application** - Build interactive public dashboards for stakeholder using Flask, Dash, or other web frameworks.
- **As a Solution** - Extract data from BDX and integrate it with other platforms, including cloud databases, CMMS, and BI tools. Maybe create automated analysis and summaries for issues with AI assistants??

**Note: BDXpy development is custom to each end user and each BDX site. The responsibility of best practices around coding, data retrievals, architecture, and deployment practices are yours. Unless contracted BuildingLogiX is not responsible nor warrants user created scripts, programs, etc.**

BuildingLogiX is providing a pathway for advanced capabilities and a gateway to large volumes of organized data. If you wish to have a consultant or use BuildingLogiX in your development with BDXpy we are happy to engage members of our development and engineering teams. Reach us at technical.support@buildinglogix.net

## Why Python?

BDXpy was built using **Python** because of its flexibility, powerful capabilities, and vast ecosystem of open-source libraries. Python is widely used in data science, automation, and web applications, making it an ideal choice for interacting with the **BuildingLogiX Data Exchange (BDX)** platform.

### Key Reasons For Choosing Python:

- **Ease of Use & Readability** - Python's simple syntax makes it accessible for both beginners and advanced users, allowing for rapid development and maintainability.
- **Large Open-Source Community** - Python has one of the largest and most active developer communities, ensuring extensive support, tutorials, and libraries for virtually any task.
- **Rich Data Science Ecosystem** - Libraries like **pandas**, **NumPy**, and **Matplotlib** enable powerful data manipulation, statistical analysis, and visualization.
- **Scalability & Performance** - Python can be used for quick prototyping as well as large-scale applications, supporting both small scripts and enterprise-level solutions.
- **Extensive Integration Options** - Python easily integrates with databases, web services, cloud platforms (AWS, Azure, GCP), and APIs, making it the perfect language for automation and analytics.
- **Cross-Platform Compatibility** - Python runs on **Windows, macOS, and Linux**, ensuring that BDXpy can be deployed across different environments with minimal setup.
- **Automation & Scripting** - Python excels at automating repetitive tasks, scheduling reports, and managing data pipelines with minimal effort.

By leveraging Python's strengths, **BDXpy** provides a robust, scalable, and easy-to-use interface for working with BDX, empowering users to extract insights, automate processes, and build custom applications.

## Architecture Options

There are a couple different ways to run/deploy BDXpy depending on your needs and use cases. Technically multiple sources of BDXpy could be running simultaneously performing various tasks.

**Disclaimer:** BDXpy is intended for power users and rates of data collection should be reasonable and if too many requests of large quantities of data are simultaneously taking place it could strain the BDX application and database servers as well as the local machine hosting BDXpy as large data frames can become memory intensive. BDXpy limitations are dependent both on the location of its operation but also the BDX instance it communicates with. It's the responsibility of the user to make smart decisions with this knowledge.

BDXpy (as the below image suggests) can be used on an existing BDX server, on a dedicated server, or run from a laptop/computer. In all cases the network path between the BDX instance and BDXpy needs to be active for scripts and processes using BDXpy to work.

### Deployment Cases

1. **On a laptop/personal computer:** for engineers wanting to experiment, run reports from their machine, non-24/7 script deployments.
   - Easiest way to get started or pilot something before deploying elsewhere so long as user has access to BDX from laptop

2. **On an existing BDX server:** likely for an on-premises installation where data is served back to BDX via Windows IIS and are publishing BDXpy internally with identical firewall rules to BDX.
   - Install here if you want BDXpy files to feedback to the kiosk or custom apps/widgets. Maybe require IT approval or cooperation

3. **On a dedicated BDXpy server:** user who might have a cloud BDX but locally want to serve up private network, but internal (non-authenticated) dashboard/visuals/kiosks on a local network. Or users who have more powerful tasks or server resources or teams that shouldn't/can't access the BDX server RDP directly or who want to have scripts automatically run on a timed/automated schedule
   - Dedicated servers could also be cloud VMs if they have access to BDX where automated reports or new apps are created. Doesn't require extra IT permissions or resources on the BDX server depending on the scope.

4. **Cloud Functions:** BDXpy scripts can be run in serverless environments such as AWS Lambda or Azure Functions provided, they don't entail long running or complex processes or other serverless constraints and have access to communicate with the BDX instance/server. See cloud provider for details

### Checking the BDX license for BDXpy

BDXpy requires a license feature on the source BDX. These can be viewed in a BDX instance under **Manage Licenses** to ensure the feature is enabled.

### Installation

Installing the BDX Python package is relatively simple. The first thing required is to download the Python language onto your device.

1. BDXpy requires Python 3.12 or newer versions (newer versions are recommended). This can be done through the Python downloads website.
2. Ensure BDX instance is licensed for API access.
3. After installing the necessary packages and obtaining the correct licensing, install BDXpy just like any other Python package:

```python
pip install bdxpy
```

Information on pip: https://pypi.org/

### Requirements packaged that come with BDXpy

BDXpy requires Python 3.12+ and the following dependencies which will be installed with BDXpy:

- requests
- pandas
- nacl
- urllib3
- dacite

Note: you do not need to install these separately as they come with BDXpy, this is purely for reference.

### BDXpy Imports

To make use of bdxpy functions python will need "imports" from the package. These imports reside before the code/functions are called in the python script and are all typically handled in the beginning lines of the code like below:

```python
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.core import BDX
from bdx.types import TimeFrame
from bdx.components import Components

## examples of other python package imports (but not limited to) that can be used with data from BDXpy
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import pandas as pd
import re
import matplotlib.pyplot as plt
```

## BDXpy License

This package is distributed under a proprietary license. Contact BuildingLogiX for licensing information.

Learn more about BuildingLogiX Data Exchange (BDX): https://buildinglogix.net/connected-buildings/buildinglogix-data-exchange-bdx/

BDXpy on pypi: https://pypi.org/project/bdxpy/

---

# Reference Guide

## Authentication and Session Setup

### Using a .env File for Credentials

To enhance security, you can store the username and password in a .env file rather than hardcoding them into your python code.

Note: Files containing the credentials should have appropriate security practices in place such as user/server permissions so they cannot be accessed/stolen/or compromised.

Below are the examples to set up and use a .env file for authentication. More on this process and security can also be found online.

1. Create a .env File

In your project directory, create a file named .env with the following content:
```
BDX_USERNAME=your_username
BDX_PASSWORD=your_password
```

2. Install the python-dotenv Library

Install the library to load environment variables from the .env file:
```python
pip install python-dotenv
```

3. Load Environment Variables in Your Script

Use the following code to load the .env file and authenticate with BDX:

```python
from dotenv import load_dotenv
import os
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.core import BDX

# Specify the path to the environment variable file
load_dotenv(dotenv_path=r"C:\Users\your-path\.env")

username = os.getenv("BDX_USERNAME")
password = os.getenv("BDX_PASSWORD")

if not username or not password:
    raise EnvironmentError("Environment variables BDX_USERNAME and BDX_PASSWORD must be set in the .env file")

authenticator = UsernameAndPasswordAuthenticator(username, password)
with BDX("http://yourBDXURL.com", authenticator) as bdx_instance:

    print("Connection successful!")
```

### Credentials in script

For testing purposes the BDX_USERNAME and BDX_PASSWORD can also be copied into the authentication in python.

```python
with BDX("http://yourBDXURL.com", UsernameAndPasswordAuthenticator(
  "BDX_USERNAME", "BDX_PASSWORD")) as bdx_instance:
```

### Important Notes on Authentication

- Currently, the authentication method requires the user to be a BDX local user or an LDAP user. Users authenticated via Single Sign-On (SSO) or Multi-Factor Authentication (MFA) are not supported or applicable by BDXpy.
- Ensure you have a local BDX username and password for successful authentication that is dedicated to BDXpy. Do not use regular usernames or admin credentials for reoccurring scripts.
- The credentials used for BDXpy must have BDX security permissions to access the data you are requesting as well as the BDX permissions listed below:
  - **BDXUser**
  - **TrendViewDataAccess**

- And any device/building/system read permissions necessary found under **Manage Path Access** if Object Level Security is enabled in BDX.
- BDXpy is generally intended for use by advanced power users and admin users even with basic permissions in the BDX app its important to secure your credentials and appoint a BDXpy lead to ensure all uses of the product are being authorized and managed properly.
- From an authentication perspective BDXpy should be limited in the users BDXpy calls from for audit log and tracking practices. (aka a limited number of users of a single BDX instance and not for mass use by basic security users).

## Component Retrieval Structure

BDXpy uses `componentPathId` to call devices and properties. This applies to buildings and all child devices in BDX. `componentPathId` is the unique identifier path from the source data agent or parent BDX properties in the hierarchy of devices.

> **Note:** `componentPathId != componentInstanceID`

### Component Structure Analogy

- **Component path**: "File path" of a component.
- **Component path ID**: "File inode number."
  - This is what BDXpy will use in component retrieval.
- **Component instance ID**: File version.

### Defining Devices for Data Retrieval

Before retrieving data, a user needs to define a set of devices to pull properties from, which will require outlining the `componentPathId`s of these devices.

#### Methods to Lookup `componentPathId`

1. Use methods in BDXpy to lookup or call `componentPathId`.
2. Manually find the `componentPathId` under **Manage Device Information** in BDX.
3. Lookup information in the **Custom Query Tool** in BDX.

---

### Overview of Methods to Get `componentPathId`

In its simplest form, a `componentPathId` can be found if you know the `componentInstanceId`.

#### Example: Retrieve a Component by Instance ID

```python
from dotenv import load_dotenv
import os
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.core import BDX

# Specify the path to the environment variable file
load_dotenv(dotenv_path=r"C:\Users\your-path\.env")

username = os.getenv("BDX_USERNAME")
password = os.getenv("BDX_PASSWORD")

if not username or not password:
    raise EnvironmentError("Environment variables BDX_USERNAME and BDX_PASSWORD must be set in the .env file")

authenticator = UsernameAndPasswordAuthenticator(username, password)
with BDX("http://yourBDXURL.com", authenticator) as bdx_instance:

    print("Authenticated successfully!")

    # Retrieve component by ID
    component_instance_id = 8590005002

    component = bdx_instance.components.by_id(component_instance_id)

    # Extract component details
    component_name = component.path.displayName
    full_path = component.path.displayFullPath
    component_path_id = component.path.componentPathId

    print(f"Component Name: {component_name}")
    print(f"Component Inst ID: {component_instance_id}")
    print(f"Component Full Path: {full_path}")
    print(f"Component Path ID: {component_path_id}")
```

Output:
```
Authenticated successfully!
Component Name: BuildingLogiX Campus
Component Inst ID: 4294967534
Component Full Path: /Buildings/BuildingLogiX Campus
Component Path ID: 4294967534
```

If you know a building ID you can then print out all its components and their IDs:

```python
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.core import BDX
from bdx.types import TimeFrame, AggregationLevel
import pandas as pd
from dotenv import load_dotenv
import os

def get_component_table(bdx_instance, building_id):
    try:
        # Retrieve components by building ID
        components = bdx_instance.components.by_building(building_id)

        # Create a list to hold the component details
        component_data = []

        # Loop through the components and collect the details
        for component in components:
            # Extract component details
            component_name = component.path.displayName
            full_path = component.path.displayFullPath
            component_path_id = component.path.componentPathId
            component_instance_id = component.componentInstanceId  # Add component instance ID
            entity_type = component.entityTypeName  # Component type
            template_type = component.templateType  # Template type

            # Append to the component_data list
            component_data.append({
                'Component Name': component_name,
                'Full Path': full_path,
                'Component Path ID': component_path_id,
                'Component Instance ID': component_instance_id,  # New column
                'Entity Type': entity_type,  # Add component type
                'Template Type': template_type  # Add template type
            })

        # Convert the list into a Pandas DataFrame
        df = pd.DataFrame(component_data)

        # Write DataFrame to CSV
        file_path = r'C:yourPath\BDXpy\component_data.csv'
        df.to_csv(file_path, index=False)

        return df  # Return the DataFrame

    except Exception as e:
        print(f"Error retrieving components: {str(e)}")
        return None

# Use this function in the run method like this:
def run():
    with BDX("https://yourBDXURL.com", UsernameAndPasswordAuthenticator("BDX_USERNAME", "BDX_PASSWORD")) as bdx_instance:

        # Retrieve components by building ID
        building_id = 4294967302  # Replace with your actual Building ID

        # Get the table of components
        component_table = get_component_table(bdx_instance, building_id)

        # Display the table
        if component_table is not None:
            print(component_table)

if __name__ == "__main__":
    run()
```

#### Example: Building ID Retrieval

To retrieve building data, use the buildings module. The list() method retrieves summaries of all accessible buildings.

```python
from dotenv import load_dotenv
import os
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.core import BDX
import pandas as pd

# Specify the path to the environment variable file
load_dotenv(dotenv_path=r"C:\Users\your-path\.env")

username = os.getenv("BDX_USERNAME")
password = os.getenv("BDX_PASSWORD")

if not username or not password:
    raise EnvironmentError("Environment variables BDX_USERNAME and BDX_PASSWORD must be set in the .env file")

authenticator = UsernameAndPasswordAuthenticator(username, password)
with BDX("http://yourBDXURL.com", authenticator) as bdx_instance:

    print("Authenticated successfully!")

###### Retrieve building summaries for all buildings in your BDX site ######
building_summaries = bdx_instance.buildings.list()

# Convert building summaries to a DataFrame
data = [
    {
        "Building Name": building.name,
        "Building ID": building.componentInstanceId,
        "Square Footage": building.sqft,
        "Address": f"{building.address.addr1}, {building.address.city}, {building.address.state}"

    }
    for building in building_summaries
]
building_df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(building_df)
```

### Manage Device Information in BDX

Within BDX, users can navigate to Manage Device Information in the upper left navigation. There user can navigate the BDX buildings, hierarchy, and device to look information. This includes the ability to get `componentInstanceId` which can then be translated with BDXpy to `componentPathId` per the code below.

```python
# Retrieve component by ID
compInstID = 4294967535
component = bdx.components.by_id(compInstID)
# Extract component details
component_name = component.path.displayName
full_path = component.path.displayFullPath
component_path_id = component.path.componentPathId

print(f"Component Name: {component_name}")
print(f"Component Inst ID: {compInstID}")
print(f"Component Full Path: {full_path}")
print(f"Component Path ID: {component_path_id}")
```

### Custom Query Tool lookup in BDX

Navigate to the Custom Query Tool in your BDX instance. In the Advanced Query Mode the various query text below can be pasted and run to retrieve `componentPathId`.

#### Building lookup

This is an example advanced query that can be run from BDX to return values.

```sql
select b.name, b.componentInstanceId, b.path.componentPathId
from Building b
```

#### "Raw" assigned point ID lookups

The query below looks up any assigned folder or raw points listed under the building (see **Manage Buildings > Assigned Point Folders List** in BDX). Users can specify/filter the building name in the BDX query below.

```sql
select pf.folderPathAlias,  pf.folderPath.fullPath, pf.folderPath.componentPathId, pf.folderPath.currentComponent.componentInstanceId
from Building b
join b.assignedPointFolders pf
where b.name = 'BuildingLogiX Campus'
```

### Built-in Component Filtering

`ComponentFilter` is a filtering mechanism used in **BDXpy** to refine searches when retrieving building components. It allows filtering by specific attributes like template type, path keyword, and subscription status.

```python
from bdx.core import BDX
from bdx.components import ComponentFilter
```

#### Attributes

- `template_type` *(str, optional)* - The template type of the component, such as "VAV" for Variable Air Volume boxes.
- `path_keyword` *(str, optional)* - A keyword to search for within the component's path. If filtering by template type alone, this must be set to an empty string (""), otherwise, a 500 error will occur.
- `only_subscribed` *(bool, default False)* - If True, filters only components that are subscribed.

#### Usage Examples

Retrieving VAV Components by Path Keyword

To retrieve all VAV components assigned to a building, filtering by a specific keyword in the path:

```python
filter = ComponentFilter()
filter.template_type = "VAV"
filter.path_keyword = "AHU_1_VAVs"

print(b.components.by_building(4294967304, filter))
```

This retrieves all VAV components associated with the building ID 4294967304 that contain "AHU_1_VAVs" anywhere in their path.

##### Filtering by Template Type Alone

If filtering by template type only, the path_keyword must be set to an empty string:

```python
filter = ComponentFilter()
filter.template_type = "VAV"
filter.path_keyword = ""  # Must be explicitly set to avoid error

print(b.components.by_building(4294967304, filter))
```

##### Retrieving Only Subscribed Components

To fetch only subscribed components, set only_subscribed to True:

```python
filter = ComponentFilter()
filter.template_type = "VAV"
filter.path_keyword = "AHU_1_VAVs"
filter.only_subscribed = True

print(b.components.by_building(4294967304, filter))
```

This will return only components that meet the filtering criteria and are subscribed.

##### Searching All Buildings for a Filter

To can search the entire BDX site for components with a certain name by looping through all buildings and applying filters to the components assigned to each building.

```python
import pandas as pd
from bdx.core import BDX
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.components import ComponentFilter

# Authenticate and initialize BDX
auth = UsernameAndPasswordAuthenticator("your_username", "your_password")
bdx_instance = BDX("https://your-bdx-instance.com", auth)

# Get a list of all buildings
building_summaries = bdx_instance.buildings.list()

# Create a filter to search for components
filter = ComponentFilter()
filter.template_type = "VAV"
filter.path_keyword = "AHU_1_VAVs"  # Adjust search term

# Store results in a list
all_components = []

for building in building_summaries:
    building_id = building.componentInstanceId
    print(f"Searching in building: {building.name} (ID: {building_id})")

    # Retrieve components matching the filter in this building
    components = bdx_instance.components.by_building(building_id, filter)

    # Add retrieved components to the list
    for comp in components:
        all_components.append({
            "Building Name": building.name,
            "Building ID": building_id,
            "Component ID": comp.componentInstanceId,
            "Component Path ID": comp.path.componentPathId if comp.path else None,
            "Template Type": comp.templateType,
            "Path": comp.path.fullPath if comp.path else None,
            "Display Name": comp.path.displayName if comp.path else None,
            "Data Collection ID": comp.path.clientDataCollectionId if comp.path else None
        })

# Convert to DataFrame
df = pd.DataFrame(all_components)

# Display the results
print(df)

# Save to CSV for analysis (optional)
df.to_csv("filtered_components_across_buildings.csv", index=False)
```

## Data Retrieval

Now that you have components, you can select properties of components and retrieve data. The Trending module and function in BDXpy allows you to retrieve time series data for various properties of components. Once the timeseries data is in a data frame in python various filters, transformations, analysis, etc. can be applied.

There are several methods in which to call data. Data can be called right from a Trendview ID or by `componentPathId`. After retrieving data the names/column labels a user might desire modifications as BDXpy returns the `componentPathId` in the column header. This can be revised to a custom-user defined label or if calling view Trendview ID inherit the trend labels.

### Methods for Data Retrieval

#### Method 1 - retrieve data using component path/property combinations

```python
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.core import BDX
from bdx.types import TimeFrame

def main():
with BDX("http://yourBDXURL.com", UsernameAndPasswordAuthenticator("BDX_USERNAME", "BDX_PASSWORD")) as bdx_instance:

# 21474864282 is an example ID of an AHU. Below calls that AHU and some properties
        r = bdx_instance.trending.retrieve_data([
            {
                "propertyName": "coolOutput",
                "componentPathId": 21474864282,
            },
            {
                "propertyName": "ductStaticPressure",
                "componentPathId": 21474864282,
            },
            {
                "propertyName": "ductStaticPressureSetpoint",
                "componentPathId": 21474864282,
            },
            {
                "propertyName": "heatOutput",
                "componentPathId": 21474864282,
            },
            {
                "propertyName": "mixedAirTemp",
                "componentPathId": 21474864282,
            },
            {
                "propertyName": "outdoorAirDamperPos",
                "componentPathId": 21474864282,
            },
            {
                "propertyName": "outdoorAirTemp",
                "componentPathId": 21474864282,
            }])

 # Output the first few rows and variables of data
        print(r.dataframe)

# Information about the columns can also be printed to help see things like 'deviceType' or 'displayName'

        print(r.column_information)
main()
```

Outputs:
```
time  21474864282_coolOutput  ...  21474864282_outdoorAirDamperPos  21474864282_outdoorAirTemp
0   2024-12-27 00:00:00-05:00                     0.0  ...                              0.0                   42.300949
1   2024-12-27 00:15:00-05:00                     0.0  ...                              0.0                   42.148983
2   2024-12-27 00:30:00-05:00                     0.0  ...                              0.0                   42.351444
3   2024-12-27 00:45:00-05:00                     0.0  ...                              0.0                   42.401859
4   2024-12-27 01:00:00-05:00                     0.0  ...                              0.0                   42.602707

[716 rows x 8 columns]
```

#### Method 2 - retrieve a pre-defined trend, then get its data

```python
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.core import BDX
from bdx.types import TimeFrame

def main():
with BDX("http://yourBDXURL.com", UsernameAndPasswordAuthenticator("BDX_USERNAME", "BDX_PASSWORD")) as bdx_instance:

# 635 is the trend ID which can be found in trendview

        t = bdx_instance.trending.trends(635)
        d = t.retrieve_data(TimeFrame.last_7_days())

        print(d.dataframe)


main()
```

Outputs:
```
time  73014470773_realPowerDemand  73014470744_realPowerDemand  fbaaca38439e857f939d395d7948c5510c8d05f7_totalDemand
0   2024-12-30 11:30:00-05:00                  1180.125122                   944.100098                                        2124.225220
1   2024-12-30 11:45:00-05:00                  1314.464478                  3286.161133                                        4600.625610
2   2024-12-30 12:00:00-05:00                  1321.848755                  3304.621826                                        4626.470581
3   2024-12-30 12:15:00-05:00                  1330.281860                  3325.704590                                        4655.986450
4   2024-12-30 12:30:00-05:00                  1434.879639                  3874.174805                                        5309.054443
```

###### Finding Trendview ID

A list of all saved trends can be called in BDXpy. A hyperlink of a saved trend can be referenced.

Pasted hyperlink with highlighted trend ID **635**:
`http://yourBDXURL.com/trendview/index.html?open=635&timeframe=last7Days&aggregationLevel=Point`

### Names and Labels

Now that you have data lets rename the labels by replacing the `componentPathId` in the column headers with the TrendView label or the equipment display name.

#### Renaming Labels in BDXpy

##### Example 1: displayName and Property as column labels

```python
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.core import BDX
from bdx.types import TimeFrame

def main():
with BDX("http://yourBDXURL.com", UsernameAndPasswordAuthenticator("BDX_USERNAME", "BDX_PASSWORD")) as bdx_instance:

# 21474864282 is an example ID of an AHU. Below calls that AHU and some properties
        r = bdx_instance.trending.retrieve_data([
            {
                "propertyName": "coolOutput",
                "componentPathId": 21474864282,
            },
            {
                "propertyName": "ductStaticPressure",
                "componentPathId": 21474864282,
            },
            {
                "propertyName": "ductStaticPressureSetpoint",
                "componentPathId": 21474864282,
            },
            {
                "propertyName": "heatOutput",
                "componentPathId": 21474864282,
            },
            {
                "propertyName": "mixedAirTemp",
                "componentPathId": 21474864282,
            },
            {
                "propertyName": "outdoorAirDamperPos",
                "componentPathId": 21474864282,
            },
            {
                "propertyName": "outdoorAirTemp",
                "componentPathId": 21474864282,
            }])

# Extract the dataframe from the response
    df = r.dataframe  # Now 'df' holds the DataFrame with your data

    # 'r.column_information' contains the metadata for the columns
    column_information = r.column_information

    new_column_names = {}  # Create an empty dictionary to store the new column names.

    # Loop through each column and its associated metadata in the column_information dictionary.
    for col, info in column_information.items():
        # Try to get the 'label' from the metadata. If no label is provided, it will return None.
        label = info.get('label', None)

        if label:
            # If a 'label' exists, use it as the new column name.
            new_column_names[col] = label
        else:
            # If no 'label' is available, we fall back to constructing a column name
            # based on the device's display name and the property name.
            device_name = info['deviceInfo']['displayName']
            property_name = info['propertyName']
            new_column_names[col] = f"{device_name}_{property_name}"

    # Apply the new column names to the DataFrame.
    df.rename(columns=new_column_names, inplace=True)
    print(df.head())

main()
```

Notice how in the outputs the `componentPathId` is replaced with the `displayName` of the device and columns are labeled `AHU1_ductStaticPressure` instead of `21474864282 ductStaticPressure`

Output:
```
time  AHU1_coolOutput  AHU1_ductStaticPressure  ...  AHU1_mixedAirTemp  AHU1_outdoorAirDamperPos  AHU1_outdoorAirTemp
0 2024-12-27 00:00:00-05:00              0.0                 -0.02514  ...          66.657455                       0.0            42.300949
1 2024-12-27 00:15:00-05:00              0.0                 -0.02514  ...          66.688950                       0.0            42.148983
2 2024-12-27 00:30:00-05:00              0.0                 -0.02514  ...          66.688950                       0.0            42.351444
3 2024-12-27 00:45:00-05:00              0.0                 -0.02514  ...          66.657455                       0.0            42.401859
4 2024-12-27 01:00:00-05:00              0.0                 -0.02514  ...          66.625923                       0.0            42.602707
```

##### Example 2: Modifying Labels from a Trendview ID function

```python
import pandas as pd
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.core import BDX
from bdx.types import TimeFrame

# Function to call the BDX API and retrieve data
def api_call(trend_id, timeframe):
    try:
        with BDX("http://yourBDXURL.com", UsernameAndPasswordAuthenticator("BDX_USERNAME", "BDX_PASSWORD")) as bdx_instance:
            trend = bdx_instance.trending.trends(trend_id)
            data = trend.retrieve_data(timeframe)
            df = data.dataframe

            # Use true column names from displayName if available
            true_column_names = [value['deviceInfo']['displayName'] if 'deviceInfo' in value and 'displayName' in value['deviceInfo'] else key
                                 for key, value in data.column_information.items()]
            df.columns = ['time'] + true_column_names[:len(df.columns) - 1]
            return df

    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return None

def main():
    try:
        trend_ids = 597
        timeframe = TimeFrame.last_n_days(4)
        df = api_call(trend_ids, timeframe)

        if df is None:
            print("No data returned from API.")
            return
    except Exception as e:
        print(f"An error occurred: {e}")

main ()
```

Output:
```
time  N_Street_Elec  N_Hill_Elec  BuildingLogiX Campus
0   2024-12-30 11:30:00-05:00    1180.125122   944.100098           2124.225220
1   2024-12-30 11:45:00-05:00    1314.464478  3286.161133           4600.625610
2   2024-12-30 12:00:00-05:00    1321.848755  3304.621826           4626.470581
3   2024-12-30 12:15:00-05:00    1330.281860  3325.704590           4655.986450
```

#### Replace Labels Manually in Python

If you manually want to create a list to rename a data frame columns by matching on IDs, something like these functions can be added to your code:

```python
def get_custom_display_names(data_response, custom_display_names):
    """
    Renames DataFrame columns based on custom display names and 'propertyName' from component metadata.

    Parameters:
    data_response: The response object containing both the DataFrame and column metadata.
    custom_display_names (dict): A dictionary mapping componentPathId to custom display names.

    Returns:
    DataFrame: DataFrame with columns renamed as 'CustomDisplayName_propertyName'.
    """
    # Retrieve the DataFrame and column information
    df = data_response.dataframe
    column_information = data_response.column_information

    new_column_names = {}

    # Loop through each column and its metadata
    for col, info in column_information.items():
        component_path_id = info.get('componentPathId')

        # Use custom display name if available; otherwise, fall back to displayName
        display_name = custom_display_names.get(component_path_id, info.get('deviceInfo', {}).get('displayName', 'Unknown'))

        # Ensure 'propertyName' exists
        property_name = info.get('propertyName', 'UnknownProperty')

        # Construct new column name as 'CustomDisplayName_propertyName'
        new_column_names[col] = f"{display_name}_{property_name}"

    # Rename DataFrame columns
    df.rename(columns=new_column_names, inplace=True)

    return df

df_compressors = get_custom_display_names(data_response, custom_display_names)
```

### Timeframes and Aggregations

BDXpy allows users to retrieve trend data for specific timeframes and aggregate the data based on desired intervals. This provides flexibility for analyzing trends over varying periods and resolutions.

#### Timeframes

Timeframes define the duration of the data to retrieve. BDXpy provides several predefined options, such as:

- `TimeFrame.last_7_days()` for data from the past seven days.
- `TimeFrame.last_30_days()` for data from the past 30 days.
- `TimeFrame.last_n_days()` for specifying a discrete number of days.

Users can also define custom timeframes by specifying a start and end datetime that is covered in the examples below.

#### Aggregations

Aggregations control how data is grouped or summarized over time. The default mode is point-level samples and doesn't need called in the retrieval function. Aggregation options include for example:

- `AggregationLevel.POINT`
- `AggregationLevel.HOURLY`
- `AggregationLevel.DAILY`
- `AggregationLevel.WEEKLY`
- `AggregationLevel.MONTHLY`
- `AggregationLevel.YEARLY`

Combining timeframes and aggregation levels allows users to tailor their trend data queries to their specific needs.

##### Example: Retrieve Trend Data with Timeframes and Aggregations

```python
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.core import BDX
from bdx.types import TimeFrame, AggregationLevel

# Replace with your credentials and BDX URL
BDX_URL = "http://your-bdx-url.com"
USERNAME = "your_username"
PASSWORD = "your_password"

authenticator = UsernameAndPasswordAuthenticator(USERNAME, PASSWORD)

with BDX(BDX_URL, authenticator) as bdx_instance:
    # Retrieve a specific trend
    trend = bdx_instance.trending.trends(635)

    # Retrieve data for the last 7 days with daily aggregation
    trend_data1 = trend.retrieve_data(
        timeframe=TimeFrame.last_7_days(),
        aggregation_level=AggregationLevel.DAILY
    )
    # Retrieve data for the last 60 days with hourly aggregation
    trend_data2 = trend.retrieve_data(
        timeframe=TimeFrame.last_n_days(60),
        aggregation_level=AggregationLevel.HOURLY
    )
```

## Python Exception Errors

The package includes custom exceptions for handling errors that might occur when running a python script with BDXpy:

- `AuthenticationError` - When calling BDXSession() or BDX() and login credentials fail.
- `HttpRequestError` - When retrieving trends, buildings, or components from the BDX API.
- `DataNotFoundError` - When requesting a component, trend, or time series that doesn't exist.
- `SecurityError` - When trying to access a restricted resource (e.g., a building component you don't have access to).

## BDXpy Modules (User-Facing Only)

1. `auth.py` - Manages authentication, including username/password login.
2. `buildings.py` - Allows users to retrieve building data, including addresses, zones, and assigned components.
3. `components.py` - Enables component lookups, including retrieving information about HVAC systems, meters, sensors, and other building components.
4. `core.py` - Provides the main interface for interacting with BDX, wrapping session management and data retrieval.
5. `trending.py` - Handles trend data retrieval, allowing users to query, filter, and analyze time-series data from BDX.
6. `types.py` - Defines helper classes, enumerations, and error handling for API interactions.

---

# Python Packages for BDXpy

BDXpy users can benefit from a variety of Python packages to enhance data analysis, visualization, automation, and machine learning. Python has numerous packages than what is listed below for almost anything. Youtube, Google, and other search options can help provide a lot of free examples to beginners. For those getting started or unfamiliar below are some packages that you might find useful working with BDXpy:

## Data Analysis & Processing

### Pandas (https://pandas.pydata.org/)
- Essential for data manipulation and analysis, Pandas makes it easy to handle time-series data retrieved from BDX.
- Supports powerful data aggregation, filtering, and statistical operations.

### NumPy (https://numpy.org/)
- Provides fast array operations, mathematical functions, and numerical processing capabilities.
- Helpful for working with large datasets from BDX efficiently.

### ReportLab (https://www.reportlab.com/docs/reportlab-userguide.pdf)
- A powerful library for generating PDFs from data.
- Useful for exporting BDX reports, trend summaries, and energy analysis into professional-grade PDFs.

---

## Data Visualization

### Plotly (https://plotly.com/python/)
- Ideal for creating interactive charts, including line charts, scatter plots, heatmaps, and dashboards.
- Works well with BDX trend data and supports rendering inside web applications.

### Dash (https://dash.plotly.com/)
- A great framework for building interactive web applications without needing JavaScript.
- Useful for creating dynamic visualizations with BDX data.

### Matplotlib (https://matplotlib.org/)
- A powerful library for static, animated, and interactive visualizations.
- Useful for quick visual analysis of BDX data without interactive elements.

### Seaborn (https://seaborn.pydata.org/)
- Enhances Matplotlib with advanced statistical visualizations and better default aesthetics.
- Great for analyzing trends in energy usage and equipment performance.

### Plotly Mapbox (https://plotly.com/python/mapbox-layers/)
- Enables map-based visualization of BDX data, such as energy consumption across multiple buildings.
- Supports overlaying real-time data on campus maps.

---

## Machine Learning & Forecasting

### Scikit-learn (https://scikit-learn.org/stable/)
- A machine learning library with tools for regression, classification, clustering, and anomaly detection.
- Can be used to analyze energy trends, detect anomalies, and forecast consumption.

### XGBoost (https://xgboost.readthedocs.io/en/stable/)
- A high-performance machine learning library optimized for structured data.
- Useful for predictive modeling of energy consumption and HVAC system behaviors.

### Prophet (https://facebook.github.io/prophet/)
- A time-series forecasting tool developed by Facebook.
- Useful for predicting energy usage patterns and trends in BDX.

### Statsmodels (https://www.statsmodels.org/stable/index.html)
- Provides statistical models, hypothesis testing, and forecasting.
- Useful for analyzing historical building energy consumption and HVAC efficiency.

### PyCaret (https://pycaret.org/)
- A low-code machine learning library that automates model training, selection, and tuning.
- Great for quickly developing predictive models for BDX data.

---

## Automation & Optimization

### NetworkX (https://networkx.org/)
- Helps model and analyze complex relationships within BDX hierarchical components.
- Useful for understanding interdependencies between buildings, sensors, and control points.

### PuLP (https://coin-or.github.io/pulp/)
- A linear programming and optimization library.
- Can optimize HVAC schedules or chiller plant operations.

### Schedule (https://schedule.readthedocs.io/en/stable/)
- A lightweight job scheduling library for Python.
- Useful for automating BDX data retrieval and reporting.

### Flask (https://flask.palletsprojects.com/en/2.2.x/)
- A lightweight web framework for building BDX-powered APIs and dashboards.
- Can serve energy reports, analytics, and visualizations.

### FastAPI (https://fastapi.tiangolo.com/)
- A high-performance web framework for building APIs with Python.
- Faster and more scalable than Flask, making it great for handling large BDX requests.

**Got more package recommendations?** Let us know on the discussion board: https://github.com/BuildingLogiX/BDXpy/discussions/categories/user-creations

---

# Frequently Asked Questions

## How do I install BDXpy?

Use pip:
```bash
pip install bdxpy
```
See the installation section: https://buildinglogix.github.io/BDXpy/getting-started/#installation

## How do use BDXpy?

See our workflow diagram for getting started: https://buildinglogix.github.io/BDXpy/getting-started/#process-overview-from-bdx-to-bdxpy-and-python-outputs

## Do I have to pay for BDXpy?

BDXpy requires an active BDX license including the license feature for RemoteAPI.
Installation of the Python package BDXpy is free and publicly available as well as all documentation and some basic examples to get users started.

## What if I don't know Python?

Python is one of the most widely used programming languages and is open-source. It has many resources, classes, examples online beginners can pull from.
Likewise most AI chatbots like ChatGPT, Gemini, etc. all generally quite good a Python development and we highly encourage beginners to utilize all these available tools.

BuildingLogiX is also working on forming a dedicated BDXpy custom GPT, coming soon.....

## What are IDEs, which one should I use for BDXpy?

An IDE (Integrated Development Environment) is a software application that provides coding tools, such as syntax highlighting, debugging, and auto-completion, to make development easier.

For working with BDXpy, most of our team uses VS Code most of the time or Jupyter Notebook in VS Code. There are others we also recommend depending on your experience and preference:

- **VS Code** - Lightweight, customizable, and great for Python development.
- **PyCharm** - More feature-rich, with advanced debugging and code analysis.
- **Jupyter Notebook** - Best for interactive data analysis and quick visualizations.
- **Spyder** - Designed for data science, similar to MATLAB.

Recommendation: If you need a full-fledged Python IDE, VS Code or PyCharm is great. If you are doing data exploration, try Jupyter Notebook.

## What is the difference between Python and Jupyter Notebook files?

- **Python scripts (.py):**
  - Standard Python files used for writing and executing programs.
  - Run using a terminal, command line, or an IDE like VS Code/PyCharm.
  - Best for larger projects and production-ready code.

- **Jupyter Notebooks (.ipynb):**
  - An interactive environment that allows you to mix code, markdown, and visualizations.
  - Best for data analysis, quick prototyping, and educational purposes.
  - Supports inline plots (like matplotlib and seaborn).

Recommendation: Use .py for software development and .ipynb for analysis, documentation, or interactive work.

## Can BuildingLogiX help me develop in Python?

Yes, BuildingLogiX has in-house developers and engineers who are happy to assist. IF you want to collaborate on BDXpy development it is considered custom development and involves working directly with our team! We will also likely have a series of small training seminars annual on BDXpy.
Reach out to us if you are interested.

## I'm getting an HTTP error when trying to connect to BDX - what does it mean?

BDXpy communicates with your **BDX platform server** over HTTPS. When HTTP errors occur, they usually indicate a **server connection**, **authentication**, or **licensing** issue.

Below are common causes and solutions.

---

### 401 Unauthorized or 403 Forbidden

**Possible causes:**
- Invalid username or password.
- Missing or expired BDX license.
- Your BDX account does not have the RemoteAPI feature enabled.
- The BDX server is enforcing HTTPS and the client attempted an HTTP connection.

**Fixes:**
- Confirm your credentials in your `.env` or authentication code:
  ```python
  from bdx.auth import UsernameAndPasswordAuthenticator
  auth = UsernameAndPasswordAuthenticator("your_username", "your_password")
  ```
- Make sure your BDX license includes the **RemoteAPI** feature.
- Check with your administrator that your user role permits API access.
- Use a proper HTTPS URL, e.g. `https://your-bdx-server.com`.

---

### 404 Not Found

**Possible causes:**
- Incorrect BDX site URL or server path.
- The BDX site has not deployed the `/bdx/rest/...` API endpoints.
- You are connecting to the wrong tenant or environment (e.g., dev vs prod).

**Fixes:**
- Double-check the `host_url` you are using:
  ```python
  bdx = BDX("https://your-bdx-server.com", auth)
  ```
- Confirm that the BDX server is online and accessible.
- If your instance is behind a VPN or proxy, ensure your client can reach it.

---

### 500 Internal Server Error / 502 / 503 / 504

**Possible causes:**
- The BDX server encountered an internal failure.
- There are network proxy issues between your client and server.
- SSL/TLS certificate on the server is invalid or expired.
- The BDX service may be restarting or under maintenance.

**Fixes:**
- Verify that your server certificate is valid (especially for on-prem installations).
- Restart the BDX site or check its service health via `/bdx/unrestricted/rest/management/monitoring/summary`.
- Try again later - some errors resolve after the server finishes restarting.
- For corporate or on-prem servers, contact your system admin to check service logs.

---

### Licensing & BDXpy Access

**Key distinction:**
- The **BDX platform license** controls access to the API.
- The **BDXpy Python package** is open-source and free to install via pip:
  ```bash
  pip install bdxpy
  ```
  However, BDXpy requires your BDX server to have **an active BDX license with RemoteAPI enabled**.

**Fixes:**
- Contact BuildingLogiX Support to verify that your BDX site has valid licensing for API use.
- If you can log into the BDX web interface but cannot authenticate via Python, your RemoteAPI feature is likely disabled.

---

### Authentication Failures (MFA, Expired Session, etc.)

**Possible causes:**
- MFA is required but not configured in your script.
- The user's session has expired.
- The password has changed since the last stored `.env` update.

**Fixes:**
- Use `UsernameAndPasswordAuthenticator` to refresh credentials each session.
- Avoid storing plaintext passwords - use an `.env` file or encrypted secret.
- If MFA is enabled, check for MFA code support (BDXpy currently supports static username/password only).

---

### Connection or Certificate Issues

**Possible causes:**
- Invalid SSL certificate on the BDX server.
- Self-signed certificate without being trusted by the client.
- Firewall or proxy interference.

**Quick test only: temporarily ignore SSL verification (insecure):**
- If using a **self-signed certificate**, either:
  - Install it as a trusted certificate on your machine, or
  - Disable SSL verification *temporarily* for testing:
    ```python
    import urllib3
    from bdx.core import BDX
    from bdx.auth import UsernameAndPasswordAuthenticator

    def make_session_insecure(sess):
        # Silence the "InsecureRequestWarning"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # Tell Requests not to verify TLS certs on this session
        sess.verify = False

    auth = UsernameAndPasswordAuthenticator("username", "password")

    # Works the same if you have a convenience helper like get_bdx()
    with BDX("https://your-bdx-server", auth) as bdx:
        # Force SSL ignore at the adapter/session level (affects all calls on THIS session)
        make_session_insecure(bdx.session)

        # Optional: ping triggers auth and populates version internally
        try:
            print("BDX version:", bdx.platform_version)
        except Exception as ex:
            print("[warn] version check failed:", type(ex).__name__, ex)

        # ... now make your data calls, e.g. fetch_daily_cycle_counts(...)
    ```
    *Not recommended for production use!*
- If behind a corporate proxy, configure `HTTP_PROXY` and `HTTPS_PROXY` environment variables.

---

### Tip: Test Basic Connectivity

To verify your setup without running a full data call:
```python
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.core import BDX

auth = UsernameAndPasswordAuthenticator("username", "password")
bdx = BDX("https://your-bdx-server.com", auth)
print(bdx.platform_version)
```

If this fails, it helps identify whether the problem is **authentication**, **network**, or **licensing**.

---

## Who can I contact for support?

Email us at technical.support@buildinglogix.net.

---

# Contributing to BDXpy

We welcome and encourage participation in the BDXpy community! While direct code contributions are not required, here's how you can get involved:

## Share Your Creations

Showcase your charts, visualizations, and analyses in the GitHub Discussions section under User Creations: https://github.com/BuildingLogiX/BDXpy/discussions/categories/user-creations

Upload images, share insights, and discuss results with the community.

## Ask Questions & Troubleshoot

If you have questions about BDXpy, visit the Q&A section in Discussions to get help: https://github.com/BuildingLogiX/BDXpy/discussions/categories/q-a

Check the Issues tab to see if your question has already been answered or report a bug.

## Reporting Issues

Found a bug? Open a new issue in the Issues section with as much detail as possible: https://github.com/BuildingLogiX/BDXpy/issues

If applicable, include screenshots, error messages, or a minimal dataset to reproduce the issue.

## Suggest Features & Improvements

Have an idea to improve BDXpy? Share it in Discussions: https://github.com/BuildingLogiX/BDXpy/discussions/categories/q-a

Thank you for being a part of the BDXpy community! Your engagement helps improve the project for everyone.

---

# Examples

## Example Highlights Gallery

### Data Visualization

- **Airflow Sankey** - Building airflow visualization by AHU and VAV
- **Building CFM Network** - Network visualization of airflow relationships
- **Campus Energy Map** - Map-based energy consumption visualization
- **AHU Economizer Analysis** - Detailed economizer operation chart
- **Operating Room KPIs** - Hospital network Sankey diagram
- **Static Pressure Distribution** - AHU static pressure curve analysis

### Dashboards

- **AHU Cooling Performance App** - https://ahu-cool-performance-buildinglogix.plotly.app/
- **Campus Utilities App** - https://energy-dashboard-xpwn.onrender.com/
- **RTU Dashboard** - https://rtu-dash-bdxpy.onrender.com/

### Machine Learning

More examples coming soon!

### Public Kiosk App

More examples coming soon!

---

# Automated Reporting Examples

This guide walks you through setting up BDXpy as a FastAPI data service on a Grafana server and configuring it as a JSON API data source.

## Example PDF generation of monthly energy report

Below is example code where you can insert BDXpy code to generate a PDF from a combination of images and tables. In the second example these principles can be applied to create a PDF that gets emailed.

```python
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import imgkit
import time
import plotly.io as pio
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import table
from selenium import webdriver
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from datetime import datetime
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from PIL import Image as PILImage

print("Current Working Directory:", os.getcwd())

# Function to save the DataFrame to a PNG
def save_dataframe_to_png(df, file_name):
    # Set up the plot
    fig, ax = plt.subplots(figsize=(12, 6))  # Adjust size as necessary
    ax.axis('off')  # No axes
    ax.axis('tight')

    # Create the table from the DataFrame
    table_data = table(ax, df, loc='center', cellLoc='center', colWidths=[0.1] * len(df.columns))

    # Save the figure as a PNG
    plt.savefig(file_name, bbox_inches='tight', dpi=300)


# Assuming 'fig' is your Plotly figure object
def save_plotly_as_png(fig, output_filename):
    # Save the figure as a PNG file
    pio.write_image(fig, output_filename)

def save_html_to_file(fig, file_name):
    # Save the Plotly figure as an HTML file
    fig.write_html(file_name)

config = imgkit.config(wkhtmltoimage=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe')

def html_to_png(html_file, output_image):
    time.sleep(2)  # Adjust the delay as necessary
    imgkit.from_file(html_file, output_image, config=config)

#### BDXpy function would go here along with component selections #####

df=data

# ... (full code continues with data processing and PDF generation)

# Function to add images with preserved aspect ratio
def add_image_with_aspect_ratio(image_path, max_width=6*inch, max_height=4*inch):
    img = PILImage.open(image_path)
    width, height = img.size
    aspect_ratio = width / height

    if width > height:
        new_width = min(max_width, width * (max_height / height))
        new_height = new_width / aspect_ratio
    else:
        new_height = min(max_height, height * (max_width / width))
        new_width = new_height * aspect_ratio

    return Image(image_path, width=new_width, height=new_height)

def create_pdf(output_filename, map_chart, cost_summary_img, energy_summary_img, co2_summary_img, yoy_chart, pct_change_chart):
    pdf = SimpleDocTemplate(output_filename, pagesize=letter)
    elements = []

    # Title and summary text
    styles = getSampleStyleSheet()
    title = Paragraph("Energy Consumption Summary", styles['Title'])
    summary_text = Paragraph(
        "This report provides an overview of the energy consumption for the month.", styles['Normal']
    )

    elements.append(title)
    elements.append(summary_text)

    # Add map chart image with aspect ratio preserved
    map_image = add_image_with_aspect_ratio(map_chart)
    elements.append(map_image)

    # Add year-over-year chart with aspect ratio preserved
    yoy_image = add_image_with_aspect_ratio(yoy_chart)
    elements.append(yoy_image)

    # Add percentage change chart with aspect ratio preserved
    pct_change_image = add_image_with_aspect_ratio(pct_change_chart)
    elements.append(pct_change_image)

    # Build PDF
    pdf.build(elements)

# Call the create_pdf function with PNG paths
create_pdf("energy_summary.pdf", "mapenergychart.png", "cost_summary.png", "energy_summary.png", "co2_summary.png", "yearoveryearchart.png", "pctchangechart.png")
```

## Email PDF Report

A SMTP email service can be used to email this PDF. The python script can then be referenced in a BAT file and scheduled to run from the Windows Task Scheduler on a user specified interval.

```python
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.core import BDX
from bdx.types import TimeFrame
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from reportlab.lib.colors import HexColor
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import smtplib
from email.message import EmailMessage

# Load environment variables from .env file
load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
ALERT_EMAIL = os.getenv("ALERT_EMAIL")

BDX_USERNAME = os.getenv("BDX_USERNAME")
BDX_PASSWORD = os.getenv("BDX_PASSWORD")

def get_previous_month_dates():
    today = datetime.now()
    first_day_of_current_month = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    last_day_of_previous_month = first_day_of_current_month - timedelta(seconds=1)
    first_day_of_previous_month = last_day_of_previous_month.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    return first_day_of_previous_month, last_day_of_previous_month

def create_pdf_report(data_summary, data_trend):
    try:
        pdf_path = "output/automated_report.pdf"
        pdf = SimpleDocTemplate(pdf_path, pagesize=A4)
        elements = []

        styles = getSampleStyleSheet()
        title = Paragraph("Automated Report Example", styles['Title'])
        elements.append(title)

        start_date, end_date = get_previous_month_dates()
        date_text = Paragraph(f"Reporting Period: {start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}", styles['BodyText'])
        elements.append(date_text)
        elements.append(Spacer(1, 0.2 * A4[1]))

        # Example chart
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(data_trend['Date'], data_trend['Value'], marker='o')
        plt.title("Example Data Trend")
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.grid(True)

        chart_image = BytesIO()
        plt.savefig(chart_image, format="png")
        plt.close(fig)
        chart_image.seek(0)
        chart = Image(chart_image, width=5 * A4[0] / 8, height=3 * A4[1] / 8)
        elements.append(chart)

        # Example data table
        table_data = [data_summary.columns.to_list()] + data_summary.values.tolist()
        table = Table(table_data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(table)
        pdf.build(elements)

        print(f"PDF report saved to {pdf_path}")
        return pdf_path
    except Exception as e:
        print(f"Error generating PDF: {e}")
        send_alert_email(f"Failed to generate PDF report: {e}")
        return None

def send_email_with_pdf(pdf_path):
    subject = "Automated Report Example"
    body = "Please find the attached example automated report."

    msg = EmailMessage()
    msg["From"] = SMTP_USERNAME
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.set_content(body)

    with open(pdf_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=os.path.basename(pdf_path))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.send_message(msg)
    print(f"Email with PDF {pdf_path} sent.")

def send_alert_email(error_message):
    subject = "PDF Generation Alert"
    msg = EmailMessage()
    msg["From"] = SMTP_USERNAME
    msg["To"] = ALERT_EMAIL
    msg["Subject"] = subject
    msg.set_content(f"An error occurred: {error_message}")

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.send_message(msg)
    print("Alert email sent due to PDF generation failure.")

def main():
    with BDX("https://yourBDXURL.com", UsernameAndPasswordAuthenticator(BDX_USERNAME, BDX_PASSWORD)) as b:
        start_date, end_date = get_previous_month_dates()
        print(f"Start Date: {start_date}, End Date: {end_date}")

        # Example dummy data retrieval
        dummy_data = b.trending.retrieveData([
            {"propertyName": "value", "componentPathId": 1234567890},
            {"propertyName": "value", "componentPathId": 1234567891}
        ], timeframe=TimeFrame(start=start_date, end=end_date))

        df_dummy = pd.DataFrame({
            "Date": pd.date_range(start=start_date, periods=10, freq='D'),
            "Value": [x for x in range(10)]
        })

        df_summary = pd.DataFrame({
            "Metric": ["Total Energy", "Peak Demand", "Average Usage"],
            "Value": [10000, 500, 350]
        })

        pdf_path = create_pdf_report(df_summary, df_dummy)
        if pdf_path:
            send_email_with_pdf(pdf_path)
        else:
            print("PDF generation failed. Email not sent.")

main()
```

---

# Dashboards

## Example: AHU Cooling Performance App

Dash app that loads AHU data from BDX and visualizes Air Handling Unit cooling performance.
Built with Dash, Plotly, and Dash AG Grid; includes fault filtering and fullscreen views.

**Live Demo:** https://ahu-cool-performance-buildinglogix.plotly.app/

### Highlights

- **Bubble Chart of Cooling Valve % vs. Coil dT (F)**: size proportional to fan VFD power, color = SAT (F), optional red halo for AHUs with active faults.
- **Faults Dropdown**: Filter everything (chart + tables) by one or more active faults, or Any active fault.
- **Building Filter**: Multi-select buildings to focus the portfolio view.
- **Centered Link Ribbon**: When a point is clicked, SAT/CCT trend links appear above the chart.
- **Data Grids (AG Grid)**: Sort/filter, quick scan of main metrics and an "Active Faults" table.
- **One-click Downloads**: Export the currently displayed main or faults data to CSV.
- **Fullscreen Overlay**: Expand any chart/table; close with x or Esc.
- **Consistent UI**: Sticky header, compact padding, modern muted icon colors.

---

## Example: Campus Utilities App

Example layout of a BDXpy app for reading/viewing campus utilities.

**Note:** this may take a minute to load as the example is being hosted on a free tier service

**Live Demo:** https://energy-dashboard-xpwn.onrender.com/

---

## Example: RTU Monitoring

Dash app containing standard colors and timeframes for various means of display on RTU data from BDX.
This example was deployed on https://render.com/

Beyond the code below there was additional server, css, and environmental files required to deploy.

**Live Demo:** https://rtu-dash-bdxpy.onrender.com/

This example demonstrates a dashboard for monitoring RTU (Rooftop Unit) performance using **BDXpy**. It features:

- **Real-time Data Visualization**: Tracks key RTU metrics over time.
- **Interactive Graphs & Charts**: Provides insights into energy consumption and efficiency.
- **Responsive Web Design**: Accessible on both desktop and mobile.

Code example here: https://github.com/dan-blx/rtu_dash_bdxpy

---

# Data Service - Grafana

## Setting Up BDXpy as a Data Service for Grafana

This guide walks you through setting up BDXpy as a FastAPI data service on a Grafana server and configuring it as a JSON API data source.

### 1. Install Dependencies

Ensure you have Python 3.12+ installed. Install the necessary dependencies:
```python
pip install fastapi uvicorn pandas requests python-dotenv
```

### 2. Set Up Environment Variables

Create a .env file to store your BDX credentials securely:
```python
BDX_URL="https://your-bdx-instance.com"
BDX_USER="your-username"
BDX_PASS="your-password"
```

**Note:** your server the data service is being run on will need access to reach the bdx URL. Because BDXpy handles authentication on additional authentication is needed in grafana.

### 3. Implement the FastAPI Service

Create a file bdx_service.py and define the API:

```python
from fastapi import FastAPI, Query, HTTPException, BackgroundTasks, Request
from fastapi.responses import JSONResponse
import pandas as pd
import uvicorn
import os
import logging
import json
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from slowapi import Limiter
from slowapi.util import get_remote_address
from typing import List, Optional
from memory_profiler import profile

# Import BDXpy modules
from bdx.core import BDX
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.trending import PropertyDescriptor
from bdx.types import TimeFrame, AggregationLevel

# Configure Logging
logger = logging.getLogger(__name__)
log_handler = logging.handlers.RotatingFileHandler("api.log", maxBytes=100*1024*1024, backupCount=5)
logger.setLevel(logging.DEBUG)
log_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(log_handler)

# Load environment variables
load_dotenv()
BDX_URL = os.getenv("BDX_URL")
BDX_USER = os.getenv("BDX_USER")
BDX_PASS = os.getenv("BDX_PASS")

# Initialize Rate Limiting
limiter = Limiter(key_func=get_remote_address)

# FastAPI app
app = FastAPI()

# Initialize BDX connection
authenticator = UsernameAndPasswordAuthenticator(BDX_USER, BDX_PASS)
bdx_instance = BDX(BDX_URL, authenticator)

@app.get("/query")
@limiter.limit("20/minute")
async def query_grafana(
    request: Request,
    background_tasks: BackgroundTasks,
    component_path_ids: str = Query(..., title="Comma-separated list of Component Path IDs"),
    properties: str = Query("value", title="Comma-separated list of properties"),
    start_time: Optional[str] = Query(None, title="Start Time (ISO 8601, default: 24h ago)"),
    end_time: Optional[str] = Query(None, title="End Time (ISO 8601, default: now)")
):
    # ... query processing code ...
    pass

@app.get("/")
async def root():
    return {"message": "BDXpy API for Grafana"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

### 4. Run the API Service

Start the service:
```python
python bdx_service.py
```

Your FastAPI service is now running on **port 8000**.

**Note:** if this is an important process you will want to create additional monitoring and error checking and maybe expand service restart scenarios to ensure high uptime

### 5. Configure Grafana

- **Install JSON API**

- **Add a New Data Source in Grafana**:
  - Navigate to **Configuration -> Data Sources -> Add Data Source**.
  - Select **"JSON API"**.
  - Set:
    - **URL**: `http://localhost:8000`
    - **Method**: `GET`
  - Click **Save & Test**.

- **Create a Panel**:
  - Go to **Dashboards -> Create -> New Panel**.
  - Choose the **JSON API** data source.
  - Set the **Query Path** to `/query`.
  - Add **Query Parameters**:
    - `component_path_ids=21474864282`
    - `properties=supplyAirTemp,ductStaticPressure`
    - `start_time=${__from:date}`
    - `end_time=${__to:date}`

- **Format Response in Grafana**:
  - Use **JSONPath Queries** to extract data

### 6. Verify Data in Grafana

- Ensure your **panel correctly visualizes each series separately**.
- If a **boolean point** (e.g., `supplyFanStatus`) is coming back **null**, check:
  - The **property name** in BDX.
  - The **data type** (it may need conversion to `1/0` instead of `true/false`).

### 7. (Optional) Enable Secondary Y-Axis in Grafana

To plot **multiple metrics** with different scales:
- Go to **Panel Settings -> Axes**.
- Under **Y-Axis**, set:
  - **Y-Axis 1** for `supplyAirTemp`
  - **Y-Axis 2** for `ductStaticPressure`

### 8. (Optional) Add Background Shading for Boolean Points

To visualize a **Boolean** (`True/False`) metric:
- Use **Field Overrides**:
  - Set a **Threshold** (e.g., `1 = ON` / `0 = OFF`).
  - Change **background color** dynamically based on status.

---

# Data Visualization

## Building CFM Network

This example demonstrates the relationships, location, and changes related to airflow across different air systems within a building.

```python
import networkx as nx
from pyvis.network import Network
import pandas as pd
from bdx.core import BDX
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.types import TimeFrame, AggregationLevel
from bdx.components import ComponentFilter
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# BDX Credentials and Connection
BDX_URL = "http://yourURL.com"  # Replace with your actual BDX URL
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"
BUILDING_NAME = "YOUR_BUILDINGNAME"

# Connect to BDX
auth = UsernameAndPasswordAuthenticator(USERNAME, PASSWORD)
with BDX(BDX_URL, auth) as bdx:
    buildings = bdx.buildings.list()
    matching_buildings = [b for b in buildings if b.name.lower() == BUILDING_NAME.lower()]
    if not matching_buildings:
        print(f"No building found with the name: {BUILDING_NAME}")
        exit()

    BUILDING_ID = matching_buildings[0].componentInstanceId
    BUILDING_NODE = f"Building: {BUILDING_NAME}"

    # ... (full code for network visualization)

# Generate and save the network visualization
net.show("VAV_network.html")

print("\n Network visualization saved as 'VAV_network.html'. Open it in a browser to view.")
```

---

## AHU Economizer Analysis

This example demonstrates a detailed review of AHU economizing conditions.

```python
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Dynamically identify the relevant column names
occupancy_col = [col for col in df.columns if 'occupancystatus' in col.lower()][0]
oat_col = [col for col in df.columns if 'outdoorairtemp' in col.lower()][0]
mat_col = [col for col in df.columns if 'mixedairtemp' in col.lower()][0]
rat_col = [col for col in df.columns if 'returnairtemp' in col.lower()][0]

# Filter data for rows where occupancyStatus is 'occupied' and drop rows with NaN in key columns
occupied_data = df[df[occupancy_col].str.lower() == 'occupied']
occupied_data = occupied_data.dropna(subset=[oat_col, mat_col, rat_col])

# ... (full code for economizer analysis visualization)

# Show the plot
fig.show()
```

---

## Building Airflow by AHU and VAV (Sankey)

This example demonstrates the relationships, location, and changes related to airflow across different air systems within a building using a Sankey diagram.

---

## Total Energy Map by Building - Building Type

Get energy data and sum/chart over map area using Plotly Mapbox.

```python
### Use BDXpy here to call your buildings and load a gps file to match on building name #####
##  store variables in df in below code

# Create a map with bubble size variation and opacity
fig = px.scatter_mapbox(
    df_summed,
    lat='Latitude',
    lon='Longitude',
    hover_name='Building Name',
    size='Total Energy',  # Bubble size based on Total Energy
    color='Building Type',  # Color based on Building Type
    size_max=40,  # Max bubble size
    zoom=14,
    mapbox_style="carto-positron",
    text='Building Name',
    opacity = 0.6,
    title= "Energy Consumption by Building Type"
)

# Set map layout
fig.update_layout(
    mapbox_center={"lat": 51.7540, "lon": -1.2577},
    margin={"r": 10, "t": 100, "l": 10, "b": 10},
    height=800  # Adjust height for better layout
)

fig.update_traces(marker=dict(opacity=0.6))

fig.show()

# Example usage
fig.write_html("mapenergychart.html")
```

---

## Hospital Network OR KPIs

Sankey diagram for hospital operating room KPIs including air changes, runtime, cost, and temperature.

---

## AHU Static Pressure Distribution Curve

This example demonstrates how to chart AHU static pressure distribution for a time period by AHU.
Load your data from BDXpy, select a timeframe and revise any variables or chart formatting.

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Parameters for dummy data
np.random.seed(0)  # For reproducibility
num_ahus = 5
ahus = [f'AHU_{i+1}' for i in range(num_ahus)]
date_range = pd.date_range(start='2023-10-01', end='2023-10-31', freq='H')
num_samples = len(date_range)

# Generate random static pressure data with different transformations for each AHU
# ... (full code)

# Plot the KDE curve using seaborn's displot
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.displot(df, x='static_pressure', hue='AHU', kind="kde", fill=True, height=6, aspect=1.5)

# Set title and adjust layout to avoid cutoff
plt.suptitle("Curve of Static Pressure Ranges by AHU", y=1.05, fontsize=16)
plt.xlabel("Static Pressure (in w.c.)")
plt.ylabel("Density")
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adding padding for the title

# Save the plot as a PNG file
plt.savefig("AHU_static_pressure_kde_curve.png", bbox_inches="tight")
plt.show()
```

---

## AHU Static Pressure Duration Comparison

This example demonstrates how to chart AHU static pressure duration for a time period by AHU.
Load your data from BDXpy, select a timeframe and revise any variables or chart formatting.

```python
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Function to generate the duration curve with binned percent exceedance for AHU static pressure
def generate_binned_duration_curve(df, ahus, bin_width=5):
    duration_data = []
    for ahu in ahus:
        ahu_data = df[df['AHU'] == ahu].copy()
        ahu_data = ahu_data.sort_values(by='static_pressure', ascending=False).reset_index(drop=True)

        # Calculate percent exceedance and bin it
        ahu_data['percent_exceedance'] = np.floor(np.arange(1, len(ahu_data) + 1) / len(ahu_data) * 100 / bin_width) * bin_width
        # Group by binned percent_exceedance and calculate mean only on numeric columns
        binned_ahu_data = ahu_data.groupby('percent_exceedance', as_index=False)['static_pressure'].mean()
        binned_ahu_data['AHU'] = ahu  # Retain AHU identifier
        duration_data.append(binned_ahu_data)
    return pd.concat(duration_data, ignore_index=True)

# Generate binned duration curve data
duration_df = generate_binned_duration_curve(df, ahus, bin_width=5)

# Plot the duration curve as overlapping bar charts with wider bins
def plot_binned_duration_curve(duration_df, ahus):
    fig = go.Figure()
    for ahu in ahus:
        ahu_duration = duration_df[duration_df['AHU'] == ahu]
        fig.add_trace(go.Bar(
            x=ahu_duration['percent_exceedance'],
            y=ahu_duration['static_pressure'],
            name=ahu,
            opacity=0.6
        ))
    fig.update_layout(
        title="Binned Duration Curve for AHU Static Pressure (Overlapping Bar Charts)",
        xaxis_title="Percent Exceedance (%)",
        yaxis_title="Static Pressure (inches of water)",
        barmode='overlay',
        legend_title="AHU",
        template="plotly_white"
    )
    fig.show()

# Run the plot function to save the file as HTML
plot_binned_duration_curve(duration_df, ahus)
```

---

# LLM Integration

Large Language Models (LLMs) can be used to summarize, interpret, and contextualize findings from BDX data. By processing HVAC and energy system data, LLMs can generate insights in a readable, action-oriented format, assisting building operators, facility managers, and analysts in making data-driven decisions.

**Example Use Case:** VAV Air System Analysis

There is an example using the OpenAI Python package to send BDX data for a VAV air system, prompting the model to generate a summary of airflow anomalies. The LLM can help highlight abnormal trends, suggest possible causes, and provide recommended actions based on the data.

## Using BDXpy with OpenAI API

This guide explains how to use `bdxpy` with an OpenAI API key to analyze HVAC airflow data. The script retrieves airflow data from a BDX instance, detects anomalies, and generates a summary using OpenAI's API.

Sending data to OpenAI is one piece that will be the focus of this example. But how you define data inputs, prompt engineering text, and select models is a crucial piece that each engineer or developer needs to review and account for.

## OpenAI API Rate Limits

OpenAI imposes rate limits on API calls, which vary based on the model and subscription plan. As of recent updates, rate limits typically include:
- **GPT-4o & GPT-4:** Limited to a set number of requests per minute (RPM) and tokens per minute (TPM).
- **GPT-3.5:** More relaxed limits but still subject to RPM and TPM constraints.
- Free-tier users have significantly lower limits compared to API subscription plans.

Refer to OpenAI's official rate limits documentation for the most up-to-date details: https://platform.openai.com/docs/guides/rate-limits

## Why Sending Large Volumes of raw BDX Data is Not Recommended

The example script retrieves extensive airflow data from a BDX instance, but sending large datasets to OpenAI is **inefficient** due to:
1. **API Rate Limits:** Exceeding limits can result in throttling or failed requests.
2. **High Token Costs:** Large payloads consume more tokens, increasing costs.
3. **Performance Delays:** Processing large text blocks slows down response times and API calls.

### Recommended Approach:
- **Use OpenAI as a Framework:** Instead of processing large volumes, focus on targeted statistics and smaller timeframes.
- **Pre-process Data Locally:** Summarize key metrics (e.g., top anomalies, AHU-wide trends) before sending to OpenAI.
- **Batch Requests:** Instead of one large request, break it into smaller, meaningful prompts.

## Importance of Prompt Engineering

Prompt engineering plays a **critical** role in obtaining useful outputs from OpenAI models.

### Key Strategies:
- **Be Specific:** Provide context and constraints to guide responses.
- **Use Formatting Cues:** Structure prompts using bullet points, tables, or numbered lists for better parsing.
- **Avoid Ambiguity:** Clearly define what constitutes an anomaly or significant event in BDX data.
- **Iterate and Refine:** Test different prompts to improve accuracy and relevance.

## Model Selection Impact

Different OpenAI models produce varying results:

- **GPT-4o** (Best for complex, structured data insights)
- **GPT-3.5** (Faster and cheaper but less accurate for nuanced analysis)
- **Fine-tuned Models** (Can be trained on historical BDX data for better contextual responses)

### Choosing the Right Model

| **Use Case**          | **Recommended Model** |
|----------------------|------------------|
| Detailed anomaly detection | GPT-4o |
| General HVAC summaries | GPT-3.5 |
| Custom BDX optimizations | Fine-tuned model |

## Final Recommendations

- Use OpenAI **strategically** to analyze key **data points**, not raw time-series data.
- Fine-tune prompts to get **actionable insights** instead of general responses.
- Optimize data selection **before API calls** to reduce costs and improve relevance.
- Choose models based on complexity and budget.

By following these best practices, you can maximize OpenAI's value while efficiently leveraging BDX data for meaningful insights.

## Example Code

Below is example code where you can insert BDXpy code to generate chart on the left and an html summary of two difference responses back from OpenAI's API.

**Note:** these are purely for API example purposes and need heavy modification for custom implementation elsewhere.

```python
import openai
import networkx as nx
from pyvis.network import Network
import pandas as pd
from bdx.core import BDX
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.types import TimeFrame, AggregationLevel
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import json
import os
import markdown
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# BDX Credentials
BDX_URL = os.getenv("BDX_URL")
USERNAME = os.getenv("BDX_USERNAME")
PASSWORD = os.getenv("BDX_PASSWORD")
BUILDING_NAME = "Apex Building" #building name to match component lookups on

# AHUs to lookup VAVs on per matching logic below
AHU_NUMBERS = [1, 2, 3, 4, 6, 8]

# Connect to BDX
auth = UsernameAndPasswordAuthenticator(USERNAME, PASSWORD)
with BDX(BDX_URL, auth) as bdx:
    # ... (full BDX data retrieval code)
    pass

# Generate Summary with OpenAI (Using GPT-4o)
def generate_summary(anomalies):
    if not anomalies:
        return "<p>No significant anomalies detected in VAV airflow this week.</p>"

    # Customize this prompt depending on your model, needs, performance of the response, etc.
    prompt_text = f"""
    Given the following data on airflow changes for VAVs in a building:
    {json.dumps(anomalies, indent=2)}

    ### **Summary Instructions**
    - **Only report the most significant anomalies** (up to **5 individual VAVs**) OR if there is a **system-wide AHU issue** (total airflow of all VAVs under an AHU changes drastically).
    - **Exclude moderate changes** - I only care about extreme cases that could indicate performance, comfort, or system inefficiencies.
    - **If there are no significant changes**, state: "No major anomalies detected this week."
    - **Airflow data provided in an accumulation of CFM so units are CF
    - **Format the response as concise bullet points**, using **Markdown formatting** for readability.

    ### **Response Format**
    - **Key Findings**
        - **VAV_3_3:** Airflow increased **+89.09%**
        Likely cause: [Occupancy shift / Calibration issue / Setpoint change]
        Recommended action: [Verify control settings / Check mechanical operation]

    - **If AHU-wide issues exist, summarize them separately**
        - **AHU-1 System-Wide Change:** Total airflow increased by **+250,000 CF**, possibly due to [scheduling changes / pressure setpoint shift].
        Recommended action: [Check AHU damper settings / Review scheduling].

    Make sure the response is **short, direct, and action-oriented**.
    """

    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert in HVAC systems analyzing airflow changes."},
            {"role": "user", "content": prompt_text}
        ]
    )

    markdown_summary = response.choices[0].message.content
    return markdown.markdown(markdown_summary)

summary_text = generate_summary(anomalies)

print(f"Final version saved in 'VAV_network_summary_openai.html'. Open in a browser.")
```

---

**End of Documentation**

---

*BDXpy helps streamline building analytics - get started today!*

*Generated from BDXpy GitHub Pages documentation. For the most up-to-date information, visit: https://buildinglogix.github.io/BDXpy/*
