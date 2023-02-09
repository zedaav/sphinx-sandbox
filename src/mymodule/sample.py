"""
Sample module, just used to demonstrate doc generation features.

Some additional test, just to check **how** it *goes*
"""
from typing import List


def get_random_ingredients(kind: List[str] = None) -> List[str]:
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: List[str] or None
    :raise ValueError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: List[str]

    """
    return ["shells", "gorgonzola", "parsley"]
