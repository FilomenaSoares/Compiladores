// Generated from c:/Users/memmy/OneDrive/Documentos/GitHub/Compiladores/fimly.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class fimlyParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INICIO=1, LEIA=2, ESCREVA=3, FIM=4, SE=5, ENTAO=6, SENAO=7, ENQUANTO=8, 
		FACA=9, TIPO_INTEIRO=10, TIPO_FLOAT=11, TIPO_STRING=12, ADICAO=13, SUBTRACAO=14, 
		DIVISAO=15, MULTIPLICA=16, IGUAL=17, DIFERENTE=18, MAIORIGUAL=19, MENORIGUAL=20, 
		MAIOR=21, MENOR=22, ATRIBUICAO=23, NAO=24, E=25, OU=26, ABRE_PAR=27, DOIS_PONTOS=28, 
		FECHA_PAR=29, ABRE_CHAVE=30, FECHA_CHAVE=31, PONTO_VIR=32, VIRG=33, ID=34, 
		INTEIRO=35, FLOAT=36, STRING=37, COMENTARIO=38, WS=39;
	public static final int
		RULE_fimly = 0, RULE_comando_declaracao = 1, RULE_tipo = 2, RULE_comandos = 3, 
		RULE_comando_ler = 4, RULE_comando_escrever = 5, RULE_lista_expressao = 6, 
		RULE_bloco_comandos = 7, RULE_comando_condicional = 8, RULE_comando_repeticao = 9, 
		RULE_comando_atribuicao = 10, RULE_expressao = 11, RULE_expressao_logica = 12, 
		RULE_expressao_comparacao = 13, RULE_expressao_aritmetica = 14, RULE_termo = 15, 
		RULE_fator = 16;
	private static String[] makeRuleNames() {
		return new String[] {
			"fimly", "comando_declaracao", "tipo", "comandos", "comando_ler", "comando_escrever", 
			"lista_expressao", "bloco_comandos", "comando_condicional", "comando_repeticao", 
			"comando_atribuicao", "expressao", "expressao_logica", "expressao_comparacao", 
			"expressao_aritmetica", "termo", "fator"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'inicio'", "'leia'", "'escreva'", "'fim'", "'se'", "'entao'", 
			"'senao'", "'enquanto'", "'faca'", "'int'", "'float'", "'string'", "'+'", 
			"'-'", "'/'", "'*'", "'=='", "'!='", "'>='", "'<='", "'>'", "'<'", "'='", 
			"'!'", "'&&'", "'||'", "'('", "':'", "')'", "'{'", "'}'", "';'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INICIO", "LEIA", "ESCREVA", "FIM", "SE", "ENTAO", "SENAO", "ENQUANTO", 
			"FACA", "TIPO_INTEIRO", "TIPO_FLOAT", "TIPO_STRING", "ADICAO", "SUBTRACAO", 
			"DIVISAO", "MULTIPLICA", "IGUAL", "DIFERENTE", "MAIORIGUAL", "MENORIGUAL", 
			"MAIOR", "MENOR", "ATRIBUICAO", "NAO", "E", "OU", "ABRE_PAR", "DOIS_PONTOS", 
			"FECHA_PAR", "ABRE_CHAVE", "FECHA_CHAVE", "PONTO_VIR", "VIRG", "ID", 
			"INTEIRO", "FLOAT", "STRING", "COMENTARIO", "WS"
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
	public String getGrammarFileName() { return "fimly.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public fimlyParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FimlyContext extends ParserRuleContext {
		public TerminalNode INICIO() { return getToken(fimlyParser.INICIO, 0); }
		public TerminalNode FIM() { return getToken(fimlyParser.FIM, 0); }
		public List<Comando_declaracaoContext> comando_declaracao() {
			return getRuleContexts(Comando_declaracaoContext.class);
		}
		public Comando_declaracaoContext comando_declaracao(int i) {
			return getRuleContext(Comando_declaracaoContext.class,i);
		}
		public List<ComandosContext> comandos() {
			return getRuleContexts(ComandosContext.class);
		}
		public ComandosContext comandos(int i) {
			return getRuleContext(ComandosContext.class,i);
		}
		public FimlyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fimly; }
	}

	public final FimlyContext fimly() throws RecognitionException {
		FimlyContext _localctx = new FimlyContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_fimly);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(37);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(34);
				comando_declaracao();
				}
				}
				setState(39);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(40);
			match(INICIO);
			setState(44);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17179869484L) != 0)) {
				{
				{
				setState(41);
				comandos();
				}
				}
				setState(46);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(47);
			match(FIM);
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
	public static class Comando_declaracaoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(fimlyParser.ID, 0); }
		public TerminalNode DOIS_PONTOS() { return getToken(fimlyParser.DOIS_PONTOS, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode PONTO_VIR() { return getToken(fimlyParser.PONTO_VIR, 0); }
		public Comando_declaracaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_declaracao; }
	}

	public final Comando_declaracaoContext comando_declaracao() throws RecognitionException {
		Comando_declaracaoContext _localctx = new Comando_declaracaoContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_comando_declaracao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			match(ID);
			setState(50);
			match(DOIS_PONTOS);
			setState(51);
			tipo();
			setState(52);
			match(PONTO_VIR);
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
	public static class TipoContext extends ParserRuleContext {
		public TerminalNode TIPO_INTEIRO() { return getToken(fimlyParser.TIPO_INTEIRO, 0); }
		public TerminalNode TIPO_FLOAT() { return getToken(fimlyParser.TIPO_FLOAT, 0); }
		public TerminalNode TIPO_STRING() { return getToken(fimlyParser.TIPO_STRING, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7168L) != 0)) ) {
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
	public static class ComandosContext extends ParserRuleContext {
		public Comando_lerContext comando_ler() {
			return getRuleContext(Comando_lerContext.class,0);
		}
		public Comando_escreverContext comando_escrever() {
			return getRuleContext(Comando_escreverContext.class,0);
		}
		public Comando_condicionalContext comando_condicional() {
			return getRuleContext(Comando_condicionalContext.class,0);
		}
		public Comando_repeticaoContext comando_repeticao() {
			return getRuleContext(Comando_repeticaoContext.class,0);
		}
		public Comando_atribuicaoContext comando_atribuicao() {
			return getRuleContext(Comando_atribuicaoContext.class,0);
		}
		public ComandosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comandos; }
	}

	public final ComandosContext comandos() throws RecognitionException {
		ComandosContext _localctx = new ComandosContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_comandos);
		try {
			setState(61);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEIA:
				enterOuterAlt(_localctx, 1);
				{
				setState(56);
				comando_ler();
				}
				break;
			case ESCREVA:
				enterOuterAlt(_localctx, 2);
				{
				setState(57);
				comando_escrever();
				}
				break;
			case SE:
				enterOuterAlt(_localctx, 3);
				{
				setState(58);
				comando_condicional();
				}
				break;
			case ENQUANTO:
				enterOuterAlt(_localctx, 4);
				{
				setState(59);
				comando_repeticao();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 5);
				{
				setState(60);
				comando_atribuicao();
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
	public static class Comando_lerContext extends ParserRuleContext {
		public TerminalNode LEIA() { return getToken(fimlyParser.LEIA, 0); }
		public TerminalNode ABRE_PAR() { return getToken(fimlyParser.ABRE_PAR, 0); }
		public TerminalNode ID() { return getToken(fimlyParser.ID, 0); }
		public TerminalNode FECHA_PAR() { return getToken(fimlyParser.FECHA_PAR, 0); }
		public TerminalNode PONTO_VIR() { return getToken(fimlyParser.PONTO_VIR, 0); }
		public Comando_lerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_ler; }
	}

	public final Comando_lerContext comando_ler() throws RecognitionException {
		Comando_lerContext _localctx = new Comando_lerContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_comando_ler);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(LEIA);
			setState(64);
			match(ABRE_PAR);
			setState(65);
			match(ID);
			setState(66);
			match(FECHA_PAR);
			setState(67);
			match(PONTO_VIR);
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
	public static class Comando_escreverContext extends ParserRuleContext {
		public TerminalNode ESCREVA() { return getToken(fimlyParser.ESCREVA, 0); }
		public TerminalNode ABRE_PAR() { return getToken(fimlyParser.ABRE_PAR, 0); }
		public TerminalNode FECHA_PAR() { return getToken(fimlyParser.FECHA_PAR, 0); }
		public TerminalNode PONTO_VIR() { return getToken(fimlyParser.PONTO_VIR, 0); }
		public Lista_expressaoContext lista_expressao() {
			return getRuleContext(Lista_expressaoContext.class,0);
		}
		public Comando_escreverContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_escrever; }
	}

	public final Comando_escreverContext comando_escrever() throws RecognitionException {
		Comando_escreverContext _localctx = new Comando_escreverContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_comando_escrever);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			match(ESCREVA);
			setState(70);
			match(ABRE_PAR);
			setState(72);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 257832255488L) != 0)) {
				{
				setState(71);
				lista_expressao();
				}
			}

			setState(74);
			match(FECHA_PAR);
			setState(75);
			match(PONTO_VIR);
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
	public static class Lista_expressaoContext extends ParserRuleContext {
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public List<TerminalNode> VIRG() { return getTokens(fimlyParser.VIRG); }
		public TerminalNode VIRG(int i) {
			return getToken(fimlyParser.VIRG, i);
		}
		public Lista_expressaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_expressao; }
	}

	public final Lista_expressaoContext lista_expressao() throws RecognitionException {
		Lista_expressaoContext _localctx = new Lista_expressaoContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_lista_expressao);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			expressao();
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VIRG) {
				{
				{
				setState(78);
				match(VIRG);
				setState(79);
				expressao();
				}
				}
				setState(84);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class Bloco_comandosContext extends ParserRuleContext {
		public TerminalNode ABRE_CHAVE() { return getToken(fimlyParser.ABRE_CHAVE, 0); }
		public TerminalNode FECHA_CHAVE() { return getToken(fimlyParser.FECHA_CHAVE, 0); }
		public List<ComandosContext> comandos() {
			return getRuleContexts(ComandosContext.class);
		}
		public ComandosContext comandos(int i) {
			return getRuleContext(ComandosContext.class,i);
		}
		public Bloco_comandosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloco_comandos; }
	}

	public final Bloco_comandosContext bloco_comandos() throws RecognitionException {
		Bloco_comandosContext _localctx = new Bloco_comandosContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_bloco_comandos);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(ABRE_CHAVE);
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17179869484L) != 0)) {
				{
				{
				setState(86);
				comandos();
				}
				}
				setState(91);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(92);
			match(FECHA_CHAVE);
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
	public static class Comando_condicionalContext extends ParserRuleContext {
		public TerminalNode SE() { return getToken(fimlyParser.SE, 0); }
		public TerminalNode ABRE_PAR() { return getToken(fimlyParser.ABRE_PAR, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode FECHA_PAR() { return getToken(fimlyParser.FECHA_PAR, 0); }
		public List<Bloco_comandosContext> bloco_comandos() {
			return getRuleContexts(Bloco_comandosContext.class);
		}
		public Bloco_comandosContext bloco_comandos(int i) {
			return getRuleContext(Bloco_comandosContext.class,i);
		}
		public TerminalNode SENAO() { return getToken(fimlyParser.SENAO, 0); }
		public Comando_condicionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_condicional; }
	}

	public final Comando_condicionalContext comando_condicional() throws RecognitionException {
		Comando_condicionalContext _localctx = new Comando_condicionalContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_comando_condicional);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(SE);
			setState(95);
			match(ABRE_PAR);
			setState(96);
			expressao();
			setState(97);
			match(FECHA_PAR);
			setState(98);
			bloco_comandos();
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SENAO) {
				{
				setState(99);
				match(SENAO);
				setState(100);
				bloco_comandos();
				}
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
	public static class Comando_repeticaoContext extends ParserRuleContext {
		public TerminalNode ENQUANTO() { return getToken(fimlyParser.ENQUANTO, 0); }
		public TerminalNode ABRE_PAR() { return getToken(fimlyParser.ABRE_PAR, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode FECHA_PAR() { return getToken(fimlyParser.FECHA_PAR, 0); }
		public TerminalNode FACA() { return getToken(fimlyParser.FACA, 0); }
		public Bloco_comandosContext bloco_comandos() {
			return getRuleContext(Bloco_comandosContext.class,0);
		}
		public Comando_repeticaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_repeticao; }
	}

	public final Comando_repeticaoContext comando_repeticao() throws RecognitionException {
		Comando_repeticaoContext _localctx = new Comando_repeticaoContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_comando_repeticao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			match(ENQUANTO);
			setState(104);
			match(ABRE_PAR);
			setState(105);
			expressao();
			setState(106);
			match(FECHA_PAR);
			setState(107);
			match(FACA);
			setState(108);
			bloco_comandos();
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
	public static class Comando_atribuicaoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(fimlyParser.ID, 0); }
		public TerminalNode ATRIBUICAO() { return getToken(fimlyParser.ATRIBUICAO, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode PONTO_VIR() { return getToken(fimlyParser.PONTO_VIR, 0); }
		public Comando_atribuicaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_atribuicao; }
	}

	public final Comando_atribuicaoContext comando_atribuicao() throws RecognitionException {
		Comando_atribuicaoContext _localctx = new Comando_atribuicaoContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_comando_atribuicao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			match(ID);
			setState(111);
			match(ATRIBUICAO);
			setState(112);
			expressao();
			setState(113);
			match(PONTO_VIR);
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
	public static class ExpressaoContext extends ParserRuleContext {
		public Expressao_logicaContext expressao_logica() {
			return getRuleContext(Expressao_logicaContext.class,0);
		}
		public ExpressaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao; }
	}

	public final ExpressaoContext expressao() throws RecognitionException {
		ExpressaoContext _localctx = new ExpressaoContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_expressao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			expressao_logica();
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
	public static class Expressao_logicaContext extends ParserRuleContext {
		public List<Expressao_comparacaoContext> expressao_comparacao() {
			return getRuleContexts(Expressao_comparacaoContext.class);
		}
		public Expressao_comparacaoContext expressao_comparacao(int i) {
			return getRuleContext(Expressao_comparacaoContext.class,i);
		}
		public List<TerminalNode> E() { return getTokens(fimlyParser.E); }
		public TerminalNode E(int i) {
			return getToken(fimlyParser.E, i);
		}
		public List<TerminalNode> OU() { return getTokens(fimlyParser.OU); }
		public TerminalNode OU(int i) {
			return getToken(fimlyParser.OU, i);
		}
		public Expressao_logicaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao_logica; }
	}

	public final Expressao_logicaContext expressao_logica() throws RecognitionException {
		Expressao_logicaContext _localctx = new Expressao_logicaContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_expressao_logica);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			expressao_comparacao();
			setState(122);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==E || _la==OU) {
				{
				{
				setState(118);
				_la = _input.LA(1);
				if ( !(_la==E || _la==OU) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(119);
				expressao_comparacao();
				}
				}
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class Expressao_comparacaoContext extends ParserRuleContext {
		public List<Expressao_aritmeticaContext> expressao_aritmetica() {
			return getRuleContexts(Expressao_aritmeticaContext.class);
		}
		public Expressao_aritmeticaContext expressao_aritmetica(int i) {
			return getRuleContext(Expressao_aritmeticaContext.class,i);
		}
		public TerminalNode IGUAL() { return getToken(fimlyParser.IGUAL, 0); }
		public TerminalNode DIFERENTE() { return getToken(fimlyParser.DIFERENTE, 0); }
		public TerminalNode MAIOR() { return getToken(fimlyParser.MAIOR, 0); }
		public TerminalNode MAIORIGUAL() { return getToken(fimlyParser.MAIORIGUAL, 0); }
		public TerminalNode MENOR() { return getToken(fimlyParser.MENOR, 0); }
		public TerminalNode MENORIGUAL() { return getToken(fimlyParser.MENORIGUAL, 0); }
		public Expressao_comparacaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao_comparacao; }
	}

	public final Expressao_comparacaoContext expressao_comparacao() throws RecognitionException {
		Expressao_comparacaoContext _localctx = new Expressao_comparacaoContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_expressao_comparacao);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			expressao_aritmetica();
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8257536L) != 0)) {
				{
				setState(126);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 8257536L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(127);
				expressao_aritmetica();
				}
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
	public static class Expressao_aritmeticaContext extends ParserRuleContext {
		public List<TermoContext> termo() {
			return getRuleContexts(TermoContext.class);
		}
		public TermoContext termo(int i) {
			return getRuleContext(TermoContext.class,i);
		}
		public List<TerminalNode> ADICAO() { return getTokens(fimlyParser.ADICAO); }
		public TerminalNode ADICAO(int i) {
			return getToken(fimlyParser.ADICAO, i);
		}
		public List<TerminalNode> SUBTRACAO() { return getTokens(fimlyParser.SUBTRACAO); }
		public TerminalNode SUBTRACAO(int i) {
			return getToken(fimlyParser.SUBTRACAO, i);
		}
		public Expressao_aritmeticaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao_aritmetica; }
	}

	public final Expressao_aritmeticaContext expressao_aritmetica() throws RecognitionException {
		Expressao_aritmeticaContext _localctx = new Expressao_aritmeticaContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_expressao_aritmetica);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			termo();
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ADICAO || _la==SUBTRACAO) {
				{
				{
				setState(131);
				_la = _input.LA(1);
				if ( !(_la==ADICAO || _la==SUBTRACAO) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(132);
				termo();
				}
				}
				setState(137);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class TermoContext extends ParserRuleContext {
		public List<FatorContext> fator() {
			return getRuleContexts(FatorContext.class);
		}
		public FatorContext fator(int i) {
			return getRuleContext(FatorContext.class,i);
		}
		public List<TerminalNode> MULTIPLICA() { return getTokens(fimlyParser.MULTIPLICA); }
		public TerminalNode MULTIPLICA(int i) {
			return getToken(fimlyParser.MULTIPLICA, i);
		}
		public List<TerminalNode> DIVISAO() { return getTokens(fimlyParser.DIVISAO); }
		public TerminalNode DIVISAO(int i) {
			return getToken(fimlyParser.DIVISAO, i);
		}
		public TermoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termo; }
	}

	public final TermoContext termo() throws RecognitionException {
		TermoContext _localctx = new TermoContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_termo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			fator();
			setState(143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DIVISAO || _la==MULTIPLICA) {
				{
				{
				setState(139);
				_la = _input.LA(1);
				if ( !(_la==DIVISAO || _la==MULTIPLICA) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(140);
				fator();
				}
				}
				setState(145);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class FatorContext extends ParserRuleContext {
		public TerminalNode INTEIRO() { return getToken(fimlyParser.INTEIRO, 0); }
		public TerminalNode FLOAT() { return getToken(fimlyParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(fimlyParser.STRING, 0); }
		public TerminalNode ID() { return getToken(fimlyParser.ID, 0); }
		public TerminalNode ABRE_PAR() { return getToken(fimlyParser.ABRE_PAR, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode FECHA_PAR() { return getToken(fimlyParser.FECHA_PAR, 0); }
		public FatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fator; }
	}

	public final FatorContext fator() throws RecognitionException {
		FatorContext _localctx = new FatorContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_fator);
		try {
			setState(154);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEIRO:
				enterOuterAlt(_localctx, 1);
				{
				setState(146);
				match(INTEIRO);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(147);
				match(FLOAT);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 3);
				{
				setState(148);
				match(STRING);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 4);
				{
				setState(149);
				match(ID);
				}
				break;
			case ABRE_PAR:
				enterOuterAlt(_localctx, 5);
				{
				setState(150);
				match(ABRE_PAR);
				setState(151);
				expressao();
				setState(152);
				match(FECHA_PAR);
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

	public static final String _serializedATN =
		"\u0004\u0001\'\u009d\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0001\u0000\u0005\u0000$\b\u0000\n\u0000\f\u0000"+
		"\'\t\u0000\u0001\u0000\u0001\u0000\u0005\u0000+\b\u0000\n\u0000\f\u0000"+
		".\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003>\b\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0003\u0005I\b\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006Q\b\u0006"+
		"\n\u0006\f\u0006T\t\u0006\u0001\u0007\u0001\u0007\u0005\u0007X\b\u0007"+
		"\n\u0007\f\u0007[\t\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\bf\b\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0005\fy\b\f\n\f\f"+
		"\f|\t\f\u0001\r\u0001\r\u0001\r\u0003\r\u0081\b\r\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0005\u000e\u0086\b\u000e\n\u000e\f\u000e\u0089\t\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u008e\b\u000f\n\u000f\f\u000f"+
		"\u0091\t\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u009b\b\u0010\u0001\u0010"+
		"\u0000\u0000\u0011\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \u0000\u0005\u0001\u0000\n\f\u0001\u0000"+
		"\u0019\u001a\u0001\u0000\u0011\u0016\u0001\u0000\r\u000e\u0001\u0000\u000f"+
		"\u0010\u009d\u0000%\u0001\u0000\u0000\u0000\u00021\u0001\u0000\u0000\u0000"+
		"\u00046\u0001\u0000\u0000\u0000\u0006=\u0001\u0000\u0000\u0000\b?\u0001"+
		"\u0000\u0000\u0000\nE\u0001\u0000\u0000\u0000\fM\u0001\u0000\u0000\u0000"+
		"\u000eU\u0001\u0000\u0000\u0000\u0010^\u0001\u0000\u0000\u0000\u0012g"+
		"\u0001\u0000\u0000\u0000\u0014n\u0001\u0000\u0000\u0000\u0016s\u0001\u0000"+
		"\u0000\u0000\u0018u\u0001\u0000\u0000\u0000\u001a}\u0001\u0000\u0000\u0000"+
		"\u001c\u0082\u0001\u0000\u0000\u0000\u001e\u008a\u0001\u0000\u0000\u0000"+
		" \u009a\u0001\u0000\u0000\u0000\"$\u0003\u0002\u0001\u0000#\"\u0001\u0000"+
		"\u0000\u0000$\'\u0001\u0000\u0000\u0000%#\u0001\u0000\u0000\u0000%&\u0001"+
		"\u0000\u0000\u0000&(\u0001\u0000\u0000\u0000\'%\u0001\u0000\u0000\u0000"+
		"(,\u0005\u0001\u0000\u0000)+\u0003\u0006\u0003\u0000*)\u0001\u0000\u0000"+
		"\u0000+.\u0001\u0000\u0000\u0000,*\u0001\u0000\u0000\u0000,-\u0001\u0000"+
		"\u0000\u0000-/\u0001\u0000\u0000\u0000.,\u0001\u0000\u0000\u0000/0\u0005"+
		"\u0004\u0000\u00000\u0001\u0001\u0000\u0000\u000012\u0005\"\u0000\u0000"+
		"23\u0005\u001c\u0000\u000034\u0003\u0004\u0002\u000045\u0005 \u0000\u0000"+
		"5\u0003\u0001\u0000\u0000\u000067\u0007\u0000\u0000\u00007\u0005\u0001"+
		"\u0000\u0000\u00008>\u0003\b\u0004\u00009>\u0003\n\u0005\u0000:>\u0003"+
		"\u0010\b\u0000;>\u0003\u0012\t\u0000<>\u0003\u0014\n\u0000=8\u0001\u0000"+
		"\u0000\u0000=9\u0001\u0000\u0000\u0000=:\u0001\u0000\u0000\u0000=;\u0001"+
		"\u0000\u0000\u0000=<\u0001\u0000\u0000\u0000>\u0007\u0001\u0000\u0000"+
		"\u0000?@\u0005\u0002\u0000\u0000@A\u0005\u001b\u0000\u0000AB\u0005\"\u0000"+
		"\u0000BC\u0005\u001d\u0000\u0000CD\u0005 \u0000\u0000D\t\u0001\u0000\u0000"+
		"\u0000EF\u0005\u0003\u0000\u0000FH\u0005\u001b\u0000\u0000GI\u0003\f\u0006"+
		"\u0000HG\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000IJ\u0001\u0000"+
		"\u0000\u0000JK\u0005\u001d\u0000\u0000KL\u0005 \u0000\u0000L\u000b\u0001"+
		"\u0000\u0000\u0000MR\u0003\u0016\u000b\u0000NO\u0005!\u0000\u0000OQ\u0003"+
		"\u0016\u000b\u0000PN\u0001\u0000\u0000\u0000QT\u0001\u0000\u0000\u0000"+
		"RP\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000S\r\u0001\u0000\u0000"+
		"\u0000TR\u0001\u0000\u0000\u0000UY\u0005\u001e\u0000\u0000VX\u0003\u0006"+
		"\u0003\u0000WV\u0001\u0000\u0000\u0000X[\u0001\u0000\u0000\u0000YW\u0001"+
		"\u0000\u0000\u0000YZ\u0001\u0000\u0000\u0000Z\\\u0001\u0000\u0000\u0000"+
		"[Y\u0001\u0000\u0000\u0000\\]\u0005\u001f\u0000\u0000]\u000f\u0001\u0000"+
		"\u0000\u0000^_\u0005\u0005\u0000\u0000_`\u0005\u001b\u0000\u0000`a\u0003"+
		"\u0016\u000b\u0000ab\u0005\u001d\u0000\u0000be\u0003\u000e\u0007\u0000"+
		"cd\u0005\u0007\u0000\u0000df\u0003\u000e\u0007\u0000ec\u0001\u0000\u0000"+
		"\u0000ef\u0001\u0000\u0000\u0000f\u0011\u0001\u0000\u0000\u0000gh\u0005"+
		"\b\u0000\u0000hi\u0005\u001b\u0000\u0000ij\u0003\u0016\u000b\u0000jk\u0005"+
		"\u001d\u0000\u0000kl\u0005\t\u0000\u0000lm\u0003\u000e\u0007\u0000m\u0013"+
		"\u0001\u0000\u0000\u0000no\u0005\"\u0000\u0000op\u0005\u0017\u0000\u0000"+
		"pq\u0003\u0016\u000b\u0000qr\u0005 \u0000\u0000r\u0015\u0001\u0000\u0000"+
		"\u0000st\u0003\u0018\f\u0000t\u0017\u0001\u0000\u0000\u0000uz\u0003\u001a"+
		"\r\u0000vw\u0007\u0001\u0000\u0000wy\u0003\u001a\r\u0000xv\u0001\u0000"+
		"\u0000\u0000y|\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000\u0000z{\u0001"+
		"\u0000\u0000\u0000{\u0019\u0001\u0000\u0000\u0000|z\u0001\u0000\u0000"+
		"\u0000}\u0080\u0003\u001c\u000e\u0000~\u007f\u0007\u0002\u0000\u0000\u007f"+
		"\u0081\u0003\u001c\u000e\u0000\u0080~\u0001\u0000\u0000\u0000\u0080\u0081"+
		"\u0001\u0000\u0000\u0000\u0081\u001b\u0001\u0000\u0000\u0000\u0082\u0087"+
		"\u0003\u001e\u000f\u0000\u0083\u0084\u0007\u0003\u0000\u0000\u0084\u0086"+
		"\u0003\u001e\u000f\u0000\u0085\u0083\u0001\u0000\u0000\u0000\u0086\u0089"+
		"\u0001\u0000\u0000\u0000\u0087\u0085\u0001\u0000\u0000\u0000\u0087\u0088"+
		"\u0001\u0000\u0000\u0000\u0088\u001d\u0001\u0000\u0000\u0000\u0089\u0087"+
		"\u0001\u0000\u0000\u0000\u008a\u008f\u0003 \u0010\u0000\u008b\u008c\u0007"+
		"\u0004\u0000\u0000\u008c\u008e\u0003 \u0010\u0000\u008d\u008b\u0001\u0000"+
		"\u0000\u0000\u008e\u0091\u0001\u0000\u0000\u0000\u008f\u008d\u0001\u0000"+
		"\u0000\u0000\u008f\u0090\u0001\u0000\u0000\u0000\u0090\u001f\u0001\u0000"+
		"\u0000\u0000\u0091\u008f\u0001\u0000\u0000\u0000\u0092\u009b\u0005#\u0000"+
		"\u0000\u0093\u009b\u0005$\u0000\u0000\u0094\u009b\u0005%\u0000\u0000\u0095"+
		"\u009b\u0005\"\u0000\u0000\u0096\u0097\u0005\u001b\u0000\u0000\u0097\u0098"+
		"\u0003\u0016\u000b\u0000\u0098\u0099\u0005\u001d\u0000\u0000\u0099\u009b"+
		"\u0001\u0000\u0000\u0000\u009a\u0092\u0001\u0000\u0000\u0000\u009a\u0093"+
		"\u0001\u0000\u0000\u0000\u009a\u0094\u0001\u0000\u0000\u0000\u009a\u0095"+
		"\u0001\u0000\u0000\u0000\u009a\u0096\u0001\u0000\u0000\u0000\u009b!\u0001"+
		"\u0000\u0000\u0000\f%,=HRYez\u0080\u0087\u008f\u009a";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}