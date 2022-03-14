# Deputy Coding Assessment


## Getting Started

These instructions will get you a copy of the project up and running on your 
local machine for development and testing purposes.

### Prerequisites

- [Python 3.8.9+](https://www.python.org/downloads/)

### Installing

Pytest is the only external library. Use pip to install it.

```shell
pip3 install pytest
```

## Running the Tests

To run the unit tests, use pytest.

```shell
pytest
```

## Running the Code

I've added `main.py` as the main entry point to the project. You'll see the 
standard `if __name__ == '__main__'` block that get's executed on invocation of 
the file. To run it use:

```shell
python3 main.py
```

If you want to play around with it, you'll see that there's a `get_subordinates`
method attached to `EmployeeHierarchy` in `EmployeeHierarchy.py`. The naming
intentionally doesn't match the spec to improve readability with the rest of
the code. It performs the same function. 

If you'd like to change the data, modify `users.json` and `roles.json` to include
your own dataset.

# Assumptions:
- There are potentially more than 1 roots to the trees.
- Each role/employee ID is unique.
- IDs can be any integer, including negatives and zero.

# Design Decisions:
- I've traded space for faster runtimes because (my own assumption) the business cares about user experience (speed) 
more than the business cares about saving money on memory.
- There are potentially multiple roots to a tree.
  - The spec doesn't specify that there's always a single root node. 
  - This increases the complexity of the problem to where a simple tree traversal or DAG isn't sufficient. If we were 
    always guaranteed to have a single root node then the code is simplified and more 
    readable, with a simple bread-first-search solution to get subordinates.
- I've kept it relatively light weight. I didn't want to use unnecessary external libs when this is a once off implementation.
  - If you extended the code to read from CSVs or otherwise do more complex operations you might consider libraries to:
    - Simply read and manipulate CSV input (pandas).
    - Convert classes to PODs using dataclasses and add field verification (pydantic).
    - and so on.
- I've kept OOP low enough to understand the code without being too convoluted.
  - To remain extensible, if more work were to be done, future devs may want to 
refactor the `EmployeeHierarchy` class into different classes to better adhere to SOLID principles.
    - One such example is by refactoring out the adjacency list.
- I've intentionally not added command line arguments, such as passing in input files.
  - To achieve this you can easily use the [configparser](https://docs.python.org/3/library/configparser.html)
  library.
