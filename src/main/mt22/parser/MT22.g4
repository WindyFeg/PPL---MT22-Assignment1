grammar MT22;

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
// COMMENT: '/*' (~[]) '*/';
COMMENT_C : '/*' .*? '*/' -> skip ;
COMMENT_CPP : '//' ~[\r\n]* -> skip ;

// 3.3 Identifier
IDENTIFIER: (LETTER | '_') (LETTER | '_' | DIGIT)*;

// 3.4 Keywords
// All keyword on the fragment below

// 3.5 Operator
OPERATOR: '+' | '-' | '*' | '/' | '%' | '!' | '&&' | '||' | '==' | '!=' | '<' | '<=' | '>' | '>=' | '::';

// 3.6 Seperators
SEPERATOR: '(' | ')' | '[' | ']' | '.' | ',' | ';' | ':' | '=' | '{' | '}';
// 3.7 Literals
// INTEGER FLOAT BOOLEAN STRING ARRAY

INT: ([1-9] (UNDERLINE DIGIT | DIGIT)* | ZERO ' '){
 	self.text = self.text.replace('_','').replace(' ','')
} ;

FLOAT:  INT '.' DECIMAL EXPONENT?
		| INT EXPONENT '.'  DECIMAL
		| INT '.' DECIMAL EXPONENT;

BOOLEAN: 'true' | 'false';

// STRING:;




//Basic fragment
fragment DECIMAL:  DIGIT+;

fragment EXPONENT: ('e'|'E') ('+'|'-')? DIGIT+;

fragment LETTER: ([a-z] | [A-Z]);

fragment DIGIT: [0-9];

fragment KEYWORD: 'auto' | 'break' | 'boolean' | 'do' | 'else' | 'false' | 'float' | 'for' | 'function' | 'if' | 'integer' | 'return' | 'string' | 'true' | 'while' | 'void' | 'out' | 'continue' | 'of' | 'inherit' | 'array' ;

fragment ZERO: '0';
fragment UNDERLINE: '_';

WS : [ \t\b\f\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: .{raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: .{raise ErrorToken(self.text)};