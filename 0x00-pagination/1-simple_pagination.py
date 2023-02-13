#!/usr/bin/env python3
""" A simple pagination """
import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """ Helper function for a simple pagination """
    start_idx = 0
    end_idx = 0

    for i in range(page):
        start_idx = end_idx
        start_idx += page_size
    return (start_idx, end_idx)


class Server:
    """
    Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Name.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get the paginated pages from the dataset using index_range
        helper function
        """
        assert page > 0, "page and page_size must be greater then zero"
        assert page_size > 0, "page_size must be greater than zero"
        start_idx, end_idx = index_range(page, page_size)
        if end_idx > len(self.dataset()):
            return []
        get_pages = self.dataset()[start_idx: end_idx]
        return get_pages
