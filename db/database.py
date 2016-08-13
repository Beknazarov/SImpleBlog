class User:
    name = []
    password = []
    phone = []
    address = []
    email = []

    def CreateUser(self, name, password, phone, address, email):
        self.name.append(name)
        self.password.append(password)
        self.phone.append(phone)
        self.address.append(address)
        self.email.append(email)

    def CheckUserIsExist(self, username, password):
        if username in self.name:
            index_username = self.name.index(username)
            if self.password[index_username] == password:
                return True

        return False


class Blog:
    id = []
    title = []
    description = []
    like = []
    author = []

    # def __init__(self):
    #     self.id.append(1)
    #     self.title.append("Nursultan")
    #     self.description.append("Nursultan Nursultan Nursultan Nursultan Nursultan Nursultan Nursultan Nursultan")
    #     self.like.append(12)
    #     self.author.append("user")

    def CreatePost(self, id, title, description, like, author):
        self.id.append(int(id))
        self.title.append(title)
        self.description.append(description)
        self.like.append(like)
        self.author.append(author)

    def GetPostById(self, id):
        if not id in self.id:
            return "error %s " % id
        else:
            blog_index_id = self.id.index(id)
            title = self.title[blog_index_id]
            description = self.description[blog_index_id]
            like = self.like[blog_index_id]
            return title, description, like

    auto_increment = [0]


class DataAccessLayer:
    author2 = []
    like2 = []
    description2 = []
    title2 = []
    id2 = []

    def __init__(self):
        self.user = User()
        self.blog = Blog()
        self.id2 = []
        self.like2 = []
        self.title2 = []
        self.description2 = []

    def CreateUser(self, username, password, phone, address, email):
        self.user.CreateUser(username, password, phone, address, email)

    def GetUserAttribute(self):
        return self.user

    def CheckUserIsExist(self, username, password):
        return self.user.CheckUserIsExist(username, password)

    def CreatePost(self, id, title, description, like, author):
        self.blog.CreatePost(id, title, description, like, author)

    def GetPostById(self, id):
        return self.blog.GetPostById(id)

    def GetPostIndexById(self, id):
        if not id in self.blog.id:
            return "error %s " % id
        else:
            blog_index_id = self.blog.id.index(id)
            title = self.blog.title[blog_index_id]
            description = self.blog.description[blog_index_id]
            like = self.blog.like[blog_index_id]
            author = self.blog.author[blog_index_id]
            result = str(title) + "/" + str(description) + "/" + str(like) + "/" + str(author)
            return result

    def getTitlePost(self):
        return self.blog.title

    def getUserName(self):
        return self.user.name

    def getAllPost(self):
        return self.blog

    def EditPostById(self, id):
        if not id in self.blog.id:
            return "error %s " % id
        else:
            blog_index_id = self.blog.id.index(id)
            title = self.blog.title[blog_index_id]
            description = self.blog.description[blog_index_id]
            like = self.blog.like[blog_index_id]
            return title, description, like

    def updatePostById(self, id, title, description, like):

        if not id in self.blog.id:
            blog_index_id = self.blog.id.index(int(id))
            self.blog.title[blog_index_id] = title
            self.blog.description[blog_index_id] = description
            self.blog.like[blog_index_id] = like
        else:
            return "error %s " % id

    def getCountFilterAuthor(self, author):
        return self.blog.author.count(author)

    def GetPostFilterByUsername(self, author):
        if self.getCountFilterAuthor(author) <= 0:
            pass
        else:
            count = 0
            for i in self.blog.author:
                if i == author:
                    self.id2.append(self.blog.id[count])
                    self.like2.append(self.blog.like[count])
                    self.title2.append(self.blog.title[count])
                    self.description2.append(self.blog.description[count])

                count += 1
        return self.id2, self.title2, self.description2, self.like2

    def deletePostById(self, id):
        blog_index_id = self.blog.id.index(int(id))
        self.blog.id.remove(self.blog.id[blog_index_id])
        self.blog.like.remove(self.blog.like[blog_index_id])
        self.blog.description.remove(self.blog.description[blog_index_id])
        self.blog.title.remove(self.blog.title[blog_index_id])
        self.blog.author.remove(self.blog.author[blog_index_id])

    def count_post(self):
        return len(self.blog.id)

    def auto_increment(self, id):
        id += 1
        self.blog.auto_increment[0] += id
        return sum(self.blog.auto_increment)

    def CheckUserPost(self, username, id):
        user_post_id = []
        count = 0
        for i in self.blog.author:
            if i == username:
                user_post_id.append(int(self.blog.id[count]))
            count += 1
        if int(id) in user_post_id:
            status = True
        else:
            status = False
        if int(id) not in self.blog.id:
            status = False
        return status
