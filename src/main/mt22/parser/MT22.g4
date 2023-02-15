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


FLOAT:  ((POSINT | ZERO)+ '.' DECIMAL EXPONENT?
		| (POSINT | ZERO)+ EXPONENT ('.'  DECIMAL)?){
 	self.text = self.text.replace('_','').replace(' ','')
};

INT: (POSINT | ZERO ' '){
 	self.text = self.text.replace('_','').replace(' ','')
} ;

BOOLEAN: 'true' | 'false';

// STRING
STRING: (DB (ESCAPE|~[\r\n])* DB) {
    self.text = self.text[1:-1].replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')
};

fragment ESCAPE: '\\' ( 'b' | 'f' | 'n' | 'r' | 't' | '\'' | '\"' | '\\' );


//Basic fragment
fragment DB: '"';
fragment ZERO: '0';
fragment UNDERLINE: '_';

fragment POSINT: [1-9] (UNDERLINE DIGIT | DIGIT)*;

fragment DECIMAL:  DIGIT+;

fragment EXPONENT: ('e'|'E') ('+'|'-')? DIGIT+;

fragment LETTER: ([a-z] | [A-Z]);

fragment DIGIT: [0-9];

fragment KEYWORD: 'auto' | 'break' | 'boolean' | 'do' | 'else' | 'false' | 'float' | 'for' | 'function' | 'if' | 'integer' | 'return' | 'string' | 'true' | 'while' | 'void' | 'out' | 'continue' | 'of' | 'inherit' | 'array' ;

WS : [ \t\b\f\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: DB ~[\r\n]* {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: .;