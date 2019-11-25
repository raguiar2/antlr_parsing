# Generated from Chat.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("j\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\6\23Y\n\23\r\23\16\23Z\3\24\6\24^\n\24\r\24\16\24")
        buf.write("_\3\25\5\25c\n\25\3\25\3\25\6\25g\n\25\r\25\16\25h\2\2")
        buf.write("\26\3\3\5\4\7\5\t\6\13\7\r\b\17\2\21\2\23\2\25\2\27\2")
        buf.write("\31\2\33\2\35\2\37\2!\t#\n%\13\'\f)\r\3\2\f\4\2CCcc\4")
        buf.write("\2UUuu\4\2[[{{\4\2JJjj\4\2QQqq\4\2WWww\4\2VVvv\3\2c|\3")
        buf.write("\2C\\\4\2\13\13\"\"\2g\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2\2")
        buf.write("\5-\3\2\2\2\7/\3\2\2\2\t\61\3\2\2\2\13\63\3\2\2\2\r\65")
        buf.write("\3\2\2\2\17\67\3\2\2\2\219\3\2\2\2\23;\3\2\2\2\25=\3\2")
        buf.write("\2\2\27?\3\2\2\2\31A\3\2\2\2\33C\3\2\2\2\35E\3\2\2\2\37")
        buf.write("G\3\2\2\2!I\3\2\2\2#N\3\2\2\2%X\3\2\2\2\']\3\2\2\2)f\3")
        buf.write("\2\2\2+,\7<\2\2,\4\3\2\2\2-.\7/\2\2.\6\3\2\2\2/\60\7+")
        buf.write("\2\2\60\b\3\2\2\2\61\62\7*\2\2\62\n\3\2\2\2\63\64\7\61")
        buf.write("\2\2\64\f\3\2\2\2\65\66\7B\2\2\66\16\3\2\2\2\678\t\2\2")
        buf.write("\28\20\3\2\2\29:\t\3\2\2:\22\3\2\2\2;<\t\4\2\2<\24\3\2")
        buf.write("\2\2=>\t\5\2\2>\26\3\2\2\2?@\t\6\2\2@\30\3\2\2\2AB\t\7")
        buf.write("\2\2B\32\3\2\2\2CD\t\b\2\2D\34\3\2\2\2EF\t\t\2\2F\36\3")
        buf.write("\2\2\2GH\t\n\2\2H \3\2\2\2IJ\5\21\t\2JK\5\17\b\2KL\5\23")
        buf.write("\n\2LM\5\21\t\2M\"\3\2\2\2NO\5\21\t\2OP\5\25\13\2PQ\5")
        buf.write("\27\f\2QR\5\31\r\2RS\5\33\16\2ST\5\21\t\2T$\3\2\2\2UY")
        buf.write("\5\35\17\2VY\5\37\20\2WY\7a\2\2XU\3\2\2\2XV\3\2\2\2XW")
        buf.write("\3\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[&\3\2\2\2\\^\t")
        buf.write("\13\2\2]\\\3\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`(\3\2")
        buf.write("\2\2ac\7\17\2\2ba\3\2\2\2bc\3\2\2\2cd\3\2\2\2dg\7\f\2")
        buf.write("\2eg\7\17\2\2fb\3\2\2\2fe\3\2\2\2gh\3\2\2\2hf\3\2\2\2")
        buf.write("hi\3\2\2\2i*\3\2\2\2\t\2XZ_bfh\2")
        return buf.getvalue()


class ChatLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    SAYS = 7
    SHOUTS = 8
    WORD = 9
    WHITESPACE = 10
    NEWLINE = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'-'", "')'", "'('", "'/'", "'@'" ]

    symbolicNames = [ "<INVALID>",
            "SAYS", "SHOUTS", "WORD", "WHITESPACE", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "A", "S", 
                  "Y", "H", "O", "U", "T", "LOWERCASE", "UPPERCASE", "SAYS", 
                  "SHOUTS", "WORD", "WHITESPACE", "NEWLINE" ]

    grammarFileName = "Chat.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


