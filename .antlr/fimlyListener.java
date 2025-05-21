// Generated from c:/Users/Filomena/Desktop/Compiladores/fimly.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link fimlyParser}.
 */
public interface fimlyListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link fimlyParser#fimly}.
	 * @param ctx the parse tree
	 */
	void enterFimly(fimlyParser.FimlyContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#fimly}.
	 * @param ctx the parse tree
	 */
	void exitFimly(fimlyParser.FimlyContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#comando_declaracao}.
	 * @param ctx the parse tree
	 */
	void enterComando_declaracao(fimlyParser.Comando_declaracaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#comando_declaracao}.
	 * @param ctx the parse tree
	 */
	void exitComando_declaracao(fimlyParser.Comando_declaracaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(fimlyParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(fimlyParser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#comandos}.
	 * @param ctx the parse tree
	 */
	void enterComandos(fimlyParser.ComandosContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#comandos}.
	 * @param ctx the parse tree
	 */
	void exitComandos(fimlyParser.ComandosContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#comando_ler}.
	 * @param ctx the parse tree
	 */
	void enterComando_ler(fimlyParser.Comando_lerContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#comando_ler}.
	 * @param ctx the parse tree
	 */
	void exitComando_ler(fimlyParser.Comando_lerContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#comando_escrever}.
	 * @param ctx the parse tree
	 */
	void enterComando_escrever(fimlyParser.Comando_escreverContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#comando_escrever}.
	 * @param ctx the parse tree
	 */
	void exitComando_escrever(fimlyParser.Comando_escreverContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#lista_expressao}.
	 * @param ctx the parse tree
	 */
	void enterLista_expressao(fimlyParser.Lista_expressaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#lista_expressao}.
	 * @param ctx the parse tree
	 */
	void exitLista_expressao(fimlyParser.Lista_expressaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#bloco_comandos}.
	 * @param ctx the parse tree
	 */
	void enterBloco_comandos(fimlyParser.Bloco_comandosContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#bloco_comandos}.
	 * @param ctx the parse tree
	 */
	void exitBloco_comandos(fimlyParser.Bloco_comandosContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#comando_condicional}.
	 * @param ctx the parse tree
	 */
	void enterComando_condicional(fimlyParser.Comando_condicionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#comando_condicional}.
	 * @param ctx the parse tree
	 */
	void exitComando_condicional(fimlyParser.Comando_condicionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#comando_repeticao}.
	 * @param ctx the parse tree
	 */
	void enterComando_repeticao(fimlyParser.Comando_repeticaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#comando_repeticao}.
	 * @param ctx the parse tree
	 */
	void exitComando_repeticao(fimlyParser.Comando_repeticaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#comando_atribuicao}.
	 * @param ctx the parse tree
	 */
	void enterComando_atribuicao(fimlyParser.Comando_atribuicaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#comando_atribuicao}.
	 * @param ctx the parse tree
	 */
	void exitComando_atribuicao(fimlyParser.Comando_atribuicaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExpressao(fimlyParser.ExpressaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExpressao(fimlyParser.ExpressaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#expressao_logica}.
	 * @param ctx the parse tree
	 */
	void enterExpressao_logica(fimlyParser.Expressao_logicaContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#expressao_logica}.
	 * @param ctx the parse tree
	 */
	void exitExpressao_logica(fimlyParser.Expressao_logicaContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#expressao_comparacao}.
	 * @param ctx the parse tree
	 */
	void enterExpressao_comparacao(fimlyParser.Expressao_comparacaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#expressao_comparacao}.
	 * @param ctx the parse tree
	 */
	void exitExpressao_comparacao(fimlyParser.Expressao_comparacaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#expressao_aritmetica}.
	 * @param ctx the parse tree
	 */
	void enterExpressao_aritmetica(fimlyParser.Expressao_aritmeticaContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#expressao_aritmetica}.
	 * @param ctx the parse tree
	 */
	void exitExpressao_aritmetica(fimlyParser.Expressao_aritmeticaContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#termo}.
	 * @param ctx the parse tree
	 */
	void enterTermo(fimlyParser.TermoContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#termo}.
	 * @param ctx the parse tree
	 */
	void exitTermo(fimlyParser.TermoContext ctx);
	/**
	 * Enter a parse tree produced by {@link fimlyParser#fator}.
	 * @param ctx the parse tree
	 */
	void enterFator(fimlyParser.FatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link fimlyParser#fator}.
	 * @param ctx the parse tree
	 */
	void exitFator(fimlyParser.FatorContext ctx);
}