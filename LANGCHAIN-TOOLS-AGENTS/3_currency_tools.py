# =========================================================
# IMPORTS
# =========================================================

import requests

from typing import Annotated

from langchain_core.tools import (

    tool,

    InjectedToolArg
)

# =========================================================
# TOOL 1
# =========================================================

@tool
def get_conversion_factor(

    base_currency: str,

    target_currency: str

) -> float:

    """
    Fetch currency conversion factor
    """

    url = f"https://v6.exchangerate-api.com/v6/YOUR_API_KEY/pair/{base_currency}/{target_currency}"

    response = requests.get(url)

    return response.json()

# =========================================================
# TOOL 2
# =========================================================

@tool
def convert(

    base_currency_value: int,

    conversion_rate: Annotated[
        float,
        InjectedToolArg
    ]

) -> float:

    """
    Convert currency
    """

    return base_currency_value * conversion_rate