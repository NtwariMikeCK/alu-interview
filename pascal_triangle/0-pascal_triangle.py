#!/usr/bin/python3

"""This prints out the pascal's traingle"""
def pascal_traingle(n):
  """
  Generate Pascal's triangle up to the nth row.

  Args:
      n (int): The number of rows of Pascal's triangle to generate.

  Returns:
      List[List[int]]: A list of lists representing Pascal's triangle.
  """
  if n <= 0:
    return []
  triangle = [[1]]# Initialize with the first row
  for i in range(1, n):
    # Start the row with 1
    row = [1]
    # Compute the inner values by summing adjacent values from the previous row
    for j in range(1, i):
        row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    # End the row with 1
    row.append(1)
    triangle.append(row)

  return triangle
