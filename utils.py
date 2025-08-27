import pandas as pd
import numpy as np

def removeLeadingQuotations(title):
    """Remove leading quotation marks from a title string."""
    return title.strip('"').strip("'")