class tree(object):

    def __init__(self):
        pass



class node(object):

    def __init__(self, content, terminal):
        self.content = content
        self.terminal = terminal


    def isTerminal(self):
        return self.terminal


    def setParentNode(self, parent):
        self.parent = parent


    def addSubNode(self, sub):
        if self.isTerminal() == false:
            if self.subNodes is None:
                self.subNodes = []
            self.subNodes.append(sub)
            return True
        else:
            return false
