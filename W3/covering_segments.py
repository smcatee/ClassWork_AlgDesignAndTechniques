# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(n, segments):
    points = []
    startPts = []
    endPts = []
    startEndMatrix = [[0]*n for _ in range(n)]

    for i, curSeg in enumerate(segments):
        startPt, endPt = curSeg
        startPts.append(startPt)
        endPts.append(endPt)

        for j, curEnd in enumerate(endPts):
            if(i > j):
                startEndMatrix[i][j] = int(startPt <= curEnd)
            else:
                for curRow, curStart in enumerate(startPts):
                    startEndMatrix[curRow][j] = int(curStart <= curEnd)
    
    while startEndMatrix:
        segOverlapSum = [0]*(len(startEndMatrix))
        for i, curRow in enumerate(startEndMatrix):
            segOverlapSum[i] += sum(curRow)
            for j, curElem in enumerate(curRow):
                segOverlapSum[j] += curElem

        leastOverlapsIndex = segOverlapSum.index(min(segOverlapSum))
        overlapPoint = 0

        overlapingIndexes = []
        i = 0
        while i < len(startEndMatrix):
            if(startEndMatrix[i][leastOverlapsIndex] & startEndMatrix[leastOverlapsIndex][i]):
                overlapPoint = max(overlapPoint, startPts[i])
                overlapingIndexes.append(i)
            i += 1

        for ind in reversed(overlapingIndexes):
            del startPts[ind], endPts[ind], startEndMatrix[ind]
            for curRow in startEndMatrix:
                del curRow[ind]

        
        points.append(overlapPoint)
        
        

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(n, segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
