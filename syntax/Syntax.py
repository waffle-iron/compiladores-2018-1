from lexical.structure.token.TokenVal import TokenVal
class syntax_analyzer(object):

    def __init__(self):
        pass


    def isNumber(self, tokenlist):
        token = tokenlist[0]
        if token.tokenval == TokenVal.INTEGER_NUMBER.value or
        token.tokenval == TokenVal.FLOAT_NUMBER.value or
        token.tokenval == TokenVal.SCIENTIFIC_NOTATION.value:
            return True
        else:
            return False


    def isSumOperator(self, tokenlist):
        token = tokenlist[0]
        if token.tokenval == TokenVal.PLUS.value or token.tokenval == TokenVal.MINUS.value:
            return True
        else:
            return False


    def isMultiOperator(self, tokenlist):
        token = tokenlist[0]
        if token.tokenval == TokenVal.TIMES.value or token.tokenval == TokenVal.DIVISION.value:
            return True
        else:
            return False


    def isRelationalOperator(self, tokenlist):
        token = tokenlist[0]
        if token.tokenval == TokenVal.LOGIC_EQUALS.value or token.tokenval == TokenVal.HIGHER.value or
        token.tokenval == TokenVal.LESS.value or token.tokenval == TokenVal.LESS_EQUALS.value or
        token.tokenval == TokenVal.HIGHER_EQUALS.value:
            return True
        else:
            return False


    def isType(self, tokenlist):
        token = tokenlist[0]
        if  token.tokenval == TokenVal.FLOAT_TYPE.value or
        token.tokenval == TokenVal.INTEGER_TYPE.value:
            return True
        else:
            return False


    def isUnaryExpression(self, tokenlist):
        if self.isFactor(tokenlist):
            return True
        elif self.isSumOperator(tokenlist) and self.isFactor(tokenlist[1:]):
            return True
        else:
            return False

            
    def isFactor(self, tokenlist):

        if tokenlist[0].tokenval == TokenVal.OPEN_PARENTHESES.value and
        self.isExpression(tokenlist[1:]) and tokenlist[2].tokenval == TokenVal.CLOSE_PARENTHESES.value:
            return True
        elif self.isVar(tokenlist):
            return True
        elif self.isCallFunction(tokenlist):
            returnt True
        elif self.isNumber(tokenlist):
            return True
        else:
            return False


    def isExpression(self, tokenlist):
        pass


    def isVar(self, tokenlist):
        pass


    def isCallFunction(self, tokenlist):
        pass
