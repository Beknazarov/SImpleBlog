class DataAccessLayer:
    users = {}
    posts = {}
    post_identity_id = [0]
    user_identity_id = [0]

    def create_user(self, username, password, email):
        user_attribute = [username, password, email]
        self.users[self.set_identity_user_id()] = user_attribute
        self.posts[username] = {}

    def create_post(self, username, title, description):
        self.posts[username][self.set_identity_post_id()] = [title, description]

    def set_identity_user_id(self):
        self.user_identity_id[0] += 1
        return sum(self.user_identity_id)

    def set_identity_post_id(self):
        self.post_identity_id[0] += 1
        return sum(self.post_identity_id)

    def print_users(self):
        return self.users

    def print_posts(self):
        return self.posts

    def is_user_exist(self, username, password):
        for user_attribute in self.users.values():
            name = user_attribute[0]
            pswd = user_attribute[1]
            if name == username and pswd == password:
                return True
        return False

    def is_post_exist(self, id):
        for posts in self.posts.values():
            for post_id in posts.keys():
                if post_id == id:
                    return True
        return False

    def check_the_author_of_the_posts(self, username, post_id):
        posts = self.posts[username]
        for id in posts.keys():
            if id == int(post_id):
                return True
        return False

    def get_post_by_id(self, id):
        for posts in self.posts.values():
            for post_id, item_post in posts.items():
                if post_id == int(id):
                    return item_post

    def get_to_only_their_posts(self, username):
        posts = self.posts[username]
        return posts

    def get_count_of_their_posts(self, username):
        posts = self.posts[username]
        return len(posts)

    def get_all_post(self):
        return self.posts

    def delete_post_by_id(self, id):
        for user_id, user_posts in self.posts.items():
            for post_id in user_posts.keys():
                if post_id == id:
                    self.posts[user_id].pop(post_id, None)
                    return

    def update_post(self, post_id, username, new_title, new_description):
        self.posts[username][post_id][0] = new_title
        self.posts[username][post_id][1] = new_description

    def count_post(self):
        count = 0
        for posts in self.posts.values():
            for post in posts.values():
                count += 1
        return count

db = DataAccessLayer()
db.create_user("nurs", "1", "nurs@mail.ru")
# db.create_user("Askar", "12345", "askar@mail.ru")
# db.create_post("Nursultan", "post2", "desc2")
# db.create_post("Askar", "post1", "desc1")
#
# db.create_post("Askar", "post3", "desc3")
# print(db.is_user_exist("Askar"))
# for key, value in db.posts.items():
#     for k, v in value.items():
#         print(key)
#         print(k)
#         print(v)
# print(db.posts)
