import random
import time
from util import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0  # constant time
        self.users = {}  # constant time
        self.friendships = {}  # constant time

        for user in range(num_users):  # O(n^2)
            # this range produces [0, 1, 2]
            self.add_user(user)  # 1 -> 2 -> 3
            # add_user function auto increments last_id before adding the user
            # that means that our user list here is [1, 2, 3], but their names are [0, 1, 2]... not intuitive >_<'

        friendships = []
        for user in range(1, self.last_id + 1):  # 1->2->3 O(n^2)
            for friend in range(user + 1, num_users):  # 2->3
                friendships.append((user, friend))

        for idx in range(len(friendships)):
            rand_idx = random.randint(0, len(friendships) - 1)
            # swap these items
            friendships[idx], friendships[rand_idx] = friendships[rand_idx], friendships[idx]

        total_friendships = num_users * avg_friendships
        pairs_needed = total_friendships // 2
        random_friendships = friendships[:pairs_needed]

        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def populate_graph_linearly(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for user_id in range(num_users):
            self.add_user(user_id)

        total_friendships = num_users * avg_friendships

        friendships_made = 0

        failures = 0

        while friendships_made < total_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if user_id != friend_id and friend_id not in self.friendships[user_id]:
                self.add_friendship(user_id, friend_id)
                friendships_made += 1
            else:
                failures += 1

        print(failures)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        Q = Queue()
        path = [user_id]
        Q.enqueue(path)

        while Q.size() > 0:
            current_path = Q.dequeue()
            current_user = current_path[-1]

            if current_user not in visited:
                visited[current_user] = current_path
                friends = self.friendships[current_user]

                for friend in friends:
                    path_copy = current_path[:]
                    path_copy.append(friend)
                    Q.enqueue(path_copy)

        return visited

        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    total_paths = 0
    for friend_id in connections:
        friend_path = connections[friend_id]
        total_paths += len(friend_path)

    average_path_length = total_paths / len(connections)

    print(f"Average path length: {average_path_length}")

    num_users = 100
    avg_friendships = 5

    start_time = time.time()
    sg.populate_graph(num_users, avg_friendships)
    end_time = time.time()

    print(f"Quadratic run time: {end_time - start_time}")

    start_time = time.time()
    sg.populate_graph_linearly(num_users, avg_friendships)
    end_time = time.time()

    print(f"Linear run time: {end_time - start_time}")
