// Generated from /Users/xhn957/Desktop/sysml_v2/model2sim/grammar/CommonLexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class CommonLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ACTION=1, PART=2, IN=3, OUT=4, PERFORM=5, ATTRIBUTE=6, REDEFINES=7, FIRST=8, 
		THEN=9, DONE=10, COLON=11, SEMI=12, EQUAL=13, DOT=14, LBRACE=15, RBRACE=16, 
		LBRACK=17, RBRACK=18, ID=19, STRING=20, NUMBER=21, WS=22;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"ACTION", "PART", "IN", "OUT", "PERFORM", "ATTRIBUTE", "REDEFINES", "FIRST", 
			"THEN", "DONE", "COLON", "SEMI", "EQUAL", "DOT", "LBRACE", "RBRACE", 
			"LBRACK", "RBRACK", "ID", "STRING", "NUMBER", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'action'", "'part'", "'in'", "'out'", "'perform'", "'attribute'", 
			"':>>'", "'first'", "'then'", "'done'", "':'", "';'", "'='", "'.'", "'{'", 
			"'}'", "'['", "']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ACTION", "PART", "IN", "OUT", "PERFORM", "ATTRIBUTE", "REDEFINES", 
			"FIRST", "THEN", "DONE", "COLON", "SEMI", "EQUAL", "DOT", "LBRACE", "RBRACE", 
			"LBRACK", "RBRACK", "ID", "STRING", "NUMBER", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public CommonLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CommonLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0016\u009c\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0005"+
		"\u0012y\b\u0012\n\u0012\f\u0012|\t\u0012\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0005\u0013\u0082\b\u0013\n\u0013\f\u0013\u0085\t\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0004\u0014\u008a\b\u0014\u000b\u0014"+
		"\f\u0014\u008b\u0001\u0014\u0001\u0014\u0004\u0014\u0090\b\u0014\u000b"+
		"\u0014\f\u0014\u0091\u0003\u0014\u0094\b\u0014\u0001\u0015\u0004\u0015"+
		"\u0097\b\u0015\u000b\u0015\f\u0015\u0098\u0001\u0015\u0001\u0015\u0000"+
		"\u0000\u0016\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b"+
		"\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b"+
		"\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016"+
		"\u0001\u0000\u0005\u0003\u0000AZ__az\u0004\u000009AZ__az\u0002\u0000\""+
		"\"\\\\\u0001\u000009\u0003\u0000\t\n\r\r  \u00a2\u0000\u0001\u0001\u0000"+
		"\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000"+
		"\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000"+
		"\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000"+
		"\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000"+
		"\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000"+
		"\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000"+
		"\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000"+
		"\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000"+
		"#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001"+
		"\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000"+
		"\u0000\u0001-\u0001\u0000\u0000\u0000\u00034\u0001\u0000\u0000\u0000\u0005"+
		"9\u0001\u0000\u0000\u0000\u0007<\u0001\u0000\u0000\u0000\t@\u0001\u0000"+
		"\u0000\u0000\u000bH\u0001\u0000\u0000\u0000\rR\u0001\u0000\u0000\u0000"+
		"\u000fV\u0001\u0000\u0000\u0000\u0011\\\u0001\u0000\u0000\u0000\u0013"+
		"a\u0001\u0000\u0000\u0000\u0015f\u0001\u0000\u0000\u0000\u0017h\u0001"+
		"\u0000\u0000\u0000\u0019j\u0001\u0000\u0000\u0000\u001bl\u0001\u0000\u0000"+
		"\u0000\u001dn\u0001\u0000\u0000\u0000\u001fp\u0001\u0000\u0000\u0000!"+
		"r\u0001\u0000\u0000\u0000#t\u0001\u0000\u0000\u0000%v\u0001\u0000\u0000"+
		"\u0000\'}\u0001\u0000\u0000\u0000)\u0089\u0001\u0000\u0000\u0000+\u0096"+
		"\u0001\u0000\u0000\u0000-.\u0005a\u0000\u0000./\u0005c\u0000\u0000/0\u0005"+
		"t\u0000\u000001\u0005i\u0000\u000012\u0005o\u0000\u000023\u0005n\u0000"+
		"\u00003\u0002\u0001\u0000\u0000\u000045\u0005p\u0000\u000056\u0005a\u0000"+
		"\u000067\u0005r\u0000\u000078\u0005t\u0000\u00008\u0004\u0001\u0000\u0000"+
		"\u00009:\u0005i\u0000\u0000:;\u0005n\u0000\u0000;\u0006\u0001\u0000\u0000"+
		"\u0000<=\u0005o\u0000\u0000=>\u0005u\u0000\u0000>?\u0005t\u0000\u0000"+
		"?\b\u0001\u0000\u0000\u0000@A\u0005p\u0000\u0000AB\u0005e\u0000\u0000"+
		"BC\u0005r\u0000\u0000CD\u0005f\u0000\u0000DE\u0005o\u0000\u0000EF\u0005"+
		"r\u0000\u0000FG\u0005m\u0000\u0000G\n\u0001\u0000\u0000\u0000HI\u0005"+
		"a\u0000\u0000IJ\u0005t\u0000\u0000JK\u0005t\u0000\u0000KL\u0005r\u0000"+
		"\u0000LM\u0005i\u0000\u0000MN\u0005b\u0000\u0000NO\u0005u\u0000\u0000"+
		"OP\u0005t\u0000\u0000PQ\u0005e\u0000\u0000Q\f\u0001\u0000\u0000\u0000"+
		"RS\u0005:\u0000\u0000ST\u0005>\u0000\u0000TU\u0005>\u0000\u0000U\u000e"+
		"\u0001\u0000\u0000\u0000VW\u0005f\u0000\u0000WX\u0005i\u0000\u0000XY\u0005"+
		"r\u0000\u0000YZ\u0005s\u0000\u0000Z[\u0005t\u0000\u0000[\u0010\u0001\u0000"+
		"\u0000\u0000\\]\u0005t\u0000\u0000]^\u0005h\u0000\u0000^_\u0005e\u0000"+
		"\u0000_`\u0005n\u0000\u0000`\u0012\u0001\u0000\u0000\u0000ab\u0005d\u0000"+
		"\u0000bc\u0005o\u0000\u0000cd\u0005n\u0000\u0000de\u0005e\u0000\u0000"+
		"e\u0014\u0001\u0000\u0000\u0000fg\u0005:\u0000\u0000g\u0016\u0001\u0000"+
		"\u0000\u0000hi\u0005;\u0000\u0000i\u0018\u0001\u0000\u0000\u0000jk\u0005"+
		"=\u0000\u0000k\u001a\u0001\u0000\u0000\u0000lm\u0005.\u0000\u0000m\u001c"+
		"\u0001\u0000\u0000\u0000no\u0005{\u0000\u0000o\u001e\u0001\u0000\u0000"+
		"\u0000pq\u0005}\u0000\u0000q \u0001\u0000\u0000\u0000rs\u0005[\u0000\u0000"+
		"s\"\u0001\u0000\u0000\u0000tu\u0005]\u0000\u0000u$\u0001\u0000\u0000\u0000"+
		"vz\u0007\u0000\u0000\u0000wy\u0007\u0001\u0000\u0000xw\u0001\u0000\u0000"+
		"\u0000y|\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000\u0000z{\u0001\u0000"+
		"\u0000\u0000{&\u0001\u0000\u0000\u0000|z\u0001\u0000\u0000\u0000}\u0083"+
		"\u0005\"\u0000\u0000~\u0082\b\u0002\u0000\u0000\u007f\u0080\u0005\\\u0000"+
		"\u0000\u0080\u0082\t\u0000\u0000\u0000\u0081~\u0001\u0000\u0000\u0000"+
		"\u0081\u007f\u0001\u0000\u0000\u0000\u0082\u0085\u0001\u0000\u0000\u0000"+
		"\u0083\u0081\u0001\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000\u0000"+
		"\u0084\u0086\u0001\u0000\u0000\u0000\u0085\u0083\u0001\u0000\u0000\u0000"+
		"\u0086\u0087\u0005\"\u0000\u0000\u0087(\u0001\u0000\u0000\u0000\u0088"+
		"\u008a\u0007\u0003\u0000\u0000\u0089\u0088\u0001\u0000\u0000\u0000\u008a"+
		"\u008b\u0001\u0000\u0000\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008b"+
		"\u008c\u0001\u0000\u0000\u0000\u008c\u0093\u0001\u0000\u0000\u0000\u008d"+
		"\u008f\u0005.\u0000\u0000\u008e\u0090\u0007\u0003\u0000\u0000\u008f\u008e"+
		"\u0001\u0000\u0000\u0000\u0090\u0091\u0001\u0000\u0000\u0000\u0091\u008f"+
		"\u0001\u0000\u0000\u0000\u0091\u0092\u0001\u0000\u0000\u0000\u0092\u0094"+
		"\u0001\u0000\u0000\u0000\u0093\u008d\u0001\u0000\u0000\u0000\u0093\u0094"+
		"\u0001\u0000\u0000\u0000\u0094*\u0001\u0000\u0000\u0000\u0095\u0097\u0007"+
		"\u0004\u0000\u0000\u0096\u0095\u0001\u0000\u0000\u0000\u0097\u0098\u0001"+
		"\u0000\u0000\u0000\u0098\u0096\u0001\u0000\u0000\u0000\u0098\u0099\u0001"+
		"\u0000\u0000\u0000\u0099\u009a\u0001\u0000\u0000\u0000\u009a\u009b\u0006"+
		"\u0015\u0000\u0000\u009b,\u0001\u0000\u0000\u0000\b\u0000z\u0081\u0083"+
		"\u008b\u0091\u0093\u0098\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}