#-------------------------------------------------------------------------------
# Name:        jgraph
# Purpose:
#
# Author:      jerry
#
# Created:     20/11/2013
# Copyright:   (c) jerry 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class JGraph:
    def __init__(self, strings = []):
        self.__gDict = {}
        self.__gMax = []
        self.buildDict(strings)
        self.buildMax(strings)

    #depth first search - use Stack
    def dfs(self, startNode):
        stack = []
        vsNodes = []

        vsNodes.append(startNode)
        stack.append(startNode)
        ctn = len(self.__gDict)

        print(startNode, end=' ')
        while len(stack) > 0:
            cur = stack[-1]
            tmp = self.getNeighbor(cur, vsNodes)
            if (tmp is not None):
                print(tmp, end=' ')
                vsNodes.append(tmp)
                stack.append(tmp)
            else:
                stack.pop()

    #breadth first search - use Queue
    def bfs(self, startNode):
        queue = []
        vsNodes = []

        queue.append(startNode)
        vsNodes.append(startNode)

        while (len(queue) > 0):
            cur = queue.pop(0)
            neighbors = self.getAllNeighbors(cur, vsNodes)
            queue.extend(neighbors)
            vsNodes.append(cur)
            print(cur, end =' ')


    def getNeighbor(self, node, vsNodes):
        idx = self.__gDict[node]
        cnt = len(self.__gDict)

        for i in range(0, cnt):
            if idx != i and self.__gMax[idx][i] == 1:
                if self.getKey(i) not in vsNodes:
                    return self.getKey(i)

        return None

    def getAllNeighbors(self, node, vsNodes):
        idx = self.__gDict[node]
        cnt = len(self.__gDict)
        neighbors= []

        for i in range(0, cnt):
            if(idx != i) and self.__gMax[idx][i] == 1:
                tmp = self.getKey(i)
                if (tmp not in vsNodes):
                    neighbors.append(tmp)

        return neighbors


    def getKey(self, idx):
        for key, value in self.__gDict.items():
            if idx == value:
                return key
        return None

    #helpers
    def buildDict(self, strings):
        idx = 0
        for st in strings:
            tmp = list(st)
            for c in tmp:
                if c not in self.__gDict:
                    self.__gDict[c] = idx
                    idx += 1

    def buildMax(self, strings):
        cnt = len(self.__gDict)
        #init with 0's
        for i in range(0, cnt):
            tmp = []
            for j in range(0, cnt):
                tmp.append(0)
            self.__gMax.append(tmp)

        for st in strings:
            tmp = list(st)
            x = self.__gDict[tmp[0]]
            y = self.__gDict[tmp[1]]
            self.__gMax[x][y] = 1
            self.__gMax[y][x] = 1


def main():
    #strings = ["AB", "AC", "AE", "BD", "DF", "CG"]
    strings = ["12", "13", "14", "25", "26", "47", "48", "59", "5A", "7B", "7C"]
    myGraph = JGraph(strings)

    myGraph.dfs('1')
    print()
    myGraph.bfs('1')


if __name__ == '__main__':
    main()
