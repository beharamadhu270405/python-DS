
"""
👾 List Items
List items are 
    -ordered, 
    -changeable, 
    -and allow duplicate values.

List items are indexed, 
    the first item has index [0], 
    the second item has index [1] etc.
"""

from icecream import ic
from datetime import datetime
from typing import Any, Union, List, Iterable


def time_format():
    return f'{datetime.now().strftime("%m/%d/%Y, %I:%M:%S")}|> '


ic.configureOutput(prefix=time_format, includeContext=True)


class ListOperations:
    def __init__(self, listInit=[]):
        self.listItem = []

    """Properties For Access List elements"""

    def getEntireList(self):
        return self.listItem

    def getItem(self, index: int) -> Union[None, int, str]:
        return self.listItem[index] or None

    def getLastItem(self) -> Union[None, List]:
        return self.listItem[-1] or None

    def getItemAfterListSlicing(self, startIndex: int, endIndex: int) -> List:
        """
        The search will start at startIndex (included) 
            and end at endIndex (not included)
        """
        return self.listItem[startIndex:endIndex] or None

    def getLength(self):
        return len(self.listItem)

    def checkIfItemExistsOrNot(self, item: Any) -> bool:
        return item in self.listItem

    """Properties For Modifying List elements"""

    def appendItem(self, item: Any):
        return self.listItem.append(item)

    def insertElementAtSpecificIndex(self, item: Any, index: int) -> List:
        return self.listItem.insert(index, item)

    def extendTheList(self, newlist: Iterable) -> List:
        """
        The extend() method does not have to append lists,
        you can add any iterable object
        (tuples, sets, dictionaries etc.).
        """
        self.listItem.extend(newlist)
        return self.listItem

    """Properties For Removing List Items"""

    def removeItemFromList(self, item: Any) -> List:
        return self.listItem.remove(item)

    def removeItemFromListSpecificIndex(self, index: int) -> List:
        """
        If you do not specify the index, 
        the pop() method removes the last item.
        """
        return self.listItem.pop(index)

    def deleteItemFromListSpecificIndex(self, index: int) -> List:
        """
        If you do not specify the index, 
        the pop() method removes the last item.
        """
        del self.listItem[index]
        return self.listItem

    def deleteEntireList(self):
        del self.listItem
        return self.listItem

    def clearEntireList(self):
        """
        The clear() method empties the list.
        The list still remains, but it has no content.
        """
        return self.listItem.clear()


if __name__ == '__main__':
    newListObj = ListOperations()
    ic(newListObj.getEntireList())
    ic(newListObj.extendTheList(['apple', True, 'Man']))
    ic(newListObj.getEntireList())
