from lexical.structure.token.TokenVal import TokenVal
class syntax_analyzer(object):

    def __init__(self):
        pass


    def isNumber(self, token):
        if token.tokenval == TokenVal.INTEGER_NUMBER.value or
        token.tokenval == TokenVal.FLOAT_NUMBER.value or
        token.tokenval == TokenVal.SCIENTIFIC_NOTATION.value:
            return True
        else:
            return False


    def isSumOperator(self, token):
        if token.tokenval == TokenVal.PLUS.value or token.tokenval == TokenVal.MINUS.value:
            return True
        else:
            return False


    def isMultiOperator(self, token):
        if token.tokenval == TokenVal.TIMES.value or token.tokenval == TokenVal.DIVISION.value:
            return True
        else:
            return False
