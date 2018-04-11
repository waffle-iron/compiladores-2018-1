from lexical.structure.token.TokenVal import Tokenval
class syntax_analyzer(object):

    def __init__(self):
        pass


    def isNumber(self, token):
        if token.tokenval == Tokenval.INTEGER_NUMBER or
        token.tokenval == Tokenval.FLOAT_NUMBER or
        token.tokenval == Tokenval.SCIENTIFIC_NOTATION:
            return True
        else:
            return False
