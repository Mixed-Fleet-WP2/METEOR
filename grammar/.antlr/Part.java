// Generated from /Users/xhn957/Desktop/sysml_v2/model2sim/grammar/Part.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class Part extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ACTION=1, PART=2, IN=3, OUT=4, PERFORM=5, ATTRIBUTE=6, REDEFINES=7, FIRST=8, 
		THEN=9, DONE=10, COLON=11, SEMI=12, EQUAL=13, DOT=14, LBRACE=15, RBRACE=16, 
		LBRACK=17, RBRACK=18, ID=19, STRING=20, NUMBER=21, WS=22;
	public static final int
		RULE_part = 0, RULE_partBody = 1, RULE_expr = 2, RULE_unit = 3;
	private static String[] makeRuleNames() {
		return new String[] {
			"part", "partBody", "expr", "unit"
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

	@Override
	public String getGrammarFileName() { return "Part.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public Part(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PartContext extends ParserRuleContext {
		public TerminalNode PART() { return getToken(Part.PART, 0); }
		public List<TerminalNode> ID() { return getTokens(Part.ID); }
		public TerminalNode ID(int i) {
			return getToken(Part.ID, i);
		}
		public TerminalNode COLON() { return getToken(Part.COLON, 0); }
		public TerminalNode LBRACE() { return getToken(Part.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(Part.RBRACE, 0); }
		public List<PartBodyContext> partBody() {
			return getRuleContexts(PartBodyContext.class);
		}
		public PartBodyContext partBody(int i) {
			return getRuleContext(PartBodyContext.class,i);
		}
		public PartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_part; }
	}

	public final PartContext part() throws RecognitionException {
		PartContext _localctx = new PartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(8);
			match(PART);
			setState(9);
			match(ID);
			setState(10);
			match(COLON);
			setState(11);
			match(ID);
			setState(12);
			match(LBRACE);
			setState(16);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PERFORM || _la==ATTRIBUTE) {
				{
				{
				setState(13);
				partBody();
				}
				}
				setState(18);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(19);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PartBodyContext extends ParserRuleContext {
		public TerminalNode ATTRIBUTE() { return getToken(Part.ATTRIBUTE, 0); }
		public TerminalNode REDEFINES() { return getToken(Part.REDEFINES, 0); }
		public TerminalNode ID() { return getToken(Part.ID, 0); }
		public TerminalNode EQUAL() { return getToken(Part.EQUAL, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(Part.SEMI, 0); }
		public UnitContext unit() {
			return getRuleContext(UnitContext.class,0);
		}
		public TerminalNode PERFORM() { return getToken(Part.PERFORM, 0); }
		public PartBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_partBody; }
	}

	public final PartBodyContext partBody() throws RecognitionException {
		PartBodyContext _localctx = new PartBodyContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_partBody);
		int _la;
		try {
			setState(34);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ATTRIBUTE:
				enterOuterAlt(_localctx, 1);
				{
				setState(21);
				match(ATTRIBUTE);
				setState(22);
				match(REDEFINES);
				setState(23);
				match(ID);
				setState(24);
				match(EQUAL);
				setState(25);
				expr();
				setState(27);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LBRACK) {
					{
					setState(26);
					unit();
					}
				}

				setState(29);
				match(SEMI);
				}
				break;
			case PERFORM:
				enterOuterAlt(_localctx, 2);
				{
				setState(31);
				match(PERFORM);
				setState(32);
				match(ID);
				setState(33);
				match(SEMI);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(Part.ID, 0); }
		public TerminalNode STRING() { return getToken(Part.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(Part.NUMBER, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3670016L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnitContext extends ParserRuleContext {
		public TerminalNode LBRACK() { return getToken(Part.LBRACK, 0); }
		public TerminalNode ID() { return getToken(Part.ID, 0); }
		public TerminalNode RBRACK() { return getToken(Part.RBRACK, 0); }
		public UnitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unit; }
	}

	public final UnitContext unit() throws RecognitionException {
		UnitContext _localctx = new UnitContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_unit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(LBRACK);
			setState(39);
			match(ID);
			setState(40);
			match(RBRACK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0016+\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000\u000f\b\u0000\n"+
		"\u0000\f\u0000\u0012\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u001c"+
		"\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003"+
		"\u0001#\b\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0000\u0000\u0004\u0000\u0002\u0004\u0006"+
		"\u0000\u0001\u0001\u0000\u0013\u0015)\u0000\b\u0001\u0000\u0000\u0000"+
		"\u0002\"\u0001\u0000\u0000\u0000\u0004$\u0001\u0000\u0000\u0000\u0006"+
		"&\u0001\u0000\u0000\u0000\b\t\u0005\u0002\u0000\u0000\t\n\u0005\u0013"+
		"\u0000\u0000\n\u000b\u0005\u000b\u0000\u0000\u000b\f\u0005\u0013\u0000"+
		"\u0000\f\u0010\u0005\u000f\u0000\u0000\r\u000f\u0003\u0002\u0001\u0000"+
		"\u000e\r\u0001\u0000\u0000\u0000\u000f\u0012\u0001\u0000\u0000\u0000\u0010"+
		"\u000e\u0001\u0000\u0000\u0000\u0010\u0011\u0001\u0000\u0000\u0000\u0011"+
		"\u0013\u0001\u0000\u0000\u0000\u0012\u0010\u0001\u0000\u0000\u0000\u0013"+
		"\u0014\u0005\u0010\u0000\u0000\u0014\u0001\u0001\u0000\u0000\u0000\u0015"+
		"\u0016\u0005\u0006\u0000\u0000\u0016\u0017\u0005\u0007\u0000\u0000\u0017"+
		"\u0018\u0005\u0013\u0000\u0000\u0018\u0019\u0005\r\u0000\u0000\u0019\u001b"+
		"\u0003\u0004\u0002\u0000\u001a\u001c\u0003\u0006\u0003\u0000\u001b\u001a"+
		"\u0001\u0000\u0000\u0000\u001b\u001c\u0001\u0000\u0000\u0000\u001c\u001d"+
		"\u0001\u0000\u0000\u0000\u001d\u001e\u0005\f\u0000\u0000\u001e#\u0001"+
		"\u0000\u0000\u0000\u001f \u0005\u0005\u0000\u0000 !\u0005\u0013\u0000"+
		"\u0000!#\u0005\f\u0000\u0000\"\u0015\u0001\u0000\u0000\u0000\"\u001f\u0001"+
		"\u0000\u0000\u0000#\u0003\u0001\u0000\u0000\u0000$%\u0007\u0000\u0000"+
		"\u0000%\u0005\u0001\u0000\u0000\u0000&\'\u0005\u0011\u0000\u0000\'(\u0005"+
		"\u0013\u0000\u0000()\u0005\u0012\u0000\u0000)\u0007\u0001\u0000\u0000"+
		"\u0000\u0003\u0010\u001b\"";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}