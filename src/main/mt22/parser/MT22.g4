grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (COMMENT_C|COMMENT_CPP|STR|FLO|INT|ID|LCB|COMA|RCB|ARR)* EOF ;



// LEXER RULE
COMMENT_C : '/*' .*? '*/' -> skip ;
COMMENT_CPP : '//' ~[\r\n]* -> skip ;

// string
fragment ESCAPE: '\\' ( 'b' | 'f' | 'n' | 'r' | 't' | '\'' | DB | '\\' );
STR: (DB (ESCAPE|~[\r\n])* DB) {self.text = self.text[1:-1].replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')};

// keyword
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

//boolean
FALSE: 'false';
TRUE: 'true';
BOOL: (FALSE | TRUE);

//float
fragment DECIMAL:  DIGIT+;
fragment EXPONENT: ('e'|'E') ('+'|'-')? DIGIT+;
FLO:  ((POSINT | ZERO)+ DOT DECIMAL EXPONENT?
		| (POSINT | ZERO)+ EXPONENT (DOT  DECIMAL)?){self.text = self.text.replace('_','')};

// integer
fragment POSINT: [1-9] (UNDE DIGIT | DIGIT)*;
INT: (POSINT | ZERO){self.text = self.text.replace('_','')} ;

// identifier
fragment DIGIT: [0-9];
fragment LETTER: ([a-z] | [A-Z]);
ID: (LETTER | UNDE) (LETTER | UNDE | DIGIT)*;


//seprator
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

// array
fragment EXPR: STR|FLO|INT|ID;
ARR: LCB EXPRESSTIONS RCB{self.text = self.text.replace(' ','')};
EXPRESSTIONS: EXPR COMA (' ')* EXPRESSTIONS | EXPR ;

// TOKENS
DB: '"';
ZERO: '0';
UNDE: '_';
PLUS: '+';
MINU: '-';
MUTI: '*';
DIVI: '/';
MODU: '%';
NOT: '!'; 
// operator
AND: '&&';
OR: '||';
EQU: '==';
NEQ: '!=';
LESS: '<';
LOEQ: '<=';
GREA: '>';
GOEQ: '>=';
SCOPE: '::';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;