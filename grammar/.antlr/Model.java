// Generated from /Users/xhn957/Desktop/projects/model2sim/grammar/Model.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class Model extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ACTION=1, PART=2, IN=3, OUT=4, PERFORM=5, ATTRIBUTE=6, REDEFINES=7, FIRST=8, 
		THEN=9, DONE=10, COLON=11, SEMI=12, EQUAL=13, DOT=14, LBRACE=15, RBRACE=16, 
		LBRACK=17, RBRACK=18, ID=19, STRING=20, NUMBER=21, WS=22, PACKAGE=23, 
		PRIVATE=24, IMPORT=25, COLONCOLON=26, STAR=27;
	public static final int
		RULE_model = 0, RULE_packageDecl = 1, RULE_importDecl = 2, RULE_qualifiedName = 3, 
		RULE_action = 4, RULE_param = 5, RULE_attribute = 6, RULE_attributeInit = 7, 
		RULE_flowStatement = 8, RULE_firstStep = 9, RULE_thenStep = 10, RULE_expr = 11, 
		RULE_part = 12, RULE_partBody = 13, RULE_unit = 14;
	private static String[] makeRuleNames() {
		return new String[] {
			"model", "packageDecl", "importDecl", "qualifiedName", "action", "param", 
			"attribute", "attributeInit", "flowStatement", "firstStep", "thenStep", 
			"expr", "part", "partBody", "unit"
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
			"LBRACK", "RBRACK", "ID", "STRING", "NUMBER", "WS", "PACKAGE", "PRIVATE", 
			"IMPORT", "COLONCOLON", "STAR"
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
	public String getGrammarFileName() { return "Model.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public Model(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ModelContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(Model.EOF, 0); }
		public PackageDeclContext packageDecl() {
			return getRuleContext(PackageDeclContext.class,0);
		}
		public List<ImportDeclContext> importDecl() {
			return getRuleContexts(ImportDeclContext.class);
		}
		public ImportDeclContext importDecl(int i) {
			return getRuleContext(ImportDeclContext.class,i);
		}
		public List<ActionContext> action() {
			return getRuleContexts(ActionContext.class);
		}
		public ActionContext action(int i) {
			return getRuleContext(ActionContext.class,i);
		}
		public List<PartContext> part() {
			return getRuleContexts(PartContext.class);
		}
		public PartContext part(int i) {
			return getRuleContext(PartContext.class,i);
		}
		public ModelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_model; }
	}

	public final ModelContext model() throws RecognitionException {
		ModelContext _localctx = new ModelContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_model);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PACKAGE) {
				{
				setState(30);
				packageDecl();
				}
			}

			setState(36);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PRIVATE || _la==IMPORT) {
				{
				{
				setState(33);
				importDecl();
				}
				}
				setState(38);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(43);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ACTION || _la==PART) {
				{
				setState(41);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ACTION:
					{
					setState(39);
					action();
					}
					break;
				case PART:
					{
					setState(40);
					part();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(45);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(46);
			match(EOF);
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
	public static class PackageDeclContext extends ParserRuleContext {
		public TerminalNode PACKAGE() { return getToken(Model.PACKAGE, 0); }
		public QualifiedNameContext qualifiedName() {
			return getRuleContext(QualifiedNameContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(Model.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(Model.RBRACE, 0); }
		public List<ImportDeclContext> importDecl() {
			return getRuleContexts(ImportDeclContext.class);
		}
		public ImportDeclContext importDecl(int i) {
			return getRuleContext(ImportDeclContext.class,i);
		}
		public List<ActionContext> action() {
			return getRuleContexts(ActionContext.class);
		}
		public ActionContext action(int i) {
			return getRuleContext(ActionContext.class,i);
		}
		public List<PartContext> part() {
			return getRuleContexts(PartContext.class);
		}
		public PartContext part(int i) {
			return getRuleContext(PartContext.class,i);
		}
		public PackageDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_packageDecl; }
	}

	public final PackageDeclContext packageDecl() throws RecognitionException {
		PackageDeclContext _localctx = new PackageDeclContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_packageDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			match(PACKAGE);
			setState(49);
			qualifiedName();
			setState(50);
			match(LBRACE);
			setState(56);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 50331654L) != 0)) {
				{
				setState(54);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PRIVATE:
				case IMPORT:
					{
					setState(51);
					importDecl();
					}
					break;
				case ACTION:
					{
					setState(52);
					action();
					}
					break;
				case PART:
					{
					setState(53);
					part();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(58);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(59);
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
	public static class ImportDeclContext extends ParserRuleContext {
		public TerminalNode IMPORT() { return getToken(Model.IMPORT, 0); }
		public QualifiedNameContext qualifiedName() {
			return getRuleContext(QualifiedNameContext.class,0);
		}
		public TerminalNode COLONCOLON() { return getToken(Model.COLONCOLON, 0); }
		public TerminalNode STAR() { return getToken(Model.STAR, 0); }
		public TerminalNode SEMI() { return getToken(Model.SEMI, 0); }
		public TerminalNode PRIVATE() { return getToken(Model.PRIVATE, 0); }
		public ImportDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_importDecl; }
	}

	public final ImportDeclContext importDecl() throws RecognitionException {
		ImportDeclContext _localctx = new ImportDeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_importDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PRIVATE) {
				{
				setState(61);
				match(PRIVATE);
				}
			}

			setState(64);
			match(IMPORT);
			setState(65);
			qualifiedName();
			setState(66);
			match(COLONCOLON);
			setState(67);
			match(STAR);
			setState(68);
			match(SEMI);
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
	public static class QualifiedNameContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(Model.ID); }
		public TerminalNode ID(int i) {
			return getToken(Model.ID, i);
		}
		public List<TerminalNode> COLONCOLON() { return getTokens(Model.COLONCOLON); }
		public TerminalNode COLONCOLON(int i) {
			return getToken(Model.COLONCOLON, i);
		}
		public QualifiedNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_qualifiedName; }
	}

	public final QualifiedNameContext qualifiedName() throws RecognitionException {
		QualifiedNameContext _localctx = new QualifiedNameContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_qualifiedName);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(ID);
			setState(75);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(71);
					match(COLONCOLON);
					setState(72);
					match(ID);
					}
					} 
				}
				setState(77);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
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
	public static class ActionContext extends ParserRuleContext {
		public TerminalNode ACTION() { return getToken(Model.ACTION, 0); }
		public List<TerminalNode> ID() { return getTokens(Model.ID); }
		public TerminalNode ID(int i) {
			return getToken(Model.ID, i);
		}
		public TerminalNode LBRACE() { return getToken(Model.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(Model.RBRACE, 0); }
		public TerminalNode COLON() { return getToken(Model.COLON, 0); }
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public List<PartContext> part() {
			return getRuleContexts(PartContext.class);
		}
		public PartContext part(int i) {
			return getRuleContext(PartContext.class,i);
		}
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<FlowStatementContext> flowStatement() {
			return getRuleContexts(FlowStatementContext.class);
		}
		public FlowStatementContext flowStatement(int i) {
			return getRuleContext(FlowStatementContext.class,i);
		}
		public List<ActionContext> action() {
			return getRuleContexts(ActionContext.class);
		}
		public ActionContext action(int i) {
			return getRuleContext(ActionContext.class,i);
		}
		public ActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_action; }
	}

	public final ActionContext action() throws RecognitionException {
		ActionContext _localctx = new ActionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_action);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(ACTION);
			setState(79);
			match(ID);
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COLON) {
				{
				setState(80);
				match(COLON);
				setState(81);
				match(ID);
				}
			}

			setState(84);
			match(LBRACE);
			setState(92);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 862L) != 0)) {
				{
				setState(90);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ATTRIBUTE:
					{
					setState(85);
					attribute();
					}
					break;
				case PART:
					{
					setState(86);
					part();
					}
					break;
				case IN:
				case OUT:
					{
					setState(87);
					param();
					}
					break;
				case FIRST:
				case THEN:
					{
					setState(88);
					flowStatement();
					}
					break;
				case ACTION:
					{
					setState(89);
					action();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(94);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(95);
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
	public static class ParamContext extends ParserRuleContext {
		public TerminalNode IN() { return getToken(Model.IN, 0); }
		public TerminalNode ID() { return getToken(Model.ID, 0); }
		public TerminalNode EQUAL() { return getToken(Model.EQUAL, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(Model.SEMI, 0); }
		public TerminalNode REDEFINES() { return getToken(Model.REDEFINES, 0); }
		public TerminalNode OUT() { return getToken(Model.OUT, 0); }
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_param);
		int _la;
		try {
			setState(109);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IN:
				enterOuterAlt(_localctx, 1);
				{
				setState(97);
				match(IN);
				setState(99);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==REDEFINES) {
					{
					setState(98);
					match(REDEFINES);
					}
				}

				setState(101);
				match(ID);
				setState(102);
				match(EQUAL);
				setState(103);
				expr();
				setState(104);
				match(SEMI);
				}
				break;
			case OUT:
				enterOuterAlt(_localctx, 2);
				{
				setState(106);
				match(OUT);
				setState(107);
				match(ID);
				setState(108);
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
	public static class AttributeContext extends ParserRuleContext {
		public TerminalNode ATTRIBUTE() { return getToken(Model.ATTRIBUTE, 0); }
		public List<TerminalNode> ID() { return getTokens(Model.ID); }
		public TerminalNode ID(int i) {
			return getToken(Model.ID, i);
		}
		public TerminalNode COLON() { return getToken(Model.COLON, 0); }
		public TerminalNode SEMI() { return getToken(Model.SEMI, 0); }
		public TerminalNode LBRACE() { return getToken(Model.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(Model.RBRACE, 0); }
		public List<AttributeInitContext> attributeInit() {
			return getRuleContexts(AttributeInitContext.class);
		}
		public AttributeInitContext attributeInit(int i) {
			return getRuleContext(AttributeInitContext.class,i);
		}
		public AttributeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute; }
	}

	public final AttributeContext attribute() throws RecognitionException {
		AttributeContext _localctx = new AttributeContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_attribute);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(ATTRIBUTE);
			setState(112);
			match(ID);
			setState(113);
			match(COLON);
			setState(114);
			match(ID);
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LBRACE) {
				{
				setState(115);
				match(LBRACE);
				setState(119);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==REDEFINES) {
					{
					{
					setState(116);
					attributeInit();
					}
					}
					setState(121);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(122);
				match(RBRACE);
				}
			}

			setState(125);
			match(SEMI);
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
	public static class AttributeInitContext extends ParserRuleContext {
		public TerminalNode REDEFINES() { return getToken(Model.REDEFINES, 0); }
		public TerminalNode ID() { return getToken(Model.ID, 0); }
		public TerminalNode EQUAL() { return getToken(Model.EQUAL, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(Model.SEMI, 0); }
		public AttributeInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attributeInit; }
	}

	public final AttributeInitContext attributeInit() throws RecognitionException {
		AttributeInitContext _localctx = new AttributeInitContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_attributeInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			match(REDEFINES);
			setState(128);
			match(ID);
			setState(129);
			match(EQUAL);
			setState(130);
			expr();
			setState(131);
			match(SEMI);
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
	public static class FlowStatementContext extends ParserRuleContext {
		public FirstStepContext firstStep() {
			return getRuleContext(FirstStepContext.class,0);
		}
		public ThenStepContext thenStep() {
			return getRuleContext(ThenStepContext.class,0);
		}
		public FlowStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_flowStatement; }
	}

	public final FlowStatementContext flowStatement() throws RecognitionException {
		FlowStatementContext _localctx = new FlowStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_flowStatement);
		try {
			setState(135);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FIRST:
				enterOuterAlt(_localctx, 1);
				{
				setState(133);
				firstStep();
				}
				break;
			case THEN:
				enterOuterAlt(_localctx, 2);
				{
				setState(134);
				thenStep();
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
	public static class FirstStepContext extends ParserRuleContext {
		public TerminalNode FIRST() { return getToken(Model.FIRST, 0); }
		public TerminalNode ID() { return getToken(Model.ID, 0); }
		public TerminalNode SEMI() { return getToken(Model.SEMI, 0); }
		public FirstStepContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_firstStep; }
	}

	public final FirstStepContext firstStep() throws RecognitionException {
		FirstStepContext _localctx = new FirstStepContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_firstStep);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(FIRST);
			setState(138);
			match(ID);
			setState(139);
			match(SEMI);
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
	public static class ThenStepContext extends ParserRuleContext {
		public TerminalNode THEN() { return getToken(Model.THEN, 0); }
		public TerminalNode DONE() { return getToken(Model.DONE, 0); }
		public TerminalNode SEMI() { return getToken(Model.SEMI, 0); }
		public TerminalNode PERFORM() { return getToken(Model.PERFORM, 0); }
		public TerminalNode ID() { return getToken(Model.ID, 0); }
		public ThenStepContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_thenStep; }
	}

	public final ThenStepContext thenStep() throws RecognitionException {
		ThenStepContext _localctx = new ThenStepContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_thenStep);
		try {
			setState(148);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(141);
				match(THEN);
				setState(142);
				match(DONE);
				setState(143);
				match(SEMI);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(144);
				match(THEN);
				setState(145);
				match(PERFORM);
				setState(146);
				match(ID);
				setState(147);
				match(SEMI);
				}
				break;
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
		public List<TerminalNode> ID() { return getTokens(Model.ID); }
		public TerminalNode ID(int i) {
			return getToken(Model.ID, i);
		}
		public TerminalNode DOT() { return getToken(Model.DOT, 0); }
		public TerminalNode STRING() { return getToken(Model.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(Model.NUMBER, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_expr);
		try {
			setState(156);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(150);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(151);
				match(ID);
				setState(152);
				match(DOT);
				setState(153);
				match(ID);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(154);
				match(STRING);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(155);
				match(NUMBER);
				}
				break;
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
	public static class PartContext extends ParserRuleContext {
		public TerminalNode PART() { return getToken(Model.PART, 0); }
		public List<TerminalNode> ID() { return getTokens(Model.ID); }
		public TerminalNode ID(int i) {
			return getToken(Model.ID, i);
		}
		public TerminalNode COLON() { return getToken(Model.COLON, 0); }
		public TerminalNode LBRACE() { return getToken(Model.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(Model.RBRACE, 0); }
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
		enterRule(_localctx, 24, RULE_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			match(PART);
			setState(159);
			match(ID);
			setState(160);
			match(COLON);
			setState(161);
			match(ID);
			setState(162);
			match(LBRACE);
			setState(166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PERFORM || _la==ATTRIBUTE) {
				{
				{
				setState(163);
				partBody();
				}
				}
				setState(168);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(169);
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
		public TerminalNode ATTRIBUTE() { return getToken(Model.ATTRIBUTE, 0); }
		public TerminalNode REDEFINES() { return getToken(Model.REDEFINES, 0); }
		public TerminalNode ID() { return getToken(Model.ID, 0); }
		public TerminalNode EQUAL() { return getToken(Model.EQUAL, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(Model.SEMI, 0); }
		public UnitContext unit() {
			return getRuleContext(UnitContext.class,0);
		}
		public TerminalNode PERFORM() { return getToken(Model.PERFORM, 0); }
		public PartBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_partBody; }
	}

	public final PartBodyContext partBody() throws RecognitionException {
		PartBodyContext _localctx = new PartBodyContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_partBody);
		int _la;
		try {
			setState(184);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ATTRIBUTE:
				enterOuterAlt(_localctx, 1);
				{
				setState(171);
				match(ATTRIBUTE);
				setState(172);
				match(REDEFINES);
				setState(173);
				match(ID);
				setState(174);
				match(EQUAL);
				setState(175);
				expr();
				setState(177);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LBRACK) {
					{
					setState(176);
					unit();
					}
				}

				setState(179);
				match(SEMI);
				}
				break;
			case PERFORM:
				enterOuterAlt(_localctx, 2);
				{
				setState(181);
				match(PERFORM);
				setState(182);
				match(ID);
				setState(183);
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
	public static class UnitContext extends ParserRuleContext {
		public TerminalNode LBRACK() { return getToken(Model.LBRACK, 0); }
		public TerminalNode ID() { return getToken(Model.ID, 0); }
		public TerminalNode RBRACK() { return getToken(Model.RBRACK, 0); }
		public UnitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unit; }
	}

	public final UnitContext unit() throws RecognitionException {
		UnitContext _localctx = new UnitContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_unit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			match(LBRACK);
			setState(187);
			match(ID);
			setState(188);
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
		"\u0004\u0001\u001b\u00bf\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0001\u0000\u0003"+
		"\u0000 \b\u0000\u0001\u0000\u0005\u0000#\b\u0000\n\u0000\f\u0000&\t\u0000"+
		"\u0001\u0000\u0001\u0000\u0005\u0000*\b\u0000\n\u0000\f\u0000-\t\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0005\u00017\b\u0001\n\u0001\f\u0001:\t\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0003\u0002?\b\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0005\u0003J\b\u0003\n\u0003\f\u0003M\t\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004S\b\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0005\u0004[\b\u0004\n\u0004\f\u0004^\t\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0003\u0005d\b\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0003\u0005n\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0005\u0006v\b\u0006\n\u0006\f\u0006y\t\u0006"+
		"\u0001\u0006\u0003\u0006|\b\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0003\b\u0088\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u0095\b\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u009d"+
		"\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0005\f\u00a5"+
		"\b\f\n\f\f\f\u00a8\t\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r"+
		"\u0001\r\u0001\r\u0003\r\u00b2\b\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0003\r\u00b9\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0000\u0000\u000f\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012"+
		"\u0014\u0016\u0018\u001a\u001c\u0000\u0000\u00ca\u0000\u001f\u0001\u0000"+
		"\u0000\u0000\u00020\u0001\u0000\u0000\u0000\u0004>\u0001\u0000\u0000\u0000"+
		"\u0006F\u0001\u0000\u0000\u0000\bN\u0001\u0000\u0000\u0000\nm\u0001\u0000"+
		"\u0000\u0000\fo\u0001\u0000\u0000\u0000\u000e\u007f\u0001\u0000\u0000"+
		"\u0000\u0010\u0087\u0001\u0000\u0000\u0000\u0012\u0089\u0001\u0000\u0000"+
		"\u0000\u0014\u0094\u0001\u0000\u0000\u0000\u0016\u009c\u0001\u0000\u0000"+
		"\u0000\u0018\u009e\u0001\u0000\u0000\u0000\u001a\u00b8\u0001\u0000\u0000"+
		"\u0000\u001c\u00ba\u0001\u0000\u0000\u0000\u001e \u0003\u0002\u0001\u0000"+
		"\u001f\u001e\u0001\u0000\u0000\u0000\u001f \u0001\u0000\u0000\u0000 $"+
		"\u0001\u0000\u0000\u0000!#\u0003\u0004\u0002\u0000\"!\u0001\u0000\u0000"+
		"\u0000#&\u0001\u0000\u0000\u0000$\"\u0001\u0000\u0000\u0000$%\u0001\u0000"+
		"\u0000\u0000%+\u0001\u0000\u0000\u0000&$\u0001\u0000\u0000\u0000\'*\u0003"+
		"\b\u0004\u0000(*\u0003\u0018\f\u0000)\'\u0001\u0000\u0000\u0000)(\u0001"+
		"\u0000\u0000\u0000*-\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000"+
		"+,\u0001\u0000\u0000\u0000,.\u0001\u0000\u0000\u0000-+\u0001\u0000\u0000"+
		"\u0000./\u0005\u0000\u0000\u0001/\u0001\u0001\u0000\u0000\u000001\u0005"+
		"\u0017\u0000\u000012\u0003\u0006\u0003\u000028\u0005\u000f\u0000\u0000"+
		"37\u0003\u0004\u0002\u000047\u0003\b\u0004\u000057\u0003\u0018\f\u0000"+
		"63\u0001\u0000\u0000\u000064\u0001\u0000\u0000\u000065\u0001\u0000\u0000"+
		"\u00007:\u0001\u0000\u0000\u000086\u0001\u0000\u0000\u000089\u0001\u0000"+
		"\u0000\u00009;\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000\u0000;<\u0005"+
		"\u0010\u0000\u0000<\u0003\u0001\u0000\u0000\u0000=?\u0005\u0018\u0000"+
		"\u0000>=\u0001\u0000\u0000\u0000>?\u0001\u0000\u0000\u0000?@\u0001\u0000"+
		"\u0000\u0000@A\u0005\u0019\u0000\u0000AB\u0003\u0006\u0003\u0000BC\u0005"+
		"\u001a\u0000\u0000CD\u0005\u001b\u0000\u0000DE\u0005\f\u0000\u0000E\u0005"+
		"\u0001\u0000\u0000\u0000FK\u0005\u0013\u0000\u0000GH\u0005\u001a\u0000"+
		"\u0000HJ\u0005\u0013\u0000\u0000IG\u0001\u0000\u0000\u0000JM\u0001\u0000"+
		"\u0000\u0000KI\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000L\u0007"+
		"\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000NO\u0005\u0001\u0000"+
		"\u0000OR\u0005\u0013\u0000\u0000PQ\u0005\u000b\u0000\u0000QS\u0005\u0013"+
		"\u0000\u0000RP\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000ST\u0001"+
		"\u0000\u0000\u0000T\\\u0005\u000f\u0000\u0000U[\u0003\f\u0006\u0000V["+
		"\u0003\u0018\f\u0000W[\u0003\n\u0005\u0000X[\u0003\u0010\b\u0000Y[\u0003"+
		"\b\u0004\u0000ZU\u0001\u0000\u0000\u0000ZV\u0001\u0000\u0000\u0000ZW\u0001"+
		"\u0000\u0000\u0000ZX\u0001\u0000\u0000\u0000ZY\u0001\u0000\u0000\u0000"+
		"[^\u0001\u0000\u0000\u0000\\Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000"+
		"\u0000]_\u0001\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000_`\u0005\u0010"+
		"\u0000\u0000`\t\u0001\u0000\u0000\u0000ac\u0005\u0003\u0000\u0000bd\u0005"+
		"\u0007\u0000\u0000cb\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000"+
		"de\u0001\u0000\u0000\u0000ef\u0005\u0013\u0000\u0000fg\u0005\r\u0000\u0000"+
		"gh\u0003\u0016\u000b\u0000hi\u0005\f\u0000\u0000in\u0001\u0000\u0000\u0000"+
		"jk\u0005\u0004\u0000\u0000kl\u0005\u0013\u0000\u0000ln\u0005\f\u0000\u0000"+
		"ma\u0001\u0000\u0000\u0000mj\u0001\u0000\u0000\u0000n\u000b\u0001\u0000"+
		"\u0000\u0000op\u0005\u0006\u0000\u0000pq\u0005\u0013\u0000\u0000qr\u0005"+
		"\u000b\u0000\u0000r{\u0005\u0013\u0000\u0000sw\u0005\u000f\u0000\u0000"+
		"tv\u0003\u000e\u0007\u0000ut\u0001\u0000\u0000\u0000vy\u0001\u0000\u0000"+
		"\u0000wu\u0001\u0000\u0000\u0000wx\u0001\u0000\u0000\u0000xz\u0001\u0000"+
		"\u0000\u0000yw\u0001\u0000\u0000\u0000z|\u0005\u0010\u0000\u0000{s\u0001"+
		"\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000"+
		"}~\u0005\f\u0000\u0000~\r\u0001\u0000\u0000\u0000\u007f\u0080\u0005\u0007"+
		"\u0000\u0000\u0080\u0081\u0005\u0013\u0000\u0000\u0081\u0082\u0005\r\u0000"+
		"\u0000\u0082\u0083\u0003\u0016\u000b\u0000\u0083\u0084\u0005\f\u0000\u0000"+
		"\u0084\u000f\u0001\u0000\u0000\u0000\u0085\u0088\u0003\u0012\t\u0000\u0086"+
		"\u0088\u0003\u0014\n\u0000\u0087\u0085\u0001\u0000\u0000\u0000\u0087\u0086"+
		"\u0001\u0000\u0000\u0000\u0088\u0011\u0001\u0000\u0000\u0000\u0089\u008a"+
		"\u0005\b\u0000\u0000\u008a\u008b\u0005\u0013\u0000\u0000\u008b\u008c\u0005"+
		"\f\u0000\u0000\u008c\u0013\u0001\u0000\u0000\u0000\u008d\u008e\u0005\t"+
		"\u0000\u0000\u008e\u008f\u0005\n\u0000\u0000\u008f\u0095\u0005\f\u0000"+
		"\u0000\u0090\u0091\u0005\t\u0000\u0000\u0091\u0092\u0005\u0005\u0000\u0000"+
		"\u0092\u0093\u0005\u0013\u0000\u0000\u0093\u0095\u0005\f\u0000\u0000\u0094"+
		"\u008d\u0001\u0000\u0000\u0000\u0094\u0090\u0001\u0000\u0000\u0000\u0095"+
		"\u0015\u0001\u0000\u0000\u0000\u0096\u009d\u0005\u0013\u0000\u0000\u0097"+
		"\u0098\u0005\u0013\u0000\u0000\u0098\u0099\u0005\u000e\u0000\u0000\u0099"+
		"\u009d\u0005\u0013\u0000\u0000\u009a\u009d\u0005\u0014\u0000\u0000\u009b"+
		"\u009d\u0005\u0015\u0000\u0000\u009c\u0096\u0001\u0000\u0000\u0000\u009c"+
		"\u0097\u0001\u0000\u0000\u0000\u009c\u009a\u0001\u0000\u0000\u0000\u009c"+
		"\u009b\u0001\u0000\u0000\u0000\u009d\u0017\u0001\u0000\u0000\u0000\u009e"+
		"\u009f\u0005\u0002\u0000\u0000\u009f\u00a0\u0005\u0013\u0000\u0000\u00a0"+
		"\u00a1\u0005\u000b\u0000\u0000\u00a1\u00a2\u0005\u0013\u0000\u0000\u00a2"+
		"\u00a6\u0005\u000f\u0000\u0000\u00a3\u00a5\u0003\u001a\r\u0000\u00a4\u00a3"+
		"\u0001\u0000\u0000\u0000\u00a5\u00a8\u0001\u0000\u0000\u0000\u00a6\u00a4"+
		"\u0001\u0000\u0000\u0000\u00a6\u00a7\u0001\u0000\u0000\u0000\u00a7\u00a9"+
		"\u0001\u0000\u0000\u0000\u00a8\u00a6\u0001\u0000\u0000\u0000\u00a9\u00aa"+
		"\u0005\u0010\u0000\u0000\u00aa\u0019\u0001\u0000\u0000\u0000\u00ab\u00ac"+
		"\u0005\u0006\u0000\u0000\u00ac\u00ad\u0005\u0007\u0000\u0000\u00ad\u00ae"+
		"\u0005\u0013\u0000\u0000\u00ae\u00af\u0005\r\u0000\u0000\u00af\u00b1\u0003"+
		"\u0016\u000b\u0000\u00b0\u00b2\u0003\u001c\u000e\u0000\u00b1\u00b0\u0001"+
		"\u0000\u0000\u0000\u00b1\u00b2\u0001\u0000\u0000\u0000\u00b2\u00b3\u0001"+
		"\u0000\u0000\u0000\u00b3\u00b4\u0005\f\u0000\u0000\u00b4\u00b9\u0001\u0000"+
		"\u0000\u0000\u00b5\u00b6\u0005\u0005\u0000\u0000\u00b6\u00b7\u0005\u0013"+
		"\u0000\u0000\u00b7\u00b9\u0005\f\u0000\u0000\u00b8\u00ab\u0001\u0000\u0000"+
		"\u0000\u00b8\u00b5\u0001\u0000\u0000\u0000\u00b9\u001b\u0001\u0000\u0000"+
		"\u0000\u00ba\u00bb\u0005\u0011\u0000\u0000\u00bb\u00bc\u0005\u0013\u0000"+
		"\u0000\u00bc\u00bd\u0005\u0012\u0000\u0000\u00bd\u001d\u0001\u0000\u0000"+
		"\u0000\u0015\u001f$)+68>KRZ\\cmw{\u0087\u0094\u009c\u00a6\u00b1\u00b8";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}