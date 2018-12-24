class testResult(object):

    def __init__(self, id, owner, title, status, pic, message, detail):
        self.id = id
        self.owner = owner
        self.title = title
        self.status = status
        self.pic = pic
        self.message = message
        self.detail = detail


class resultDetail(object):

    def __init__(self, step):
        self.step = step


class step(object):
    def __init__(self, status, action, message, pic_path):
        self.status = status
        self.action = action
        self.message = message
        self.pic_path = pic_path
