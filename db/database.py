class User:
    usernameList = []
    passwordList = []
    phoneList = []
    addressList = []
    emailList = []

    def createUser(self, username, password, phone, address, email):
        self.usernameList.append(username)
        self.passwordList.append(password)
        self.phoneList.append(phone)
        self.addressList.append(address)
        self.emailList.append(email)

    def checkUserIsExist(self, username, password):
        if username in self.usernameList:
            index_username = self.usernameList.index(username)
            if self.passwordList[index_username] == password:
                return True
        return False


class Post:
    idList = []
    titleList = []
    descriptionList = []
    likeList = []
    authorList = []  # Foreign key User

    def createPost(self, id, title, description, like, author):
        self.idList.append(int(id))
        self.titleList.append(title)
        self.descriptionList.append(description)
        self.likeList.append(like)
        self.authorList.append(author)

    def getPostById(self, id):
        if id not in self.idList:
            return "Такой пост не существует %s " % id
        else:
            postIndexId = self.idList.index(id)
            title = self.titleList[postIndexId]
            description = self.descriptionList[postIndexId]
            like = self.likeList[postIndexId]
            return title, description, like

    autoIncrementForId = [0]

    def updatePostById(self, id, title, description, like):
        if id not in self.idList:
            postIndexId = self.idList.index(int(id))
            self.titleList[postIndexId] = title
            self.descriptionList[postIndexId] = description
            self.likeList[postIndexId] = like
        else:
            return "error %s " % id

    def getPostCountByAuthor(self, author):
        return self.authorList.count(author)

    def getPostFilterByAuthor(self, author):
        extractID = []
        extractDescript = []
        extractTitle = []
        extractLike = []
        if self.getPostCountByAuthor(author) > 0:
            count = 0
            for i in self.authorList:
                if i == author:
                    extractID.append(self.idList[count])
                    extractLike.append(self.likeList[count])
                    extractTitle.append(self.titleList[count])
                    extractDescript.append(self.descriptionList[count])

                count += 1
        return extractID, extractTitle, extractDescript, extractLike

    def deletePostById(self, id):
        postIndexId = self.idList.index(int(id))
        self.idList.remove(self.idList[postIndexId])
        self.likeList.remove(self.likeList[postIndexId])
        self.descriptionList.remove(self.descriptionList[postIndexId])
        self.titleList.remove(self.titleList[postIndexId])
        self.authorList.remove(self.authorList[postIndexId])

    def getCountPost(self):
        return len(self.titleList)

    def setAutoIncrementToPostId(self, id):
        id += 1
        self.autoIncrementForId[0] += id
        return sum(self.autoIncrementForId)

    def isPostExist(self, id):
        if int(id) not in self.idList:
            return True
        return False

    def checkUserIsOwnPost(self, username, id):
        authorPostId = []
        count = 0
        for i in self.authorList:
            if i == username:
                authorPostId.append(int(self.idList[count]))
            count += 1
        if int(id) in authorPostId:
            status = True
        else:
            status = False
        return status


class DataAccessLayer:
    def __init__(self):
        self.user = User()
        self.post = Post()

    def getTablePost(self):
        return self.post

    def getTableUser(self):
        return self.user
