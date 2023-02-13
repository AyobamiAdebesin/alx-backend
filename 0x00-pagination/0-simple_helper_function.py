#!/usr/bin/env python3
"""A simple helper function"""


def index_range(page: int, page_size: int):
    """
    Returns a tuple containing a start index and
    an end index corresponding to the range of
    indexes to return in a list for those particular
    pagination parameters.

    page: this is analogous to offset in offset pagination
    page_size: this is analogous to limit in offset pagination
    """
    start_idx = 0
    end_idx = 0
    for i in range(page):
        start_idx = end_idx
        end_idx += page_size
    return (start_idx, end_idx)
