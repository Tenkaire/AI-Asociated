from queue import PriorityQueue


def neighbour(node_status, grid_size):
    neigbour_set = []
    node_status_x = node_status[0]
    node_status_y = node_status[1]
    if node_status_x > 1:
        neigbour_set.append((node_status_x - 1, node_status_y))
    if node_status_y > 1:
        neigbour_set.append((node_status_x, node_status_y - 1))
    if node_status_x < grid_size:
        neigbour_set.append((node_status_x + 1, node_status_y))
    if node_status_y < grid_size:
        neigbour_set.append((node_status_x, node_status_y + 1))
    return neigbour_set


def least_cost_path(grid_size, start_location, goal_location, grid_cost_value):
    node_status = start_location
    frontier_set = PriorityQueue()
    frontier_set.put((0, [start_location]))
    explored_set = []

    if node_status == goal_location:
        return [start_location]
    if frontier_set.empty():
        return FileExistsError
    while frontier_set:
        cost_counter, path = frontier_set.get()
        node_status = path[-1]
        if node_status == goal_location:
            return path
        elif node_status not in explored_set:
            explored_set.append(node_status)

            for nodes in neighbour(node_status, grid_size):
                if nodes not in explored_set:
                    x = nodes[0]
                    y = nodes[1]
                    new_list = path + [(x, y)]
                    frontier_set.put((cost_counter + grid_cost_value[x - 1][y - 1] + 1, new_list))
    return path


grid_value_set = [[4, 3, 3, 4, 2], [2, 4, 4, 2, 2], [3, 4, 5, 3, 2], [2, 3, 4, 5, 2], [4, 3, 3, 2, 4]]
shortest_path = least_cost_path(5, (1, 1), (5, 4), grid_value_set)
print(shortest_path)

# grid_size = input("Enter Grid Size: ")
# print("Grid size is " + grid_size + "* " +grid_size)
# start_location = input("Enter Start Location: ")
# print("Start location is :" + start_location)
# goal_location = input("Enter Goal Location: ")
# print("Goal location is : "+ goal_location)
