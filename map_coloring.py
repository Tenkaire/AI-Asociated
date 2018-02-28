import time
import operator

# G = [[1, 2, 3], [2, 1, 3], [3, 1, 2], [4, 5], [5, 4]]
# n = 5
# k = 3

G = [[1, 2, 3, 4, 6, 7, 10], [2, 1, 3, 4, 5, 6], [3, 1, 2], [4, 1, 2], [5, 2, 6], [6, 1, 2, 5, 7, 8],
     [7, 1, 6, 8, 9, 10], [8, 6, 7, 9], [9, 7, 8, 10], [10, 1, 7, 9]]
n = 10
k = 4


def solve(n, k, G):
    return recursive_backtracking([], n, k, G)


def recursive_backtracking(assignment, n, k, G):
    G_copy = G[:]

    if len(assignment) == n:
        return assignment

    var = select_unassigned_variable_by_degree(assignment, n, k, G_copy)
    # var = select_unassigned_variable_by_mrv(assignment, n, k, G_copy)
    # var = select_unassigned_variable_by_order(assignment, n, k, G_copy)

    ##########################################################################################
    ##########################################################################################
    color = list(range(1, k + 1))
    result = []
    for items in color:
        result.append((find_least_constraining_value(n, k, G, assignment, var, items), items))
    result.sort(key=operator.itemgetter(0))

    for tuples in result:
        value = tuples[1]
        ##########################################################################################
        ################       least constraining value     ######################################

        ##########################################################################################
        # for value in range (1, k+1):
        ##########################################################################################
        if consistency(var, value, assignment, G):
            assignment.append((var, value))
            result = recursive_backtracking(assignment, n, k, G_copy)
            if result != False:
                return result

            assignment.remove((var, value))
    return False


def consistency(var, value, assignment, G):
    for lists in G:
        for neighbor in lists:
            if var == lists[0] and neighbor != var and (var, value) not in assignment and (
            neighbor, value) in assignment:
                increment()
                return False
    return True


def select_unassigned_variable_by_degree(assignment, n, k, G):
    largest_degree = 0
    for var in G:
        counter = 0
        for i in range(1, len(var)):
            for j in assignment:
                if i == j[0]:
                    counter += 1
        if (len(var) - counter) > largest_degree:
            largest_degree = len(var) - counter
            largest = var[0]
            assigned = var
    G.remove(assigned)
    return largest


def select_unassigned_variable_by_mrv(assignment, n, k, G):
    smallest_remaining = float("inf")
    index = []
    counter = 0
    mrv = 0
    for lists in G:
        for neighbor in range(1, len(lists)):
            for assigned in assignment:
                if neighbor == assigned[0]:
                    if assigned[1] not in index:
                        counter += 1
                    else:
                        counter += 1
                        index.append(assigned[1])
        if smallest_remaining > counter:
            smallest_remaining = counter
            mrv = lists[0]
            var_assigned = lists
    G.remove(var_assigned)
    return mrv


def select_unassigned_variable_by_order(assignment, n, k, G):
    var = G[0][0]
    G.remove(G[0])
    return var


def find_least_constraining_value(n, k, G, assignment, var, value):
    target = []
    for variables in G:
        if variables[0] == var:
            target = target.copy()
    for item in target:
        for variables in assignment:
            if item == variables[0]:
                target.remove(item)
    counter = 0
    for item in target:
        colors = list(range(1, k + 1))
        neighbor = []
        for vars in G:
            if vars[0] == item:
                neighbor = vars[0:]
        for items in neighbor:
            for assigned_items in assignment:
                if items == assigned_items[0]:
                    if assigned_items[1] in colors:
                        colors.remove(assigned_items[1])
        if value in colors:
            counter += 1
    return counter


check_failed = 0


def increment():
    global check_failed
    check_failed += 1


start_time = time.clock()
sol = solve(n, k, G)
end_time = time.clock()
duration = end_time - start_time

print(sol)
print(duration, "seconds")
print(check_failed, "times check.")