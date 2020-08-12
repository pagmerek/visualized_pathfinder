from queue import LifoQueue
from collections import deque
from sys import float_info

def isValid(row, col):
    return 0 <= row < 30 and 0 <= col < 30


def isUnblocked(row, col, all_rects):
    return all_rects[row][col][0].kind != "obstacle"


def isDestination(row, col, end):
    return row == end[1] and col == end[0]


def calculate_Heurisitc(row, col, end):
    return max(abs(col - end[0]), abs(row - end[1]))


def tracePath(all_rects, end):
    row = end[1]
    col = end[0]

    stack = LifoQueue()

    while all_rects[row][col][0].parentRow != row or all_rects[row][col][0].parentCol != col:
        stack.put((row, col))
        temp_row = all_rects[row][col][0].parentRow
        temp_col = all_rects[row][col][0].parentCol
        row = temp_row
        col = temp_col

    stack.put((row, col))
    while not stack.empty():
        p, q = stack.get()
        all_rects[p][q][1] = (255, 0, 0)


def aStarSearch(start, end, all_rects):
    i, j = start
    all_rects[j][i][0].F_value = 0.0
    all_rects[j][i][0].G_value = 0.0
    all_rects[j][i][0].H_value = 0.0
    all_rects[j][i][0].parentCol = i
    all_rects[j][i][0].parentRow = j

    openList = deque()
    openList.append((0.0, (i, j)))

    foundDest = False

    while len(openList) != 0:
        p = openList.popleft()
        i, j = p[1]
        all_rects[j][i][0].visited = True
        all_rects[j][i][1] = (255, 182, 193)
        gNew, hNew, fNew = 0, 0, 0
        # North
        if isValid(j - 1, i):
            if isDestination(j - 1, i, end):
                all_rects[j - 1][i][0].parentCol = i
                all_rects[j - 1][i][0].parentRow = j
                tracePath(all_rects, end)
                foundDest = True
                return
            elif not all_rects[j - 1][i][0].visited and isUnblocked(j - 1, i, all_rects):
                gNew = all_rects[j][i][0].G_value + 1.0
                hNew = calculate_Heurisitc(j - 1, i, end)
                fNew = gNew + hNew

                if all_rects[j - 1][i][0].F_value == float_info.max or all_rects[j - 1][i][0].F_value > fNew:
                    openList.append((fNew, (i, j - 1)))
                    all_rects[j - 1][i][0].F_value = fNew
                    all_rects[j - 1][i][0].G_value = gNew
                    all_rects[j - 1][i][0].H_value = hNew
                    all_rects[j - 1][i][0].parentCol = i
                    all_rects[j - 1][i][0].parentRow = j
                    all_rects[j - 1][i][1] = (0, 255, 0)
        # South
        if isValid(j + 1, i):
            if isDestination(j + 1, i, end):
                all_rects[j + 1][i][0].parentCol = i
                all_rects[j + 1][i][0].parentRow = j
                tracePath(all_rects, end)
                foundDest = True
                return
            elif not all_rects[j + 1][i][0].visited and isUnblocked(j + 1, i, all_rects):
                gNew = all_rects[j][i][0].G_value + 1.0
                hNew = calculate_Heurisitc(j + 1, i, end)
                fNew = gNew + hNew

                if all_rects[j + 1][i][0].F_value == float_info.max or all_rects[j + 1][i][0].F_value > fNew:
                    openList.append((fNew, (i, j + 1)))
                    all_rects[j + 1][i][0].F_value = fNew
                    all_rects[j + 1][i][0].G_value = gNew
                    all_rects[j + 1][i][0].H_value = hNew
                    all_rects[j + 1][i][0].parentCol = i
                    all_rects[j + 1][i][0].parentRow = j
                    all_rects[j + 1][i][1] = (0, 255, 0)

        # East
        if isValid(j, i + 1):
            if isDestination(j, i + 1, end):
                all_rects[j][i + 1][0].parentCol = i
                all_rects[j][i + 1][0].parentRow = j
                tracePath(all_rects, end)
                foundDest = True
                return
            elif not all_rects[j][i + 1][0].visited and isUnblocked(j, i + 1, all_rects):
                gNew = all_rects[j][i][0].G_value + 1.0
                hNew = calculate_Heurisitc(j, i + 1, end)
                fNew = gNew + hNew

                if all_rects[j][i + 1][0].F_value == float_info.max or all_rects[j][i + 1][0].F_value > fNew:
                    openList.append((fNew, (i + 1, j)))
                    all_rects[j][i + 1][0].F_value = fNew
                    all_rects[j][i + 1][0].G_value = gNew
                    all_rects[j][i + 1][0].H_value = hNew
                    all_rects[j][i + 1][0].parentCol = i
                    all_rects[j][i + 1][0].parentRow = j
                    all_rects[j][i + 1][1] = (0, 255, 0)

        # West
        if isValid(j, i - 1):
            if isDestination(j, i - 1, end):
                all_rects[j][i - 1][0].parentCol = i
                all_rects[j][i - 1][0].parentRow = j
                tracePath(all_rects, end)
                foundDest = True
                return
            elif not all_rects[j][i - 1][0].visited and isUnblocked(j, i - 1, all_rects):
                gNew = all_rects[j][i][0].G_value + 1.0
                hNew = calculate_Heurisitc(j, i - 1, end)
                fNew = gNew + hNew

                if all_rects[j][i - 1][0].F_value == float_info.max or all_rects[j][i - 1][0].F_value > fNew:
                    openList.append((fNew, (i - 1, j)))
                    all_rects[j][i - 1][0].F_value = fNew
                    all_rects[j][i - 1][0].G_value = gNew
                    all_rects[j][i - 1][0].H_value = hNew
                    all_rects[j][i - 1][0].parentCol = i
                    all_rects[j][i - 1][0].parentRow = j
                    all_rects[j][i - 1][1] = (0, 255, 0)

        # South - West
        if isValid(j + 1, i - 1):
            if isDestination(j + 1, i - 1, end):
                all_rects[j + 1][i - 1][0].parentCol = i
                all_rects[j + 1][i - 1][0].parentRow = j
                tracePath(all_rects, end)
                foundDest = True
                return
            elif not all_rects[j + 1][i - 1][0].visited and isUnblocked(j + 1, i - 1, all_rects):
                gNew = all_rects[j][i][0].G_value + 1.0
                hNew = calculate_Heurisitc(j + 1, i - 1, end)
                fNew = gNew + hNew

                if all_rects[j + 1][i - 1][0].F_value == float_info.max or all_rects[j + 1][i - 1][0].F_value > fNew:
                    openList.append((fNew, (i - 1, j + 1)))
                    all_rects[j + 1][i - 1][0].F_value = fNew
                    all_rects[j + 1][i - 1][0].G_value = gNew
                    all_rects[j + 1][i - 1][0].H_value = hNew
                    all_rects[j + 1][i - 1][0].parentCol = i
                    all_rects[j + 1][i - 1][0].parentRow = j
                    all_rects[j + 1][i - 1][1] = (0, 255, 0)

        # North West
        if isValid(j - 1, i - 1):
            if isDestination(j - 1, i - 1, end):
                all_rects[j - 1][i - 1][0].parentCol = i
                all_rects[j - 1][i - 1][0].parentRow = j
                tracePath(all_rects, end)
                foundDest = True
                return
            elif not all_rects[j - 1][i - 1][0].visited and isUnblocked(j - 1, i - 1, all_rects):
                gNew = all_rects[j][i][0].G_value + 1.0
                hNew = calculate_Heurisitc(j - 1, i - 1, end)
                fNew = gNew + hNew

                if all_rects[j - 1][i - 1][0].F_value == float_info.max or all_rects[j - 1][i - 1][0].F_value > fNew:
                    openList.append((fNew, (i - 1, j - 1)))
                    all_rects[j - 1][i - 1][0].F_value = fNew
                    all_rects[j - 1][i - 1][0].G_value = gNew
                    all_rects[j - 1][i - 1][0].H_value = hNew
                    all_rects[j - 1][i - 1][0].parentCol = i
                    all_rects[j - 1][i - 1][0].parentRow = j
                    all_rects[j - 1][i - 1][1] = (0, 255, 0)

        # North - East
        if isValid(j - 1, i + 1):
            if isDestination(j - 1, i + 1, end):
                all_rects[j - 1][i + 1][0].parentCol = i
                all_rects[j - 1][i + 1][0].parentRow = j
                tracePath(all_rects, end)
                foundDest = True
                return
            elif not all_rects[j - 1][i + 1][0].visited and isUnblocked(j - 1, i + 1, all_rects):
                gNew = all_rects[j][i][0].G_value + 1.0
                hNew = calculate_Heurisitc(j - 1, i + 1, end)
                fNew = gNew + hNew

                if all_rects[j - 1][i + 1][0].F_value == float_info.max or all_rects[j - 1][i + 1][0].F_value > fNew:
                    openList.append((fNew, (i + 1, j - 1)))
                    all_rects[j - 1][i + 1][0].F_value = fNew
                    all_rects[j - 1][i + 1][0].G_value = gNew
                    all_rects[j - 1][i + 1][0].H_value = hNew
                    all_rects[j - 1][i + 1][0].parentCol = i
                    all_rects[j - 1][i + 1][0].parentRow = j
                    all_rects[j - 1][i + 1][1] = (0, 255, 0)

        # South - East
        if isValid(j + 1, i + 1):
            if isDestination(j + 1, i + 1, end):
                all_rects[j + 1][i + 1][0].parentCol = i
                all_rects[j + 1][i + 1][0].parentRow = j
                tracePath(all_rects, end)
                foundDest = True
                return
            elif not all_rects[j + 1][i + 1][0].visited and isUnblocked(j + 1, i + 1, all_rects):
                gNew = all_rects[j][i][0].G_value + 1.0
                hNew = calculate_Heurisitc(j + 1, i + 1, end)
                fNew = gNew + hNew

                if all_rects[j + 1][i + 1][0].F_value == float_info.max or all_rects[j + 1][i + 1][0].F_value > fNew:
                    openList.append((fNew, (i + 1, j + 1)))
                    all_rects[j + 1][i + 1][0].F_value = fNew
                    all_rects[j + 1][i + 1][0].G_value = gNew
                    all_rects[j + 1][i + 1][0].H_value = hNew
                    all_rects[j + 1][i + 1][0].parentCol = i
                    all_rects[j + 1][i + 1][0].parentRow = j
                    all_rects[j + 1][i + 1][1] = (0, 255, 0)

    if not foundDest:
        return 1
