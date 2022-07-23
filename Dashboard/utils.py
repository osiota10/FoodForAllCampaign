import uuid
from .models import *


def generate_ref_code():
    code = str(uuid.uuid4()).replace("-", "")[:12]
    return code


def generate_payment_pin():
    pin = str(uuid.uuid4()).replace("-", "")[:5]
    return pin


def reverse(lst):
    lst.reverse()
    return lst


def get_downlines_slice(**kwargs):
    all_users = User.objects.all()
    qs = []
    for users in all_users:
        # if users.profile.status == 'Active':
        qs.append(users)
    current_user = User.objects.get(**kwargs)
    if current_user in qs:
        user_index = qs.index(current_user)
        user_index_increment = user_index + 1
        next_downlines_index = user_index_increment + 257  # plus 1 from increment
        index_slice = reverse(qs[user_index_increment:next_downlines_index])
        return index_slice
    else:
        return []


def get_last_item(downline, all_level_downline_list):
    new_qs = []
    for item in all_level_downline_list:
        if downline >= item:
            new_qs.append(item)
    last_item = new_qs[-1]
    return last_item


# Binary Tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # def insert(self, data):
    #     # Compare the new value with the parent node
    #     if self.data:
    #         if data < self.data:
    #             if self.left is None:
    #                 self.left = Node(data)
    #             else:
    #                 self.left.insert(data)
    #         elif data > self.data:
    #             if self.right is None:
    #                 self.right = Node(data)
    #             else:
    #                 self.right.insert(data)
    #     else:
    #         self.data = data

    # def insert(self, data):
    #     # Compare the new value with the parent node
    #     if self.data:
    #         if data == self.data:
    #             if self.left is None:
    #                 self.left = Node(data)
    #             else:
    #                 self.left.insert(data)
    #         elif data == self.data:
    #             if self.right is None:
    #                 self.right = Node(data)
    #             else:
    #                 self.right.insert(data)
    #     else:
    #         self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        # recs = Profile.objects.get
        all_users = User.objects.all()
        first_user = all_users.first()

        qs = []
        for users in all_users:
            qs.append(users.username)
        if data in qs:
            data = data
        current_user = User.objects.get(username=data)
        recommended_by = current_user.profile.recommended_by

        if self.data:
            if data == recommended_by and data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data == recommended_by and data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    def print_new(self, data, space=0, LEVEL_SPACE=5):
        if data is None: return
        space += LEVEL_SPACE
        self.print_new(data.right, space)
        # print() # neighbor space
        for i in range(LEVEL_SPACE, space): print(end=" ")
        print("|" + str(data.value) + "|<")
        self.print_new(data.left, space)


# all_users = User.objects.all()
# first_user = all_users.first()
#
# qs = []
# for users in all_users:
#     qs.append(users.username)



# root = Node(first_user)
# root.insert()
