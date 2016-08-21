class DataAccessLayer:
    users = {}
    posts = {}
    post_increment_id = [0]
    user_increment_id = [0]

    def create_user(self, username, password, email):
        user_attribute = [username, password, email]
        self.users[self.set_increment_user_id()] = user_attribute
        self.posts[username] = {}

    def set_increment_user_id(self):
        self.user_increment_id[0] += 1
        return sum(self.user_increment_id)

    def create_post(self, username, title, description):
        self.posts[username][self.set_increment_post_id()] = [title, description]

    def set_increment_post_id(self):
        self.post_increment_id[0] += 1
        return sum(self.post_increment_id)

    def is_user_exist(self, username):
        for user_attribute in self.users.values():
            name = user_attribute[0]
            if name == username:
                return True
        return False

    def is_login_correct(self, username, password):
        for user_attribute in self.users.values():
            name = user_attribute[0]
            pswd = user_attribute[1]
            if name == username and password == pswd:
                return True
        return False

    def is_post_exist(self, id):
        for posts in self.posts.values():
            for post_id in posts.keys():
                if post_id == id:
                    return True
        return False

    def check_the_author_of_the_posts(self, username, post_id):
        try:
            posts = self.posts[username]
            for id in posts.keys():
                if id == int(post_id):
                    return True
        except KeyError:
            raise KeyError("User doesn't authenticated")
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
        index_title = 0
        index_description = 1
        self.posts[username][post_id][index_title] = new_title
        self.posts[username][post_id][index_description] = new_description

    def count_post(self):
        count = 0
        for posts in self.posts.values():
            for post in posts.values():
                count += 1
        return count

    def test_get_username_by_id(self, id):
        for user_id, user_item in self.users.items():
            if user_id == int(id):
                username = user_item[0]
                return username


db = DataAccessLayer()
db.create_user("nurs", "1", "nurs@mail.ru")
