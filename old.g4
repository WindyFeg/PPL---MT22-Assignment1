grammar old;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;

// 3.1 Character set (White Space on the bottom)
NEWLINE: '\n';

// 3.2 Program comment
COMMENT_C : '/*' .*? '*/' -> skip ;
COMMENT_CPP : '//' ~[\r\n]* -> skip ;

// 3.3 Identifier

// 3.4 Keywords

// 3.5 Operator
OPERATOR: '+' | '-' | '*' | '/' | '%' | '!' | '&&' | '||' | '==' | '!=' | '<' | '<=' | '>' | '>=' | '::';

// 3.6 Seperators
// 3.7 Literals
// INTEGER FLOAT BOOLEAN STRING ARRAY

FLOAT:  ((POSINT | ZERO)+ DOT DECIMAL EXPONENT?
		| (POSINT | ZERO)+ EXPONENT (DOT  DECIMAL)?){self.text = self.text.replace('_','')};

INT: (POSINT | ZERO){self.text = self.text.replace('_','')} ;

BOOLEAN: 'true' | 'false';

IDENTIFIER: (LETTER | '_') (LETTER | '_' | DIGIT)*;

// STRING (Must be the last one for everything work perfectly)
STRING: (DB (ESCAPE|~[\r\n])* DB) {self.text = self.text[1:-1].replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')};

//ARRAY
// ARRAY:LCB (INT | ',')* RCB;



SEPERATOR: (LB | RB | LSB | RSB | DOT | COM | SEM | COL | EQU | LCB | RCB);

//Basic fragment
ESCAPE: '\\' ( 'b' | 'f' | 'n' | 'r' | 't' | '\'' | DB | '\\' );
COM: ',';
COL: ':';
EQU: '=';
SEM: ';';
DOT: '.';
LSB: '[';
RSB: ']';
LB: '(';
RB: ')';
LCB: '{';
RCB: '}';
DB: '"';
ZERO: '0';
UNDERLINE: '_';
fragment POSINT: [1-9] (UNDERLINE DIGIT | DIGIT)*;
fragment DECIMAL:  DIGIT+;
fragment EXPONENT: ('e'|'E') ('+'|'-')? DIGIT+;
fragment LETTER: ([a-z] | [A-Z]);
fragment DIGIT: [0-9];

fragment KEYWORD: ('auto' | 'break' | 'boolean' | 'do' | 'else' | 'false' | 'float' | 'for' | 'function' | 'if' | 'integer' | 'return' | 'string' | 'true' | 'while' | 'void' | 'out' | 'continue' | 'of' | 'inherit' | 'array') ;

WS : [ \t\b\f\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: DB ~[\r\n]* {raise UncloseString(self.text[1:])};
// ILLEGAL_NUMBER: '0' DECIMAL+{raise IllegalNumber(self.text)};
ILLEGAL_ESCAPE: .;