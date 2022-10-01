# Do not remove these imports. You may add others if you wish.
import sys
import copy

# Args:
#   board: a list of list of strings, each list is a row of the board.
#          Each string will be "+" for impassable squares, and "0" for
#          squares the snake can move through.
#   row: an integer, the row the snake will start on
#   col: an integer, the column the snake will start on
#
# Returns:
#   A tuple of two ints, (row, col), the closest edge square the snake can exit.
#   If multiple are equally close, the one with smallest row value. If there
#   are multiple with smallest row value, the one with smallest column value.
#   If there are no answers, return (-1, -1)
def find_exit(board, row, column):
  # Your code goes here
  # NOTE: You may use print statements for debugging purposes, but you may
  #       need to remove them for the tests to pass.

  # locate all exits, if none, return (-1, -1)
  if all_exits:
    exits = all_exits(board, row, column)
    print("exits:" + str(exits))
  else:
    return (-1, -1)

  # compute length of each path (may need helper method)
  # select shortest path, if multiple, choose lowest row valuet then column value

  return find_shortest_path(board, exits, row, column)

def find_shortest_path(board, exits, row, column):
  # choose shortest
  dlist = paths_to_exits(board, exits, row, column)
  sorted(dlist, key=lambda tup: (tup[1]) )
  if dlist:
    return dlist[0]
  else:
    return (-1, -1)

def paths_to_exits(board, exits, row, column):
  # generate adjacency list
  # BFS, traverse all exits, if any, find shortest path
  # if found, add distance and exit to dlist
  # (mark visited with len)
  distance_matrix = copy.copy(board)
  h = len(board)
  l = len(board[0])
  print("h: " + str(h))
  print("l: "+ str(l))

  dlist = []
  adj = {}

  # generate adjacency list (works)
  for i in range(0, h):
      for j in range(0, l):
          adj[(i, j)] = []
          if board[i][j] == '0':
              add_adj(adj, board, i, j, h, l)

  print("adj: "+str(adj))

  # BFS for shortest paths from start to each exits
  start = (row, column)
  for exit in exits:
      dist = shortest_path(adj, start, exit)
      if dist != None:
          dlist.append([exit, dist])

  print("dlist: "+ str(dlist))
  return dlist

def shortest_path(adj, start, exit):
    # if exists, return dist, else return None
    

# works
def add_adj(adj, board, i, j, h, l):
    # not top row
    if i > 0:
        if board[i-1][j] == '0':
            adj[(i, j)].append((i-1, j))
        # not bottom row
        if i < h-1:
            if board[i+1][j] == '0':
                adj[(i, j)].append((i+1, j))
            # not left column
            if j > 0:
                if board[i][j-1] == '0':
                    adj[(i, j)].append((i, j-1))
                # not right column
                if j < l-1:
                    if board[i][j+1] == '0':
                        adj[(i, j)].append((i, j+1))
                else:
                    if board[i-1][j] == '0':
                        adj[(i, j)].append((i-1, j))
                    if board[i+1][j] == '0':
                        adj[(i, j)].append((i+1, j))
                    if board[i][j-1] == '0':
                        adj[(i, j)].append((i, j-1))
            else:
                if board[i-1][j] == '0':
                    adj[(i, j)].append((i-1, j))
                if board[i+1][j] == '0':
                    adj[(i, j)].append((i+1, j))
                if board[i][j+1] == '0':
                    adj[(i, j)].append((i, j+1))
        else:
            if board[i][j-1] == '0':
                adj[(i, j)].append((i, j-1))
            #print("i: "+str(i)+", j: "+ str(j))
            if board[i-1][j] == '0':
                adj[(i, j)].append((i-1, j))
            if board[i][j+1] == '0':
                adj[(i, j)].append((i, j+1))
    # top row
    else:
        if board[i][j-1] == '0':
            adj[(i, j)].append((i, j-1))
        if board[i+1][j] == '0':
            adj[(i, j)].append((i+1, j))
        if board[i][j+1] == '0':
            adj[(i, j)].append((i, j+1))
    return

# works
def all_exits(board, row, column):
  exits = []
  h = len(board)
  l = len(board[0])

  for itr,x in enumerate(board[0]):
    if x == '0':
      exits.append((0,itr))

  for ibr,x in enumerate(board[len(board)-1]):
    if x == '0':
      exits.append((h-1,ibr))


  for lc in range(0,h):
    if board[lc][0] == '0':
      exits.append((lc, 0))

  for rc in range(0,h):
    if board[rc][l-1] == '0':
      exits.append((rc, l))
  #exits.remove([[row, column]])
  #sorted(exits, key=lambda tup: (tup[0],tup[1]) )
  return exits


# tests
# DO NOT MODIFY BELOW THIS LINE
def main(board, start):
  # start = None
  # board = []

  # for line in sys.stdin:
  #   if len(line.strip()) == 0:
  #     continue
    #
    # if start is None:
    #   start = tuple(int(x) for x in line.rstrip().split(" "));
    # else:
    #   board.append(line.rstrip().split(" "))

  print(" ".join(str(x) for x in find_exit(board, *start)))

# board0
board0 = [
['+','0','0','0','+'],
['+','0','+','0','+'],
['+','0','0','0','+'],
['+','0','+','0','+'],
]

start0 = (3, 1) # end to be (0, 1)

main(board0, start0)






# -------------------------------------------------------------------
# testing code recycle

'''
while(c_row-1>=0 and distance_matrix[c_row-1][c_column]!='+'):
  dist = dist + 1
  distance_matrix[c_row-1][c_column] = dist
  c_row = c_row - 1
  if distance_matrix[c_row][c_column] in exits:
    dlist.append(((c_row, c_column), dist))

  while(c_column+1<l and distance_matrix[c_row][c_column+1]!='+'):
    dist = dist + 1
    distance_matrix[c_row][c_column+1] = dist
    c_column = c_column + 1
    if distance_matrix[c_row][c_column] in exits:
      dlist.append(((c_row, c_column), dist))

    while(c_row+1<h and distance_matrix[c_row+1][c_column]!='+'):
      dist = dist + 1
      distance_matrix[c_row+1][c_column] = dist
      c_row = c_row + 1
      if distance_matrix[c_row][c_column] in exits:
        dlist.append(((c_row, c_column), dist))

      while(c_column-1>=0 and distance_matrix[c_row][c_column-1]!='+'):
        dist = dist + 1
        distance_matrix[c_row][c_column-1] = dist
        c_column = c_column - 1
        if distance_matrix[c_row][c_column] in exits:
          dlist.append(((c_row, c_column), dist))
'''
