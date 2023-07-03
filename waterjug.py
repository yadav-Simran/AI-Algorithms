from collections import deque

class Pair:
    def _init_(self, j1, j2, path=[]):
        self.j1 = j1
        self.j2 = j2
        self.path = path + [(j1, j2)]

def getPathIfPossible(jug1, jug2, target):
    visited = [[False] * (jug2 + 1) for _ in range(jug1 + 1)]
    queue = deque()

    # Initial State: Both Jugs are empty so,
    # initialise j1 j2 as 0 and put it in the path list
    initialState = Pair(0, 0)
    queue.append(initialState)

    while queue:
        curr = queue.popleft()

        # Skip already visited states and overflowing water states
        if curr.j1 > jug1 or curr.j2 > jug2 or visited[curr.j1][curr.j2]:
            continue
        # mark current jugs state as visited
        visited[curr.j1][curr.j2] = True

        # Check if current state has already reached the target amount of water or not
        if curr.j1 == target or curr.j2 == target:
            if curr.j1 == target:
                # If in our current state, jug1 holds the required amount of water, then we
                # empty the jug2 and push it into our path.
                curr.path.append((curr.j1, 0))
            else:
                # else, If in our current state, jug2 holds the required amount of water,
                # then we empty the jug1 and push it into our path.
                curr.path.append((0, curr.j2))

            print("Path of states of jugs followed is :")
            for state in curr.path:
                print(f"{state[0]}, {state[1]}")
            return

        # If we have not yet found the target, then we have three cases left
        # I. Fill the jug and Empty the other
        # II. Fill the jug and let the other remain untouched
        # III. Empty the jug and let the other remain untouched
        # IV. Transfer amounts from one jug to another

        # Please refer to the table attached above to understand the cases that we are taking into consideration

        # Now,
        # I. Fill the jug and Empty the other
        queue.append(Pair(jug1, 0, curr.path))
        queue.append(Pair(0, jug2, curr.path))

        # II. Fill the jug and let the other remain untouched
        queue.append(Pair(jug1, curr.j2, curr.path))
        queue.append(Pair(curr.j1, jug2, curr.path))

        # III. Empty the jug and let the other remain untouched
        queue.append(Pair(0, curr.j2, curr.path))
        queue.append(Pair(curr.j1, 0, curr.path))

        # IV. Transfer water from one to another until one jug becomes empty or until one jug
        # becomes full in this process

        # Transferring water form jug1 to jug2
        emptyJug = jug2 - curr.j2
        amountTransferred = min(curr.j1, emptyJug)
        j2 = curr.j2 + amountTransferred
        j1 = curr.j1 - amountTransferred
        queue.append(Pair(j1, j2, curr.path))

        # Transferring water form jug2 to jug1
        emptyJug = jug1 - curr.j1
        amountTransferred
if _name_ == '_main_':
 
    Jug1, Jug2, target = 5 , 3 , 4
    print("Path from initial state "
          "to solution state ::")
 
    getPathIfPossible(Jug1, Jug2, target)