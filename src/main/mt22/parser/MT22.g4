grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (expression|statement|functiondecl|mainfunction|variabledecl|arraytype|COMMENT_C|COMMENT_CPP|STR|FLO|DEMENTION|INT|ID|LCB|COMA|RCB|ARR|SEM)* EOF ;

// ! --------------PARSER RULE--------------

vartype: STRING | BOOLEAN | FLOAT | INTEGER;
arithmetricop: MINU | PLUS | MUTI | DIVI | MODU;
booleanop: NOT | AND | OR;
stringop: SCOPE;
relationalop: EQUL | NEQ | LESS | GREA | LOEQ | GOEQ;

// ?testing expression
operator: arithmetricop| booleanop | stringop | relationalop | indexop;
// *Two operation type
operand: constant | vartype | operator | functioncall;
expression: operand stringop operand
		|operand relationalop operand
		|expression (AND|OR) operand
		|expression (PLUS|MINU) operand 
		|expression (MUTI|DIVI|MODU) operand
		|NOT operand
		|MINU operand
		|indexop operand
		|operand
		;

// ?constant not clear in ass1
constant: STR | BOOL | FLO | INT | ID;
functioncall: ID LB arguementlist RB;

indexop: ID expressionlist;

// ?testing expression


// *--------part of things--------
parameter: INHERIT? OUT? ID COL vartype;

indexexpression:;

//? arguement add-on
arguement: expression; //TODO arguement
functionmainprot:MAIN COL FUNCTION VOID LB parameterlist? RB;
functionprot: ID COL FUNCTION (VOID|vartype) LB parameterlist RB (INHERIT ID LSB RSB)?;
// ?add-on not found in mt22
functionmainbody: LCB statementlist? RCB;
functionbody: LCB statementlist RCB;

// *Statement
scalarvar: ID;
lhs: scalarvar | indexexpression;

statement: assignstatement 
| ifstatement 
| forstatement 
| whilestatement
| dowhilestatement
| breakstatement
| continuestatement
| returnstatement
| callstatement
| blockstatement
;

assignstatement: lhs EQU expression;

ifstatement: IF LB expression RB statement (ELSE statement)? ;
// ?I put expression for init-express and condition-express
// ? statement should be statement list
forstatement: FOR LB scalarvar EQU expression COMA expression COMA expression RB LCB statement RCB SEM;

whilestatement:WHILE LB expression RB LCB statement RCB SEM;

dowhilestatement: DO blockstatement WHILE LB expression RB SEM;

breakstatement: BREAK SEM;

continuestatement: CONTINUE SEM;

returnstatement: RETURN expression SEM;

callstatement: functioncall SEM;

blockstatement: LCB statementlist RCB;

// *--------List of ...--------
idlist: ID  COMA idlist | ID;
expressionlist: expression COMA expressionlist| expression;
parameterlist: parameter COMA parameterlist| parameter;
arguementlist: arguement COMA arguementlist | arguement;
statementlist: statement SEM statementlist | statement SEM;
// *--------Declare--------
variabledecl: idlist COL vartype  (EQU expressionlist)? SEM;
functiondecl: functionprot functionbody;
// ?unique function, whose name is main without any parameter and return nothing (type void).
mainfunction: functionmainprot functionmainbody;
// ?Is arrray type here?
arraytype:ARRAY LSB DEMENTION RSB OF INTEGER;

// !--------------LEXER RULE----------------

// * --------Comment--------
COMMENT_C : '/*' .*? '*/' -> skip ;
COMMENT_CPP : '//' ~[\r\n]* -> skip ;

// * --------String--------
fragment ESCAPE: '\\' ( 'b' | 'f' | 'n' | 'r' | 't' | '\'' | DB | '\\'| '"' );
STR: (DB (ESCAPE|~[\\"\r\n])*  DB) {self.text = self.text[1:-1]};
STRTYP: SCOPE;

// * --------Keyword--------
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';
MAIN:'main';

// *--------Boolean--------
FALSE: 'false';
TRUE: 'true';
BOOL: (FALSE | TRUE);

// *--------Float--------
fragment DECIMAL:  DIGIT+;
fragment EXPONENT: ('e'|'E') ('+'|'-')? DIGIT+;
FLO:  ((POSINT | ZERO)+ DOT DECIMAL EXPONENT?
		| (POSINT | ZERO)+ EXPONENT (DOT  DECIMAL)?){self.text = self.text.replace('_','')};

// *--------Integer--------
fragment POSINT: [1-9] (UNDE DIGIT | DIGIT)*;
INT: (POSINT | ZERO){self.text = self.text.replace('_','')} ;
DEMENTION: INT COMA DEMENTION | INT;

// *--------Identifier--------
fragment DIGIT: [0-9];
fragment LETTER: ([a-z] | [A-Z]);
ID: (LETTER | UNDE) (LETTER | UNDE | DIGIT)*;


//*--------Seprator--------
COMA: ',';
COL: ':';
SEM: ';';
DOT: '.';
LSB: '[';
RSB: ']';
LB: '(';
RB: ')';
LCB: '{';
RCB: '}';
EQU:'=';

// *--------Array--------
fragment EXPR: STR|FLO|INT|ID;
fragment EXPRESSTIONS: EXPR COMA EXPRESSTIONS | EXPR ;
ARR: LCB EXPRESSTIONS RCB{self.text = self.text.replace(' ','')};


// *--------Tokens--------
DB: '"';
ZERO: '0';
UNDE: '_';
PLUS: '+';
MINU: '-';
MUTI: '*';
DIVI: '/';
MODU: '%';
NOT: '!'; 
// *--------Operator--------
AND: '&&';
OR: '||';
EQUL: '==';
NEQ: '!=';
LESS: '<';
LOEQ: '<=';
GREA: '>';
GOEQ: '>=';
SCOPE: '::';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: DB (ESCAPE|~["\r\n])* {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: .;