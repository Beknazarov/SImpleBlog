class DataAccessLayer:
    users = {}
    posts = {}
    postIdentityId = [0]
    userIdentityId = [0]

    def createUser(self, username, password, email):
        user_attribute = [username, password, email]
        self.users[self.setUserIdentityId()] = user_attribute
        self.posts[username] = {}

    def createPost(self, username, title, description):
        self.posts[username][self.setPostIdentityId()] = [title, description]

    def setUserIdentityId(self):
        self.userIdentityId[0] += 1
        return sum(self.userIdentityId)

    def setPostIdentityId(self):
        self.postIdentityId[0] += 1
        return sum(self.postIdentityId)

    def printUser(self):
        return self.users

    def isUserExist(self, username):
        for userId, userAttribute in self.users.items():
            name = userAttribute[0]
            if name == username:
                return True
        return False

    def isPostExist(self, post_id):
        for userId, userPost in self.posts.items():
            for postId, postItem in userPost.items():
                if postId == post_id:
                    return True
        return False

    def isPostInUser(self, username, id):
        post = self.posts[username]
        for post_id in post.keys():
            if post_id == int(id):
                return True
        return False

    def printPost(self):
        return self.posts

    def getPostById(self, post_id):
        for userId, userPost in self.posts.items():
            for postId, postItem in userPost.items():
                if postId == post_id:
                    return postItem

    def getAllPostOwnUser(self, username):
        post = self.posts[username]
        return post

    def getCountPostOwnUser(self, username):
        post = self.posts[username]
        return len(post)

    def getAllPost(self):
        return self.posts

    def deletePostById(self, post_id):
        for userId, userPost in self.posts.items():
            for postId, postItem in userPost.items():
                if postId == post_id:
                    self.posts[userId].pop(postId, None)
                    return

    def updatePost(self, post_id, username, new_title, new_description):
        self.posts[username][post_id][0] = new_title
        self.posts[username][post_id][1] = new_description

    def countPost(self):
        count = 0
        for userId, userPost in self.posts.items():
            for post in userPost.values():
                count += 1
        return count

# db = DataAccessLayer()
# db.createUser("Nursultan", "12345", "nurs@mail.ru")
# db.createUser("Askar", "12345", "askar@mail.ru")
# db.createPost("Nursultan", "post2", "desc2")
# db.createPost("Askar", "post1", "desc1")
#
# db.createPost("Askar", "post3", "desc3")
# print(db.isUserExist("Askar"))
# for key, value in db.posts.items():
#     for k, v in value.items():
#         print(key)
#         print(k)
#         print(v)
# print(db.posts)

