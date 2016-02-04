# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import pdb

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    visited = set()
    fringe = util.Stack()
    start = []
    start.append(problem.getStartState())
    fringe.push(start)
    while not fringe.isEmpty():
        if fringe.isEmpty():
            return "Goal state not found."
        node = fringe.pop()
        if problem.isGoalState(node[0]):
            return node[1]
        if node[0] not in visited:
            visited.add(node[0])
            for (successor, action, cost) in problem.getSuccessors(node[0]):
                if (len(node) == 1): #edge case: No actions yet for the start state
                    actionSequence = []
                else:
                    actionSequence = list(node[1])
                actionSequence.append(action)
                fringe.push((successor, actionSequence)) 
                #node is a tuple of (position, list of actions to reach node)
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    visited = set()
    #pdb.set_trace()
    fringe = util.Queue()
    #print problem.getStartState()
    #start.append(problem.getStartState())
    #print start
    pdb.set_trace()
    if type(problem.getStartState) == tuple:
        start = []
        start.append(problem.getStartState())
    else:
        start = problem.getStartState()
    fringe.push(start)
    while not fringe.isEmpty():
        if fringe.isEmpty():
            return "Goal state not found."
        node = fringe.pop()
        print node[:-1]
        if problem.isGoalState(node[:-1]):
            pdb.set_trace()
            print node
            print node[-1]
            return node[-1]
        #print node[0]
        #print node[1]
        if node[0] not in visited:
            visited.add(node[0])
            for (successor, action, cost) in problem.getSuccessors(node[0]):
                if (node == problem.getStartState()): #edge case: No actions yet for the start state
                    """
                    # Concatenate all elements--no actionSequence in node yet
                    successorState = []
                    for each in successor:
                        successorState.append(each)
                    """
                    #print successor
                    #print action
                    stringToList = []
                    stringToList.append(action)
                    successor.append(stringToList)
                    #print successor
                    fringe.push(successor)
                    #print fringe.isEmpty()
                else:
                    actionSequence = list(node[-1])
                    actionSequence.append(action)
                    """
                    # Concatenate all but last element--actionSequence
                    successorState = []
                    for i in range(0, len(successor - 2)):
                        successorState.append(successor[i])
                    """
                    successor.append(actionSequence)
                    fringe.push(successor)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    visited = set()
    fringe = util.PriorityQueue()
    start = []
    start.append(problem.getStartState())
    fringe.push(start, 0)
    while not fringe.isEmpty():
        if fringe.isEmpty():
            return "Goal state not found."
        node = fringe.pop()
        if problem.isGoalState(node[0]):
            return node[1]
        if node[0] not in visited:
            visited.add(node[0])
            for (successor, action, cost) in problem.getSuccessors(node[0]):
                if (len(node) == 1): #edge case: No actions yet for the start state
                    actionSequence = []
                else:
                    actionSequence = list(node[1])
                actionSequence.append(action)
                fringe.push((successor, actionSequence), cost)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    visited = set()
    fringe = util.PriorityQueue()
    start = []
    start.append(problem.getStartState())
    fringe.push(start, heuristic)
    while not fringe.isEmpty():
        if fringe.isEmpty():
            return "Goal state not found."
        node = fringe.pop()
        if problem.isGoalState(node[0]):
            return node[1]
        if node[0] not in visited:
            visited.add(node[0])
            for (successor, action, cost) in problem.getSuccessors(node[0]):
                if (len(node) == 1): #edge case: No actions yet for the start state
                    actionSequence = []
                else:
                    actionSequence = list(node[1])
                actionSequence.append(action)
                #Successors are pushed onto the fringe with the combination priority of the heuristic for successor
                #and the cost of actions to get to that successor.
                fringe.push((successor, actionSequence), heuristic(successor, problem) 
                    + problem.getCostOfActions(actionSequence))
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
