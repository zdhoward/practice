from random import randint, shuffle

solved = None
level = 0

moves = list(range(1, 10))


def main():
    global solved
    state = {"num": 0, "increments": [], "max": 100}
    if recursive_run(state):
        print("Solved:\n", solved)


def recursive_run(_state):
    global moves
    shuffle(moves)
    for move in moves:
        if isAllowed(_state, move):
            _state["num"] += move
            _state["increments"].append(move)
            if isCompleted(_state):
                return True
            if recursive_run(_state):
                return True
    return False


def isAllowed(_state, _move):
    if _state["num"] + _move <= _state["max"]:
        return True
    return False


def isCompleted(_state):
    global solved
    if _state["num"] == _state["max"]:
        solved = _state
        print("COMPLETE")
        return True
    return False


if __name__ == "__main__":
    main()
