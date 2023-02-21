/**
 * Student name:
 * Student ID:
 */
grammar BKOOL;

@lexer::header{
	package bkool.parser;
}

@parser::header{
	package bkool.parser;
}

options{
	language=Java;
}
 
 
//		2.1
program: classDecl+;      // match keyword hello followed by an identifier
classDecl:CLASS ID (EXTENDS ID)? LEFT_PARENTHESIS listmember* RIGHT_PARENTHESIS;

listmember: attribute | methodDecl;

attribute:STATIC?  listID COLON type SEMI_COLON 
		 |STATIC?  FINAL type ID EQUAL_OP_2  expression SEMI_COLON
		 ;

declare1 : constDeclare|varDeclare;

declare:constDeclare|varDeclare;

//indexExpression:;
type: type1 (LEFT_SQUARE_BRACKET INTEGER_LIT RIGHT_SQUARE_BRACKET)?; // ?expression

type1: INTEGER
		|FLOAT 
		|STRING 
		|BOOL	
		|ID		
		|VOID   
		;	

//		2.2
constDeclare: STATIC?  FINAL type ID EQUAL_OP_2  expression SEMI_COLON ; // ?type

//		2.3
varDeclare: STATIC?  listID COLON type SEMI_COLON;
listID: ID (COMMA ID)*;

//		2.4 
methodDecl: type? STATIC? ID LEFT_BRACKET listparameter? RIGHT_BRACKET block_stmt;
listparameter: listpara_member (SEMI_COLON listpara_member)*;    //////////////////////// Sai test foo(3,3,)

listpara_member:listID COLON type ;

/* 
expression_static:		
			| <assoc=right> (ADD_OP|SUB_OP) expression_static 
			| <assoc=right> NOT_OP expression_static
			| expression_static CONCAT_OP expression_static
			| expression_static (INT_DIV_OP| MOD_OP|FLOAT_DIV_OP|MUL_OP) expression_static
			| expression_static (ADD_OP|SUB_OP) expression_static
			| expression_static (AND_OP|OR_OP) expression_static
			| expression_static (EQUAL_OP|NOT_EQUAL_OP) expression_static
			| expression_static  (LESS_OP|GREATER_OP|LESS_EQUAL_OP|GREATER_EQUAL_OP) expression_static
			| FLOAT_LIT| INTEGER_LIT| STRING_LIT|CHARACTER|TRUE|FALSE | '('expression_static')'
		; ///type = Integer|float|string
*/
expression: expression2 (LESS_OP|GREATER_OP|LESS_EQUAL_OP|GREATER_EQUAL_OP) expression2
			|expression2;
expression2:  expression1 (EQUAL_OP|NOT_EQUAL_OP) expression1
			|expression1;

expression1: <assoc=right> NEW ID '('list_expression?')' # newExpr // ID? 
			| expression1 DOT ID ('('list_expression?')') # callExpr1
			//| SELF DOT ID ('('list_expression?')')  # callExpr2
			| expression1 DOT ID					# FieldAccess1
			//|	SELF DOT ID ('('list_expression?')')?	
			| expression1 LEFT_SQUARE_BRACKET expression1  RIGHT_SQUARE_BRACKET  # ArrayCell
			| <assoc=right> (ADD_OP|SUB_OP) expression1							 # Unary1
			| <assoc=right> NOT_OP expression1									 # Unary2
			| expression1 CONCAT_OP expression1									 # Binary1
			| expression1 (INT_DIV_OP| MOD_OP|FLOAT_DIV_OP|MUL_OP) expression1   # Binary2
			| expression1 (ADD_OP|SUB_OP) expression1						 # Binary3
			| expression1 (AND_OP|OR_OP) expression1						 # Binary4
			|fact                                                            # fact1               //////////////   ?????????????
			;
fact: FLOAT_LIT| INTEGER_LIT| STRING_LIT|ID |SELF|TRUE|FALSE|NULL| '('expression')';
		
list_expression:<assoc=right> expression (COMMA  expression)*;


/////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* 
expression:relation_expr2;
relation_expr2:<assoc=none>  relation_expr2 (LESS_OP|GREATER_OP|LESS_EQUAL_OP|GREATER_EQUAL_OP)relation_expr2
				|relation_type1
				|relation_expr1;
relation_type2:INTEGER|FLOAT_LIT|ID|'('expression')';

relation_expr1: <assoc=none> relation_expr1 (EQUAL_OP|NOT_EQUAL_OP) relation_expr1
				|relation_type1
				|bool_expr;
				
relation_type1:INTEGER_LIT|STRING_LIT|FLOAT_LIT|CHARACTER|TRUE|FALSE|ID;

bool_expr:<assoc=left> bool_expr (AND_OP|OR_OP) bool_expr
			|bool_type
			|binary3_expr;
bool_type:TRUE|FALSE|ID;

binary3_expr:<assoc=left> binary3_expr (ADD_OP|SUB_OP) binary3_expr
			|binary2_type
			|binary2_expr;

binary2_expr:<assoc=left> binary2_expr (FLOAT_DIV_OP|MUL_OP) binary2_expr
			|binary2_type
			| binary3_expr;
binary2_type:INTEGER_LIT|FLOAT_LIT|ID;

binary1_expr:<assoc=left> binary1_expr (INT_DIV_OP| MOD_OP) binary1_expr
			|binary1_type
			| string_expr;
binary1_type:INTEGER_LIT|ID;

string_expr:<assoc=left> string_expr CONCAT_OP string_expr
			|not_expr;
			
not_expr:<assoc=right> NOT_OP not_expr
		|bool_type
		|unary_expr;

unary_expr:<assoc=right> (ADD_OP|SUB_OP) unary_expr
			//|arith_type
			|index_expr;
arith_type:INTEGER_LIT|FLOAT_LIT|ID;

index_expr:<assoc=left> (ID|'('expression')') LEFT_SQUARE_BRACKET expression  RIGHT_SQUARE_BRACKET
			|access_member;
expression_array:access_member|index_expr|string_expr;
expression_integer:binary1_expr;

access_member:  <assoc=left> (SELF|'('expression')'|ID) DOT ID ('('list_expression')')?
				|create_object ; 
expression_object:string_expr|index_expr|access_member;

create_object: NEW ID '('list_expression')'
			| access_member
			|'('expression')';
list_expression:<assoc=right> list_expression COMMA list_expression|expression?;
*/
///////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////
 /* 
expression:create_object;

create_object: NEW ID '('list_expression')'
			| access_member;
list_expression:<assoc=right> list_expression COMMA list_expression|expression?;
 
access_member:  <assoc=left> (SELF|ID) DOT ID (access_member)? 
				|<assoc=left>access_member DOT ID (access_member)?
				|index_expr ; 
expression_object:string_expr|index_expr|access_member;

index_expr:<assoc=left> ID LEFT_SQUARE_BRACKET index_expr  RIGHT_SQUARE_BRACKET
			|<assoc=left> index_expr LEFT_SQUARE_BRACKET index_expr  RIGHT_SQUARE_BRACKET
			|unary_expr;
expression_array:access_member|index_expr|string_expr;
expression_integer:binary1_expr;

unary_expr:<assoc=right> (ADD_OP|SUB_OP) unary_expr
			|not_expr
			|arith_type;
arith_type:INTEGER_LIT|FLOAT_LIT|ID;

not_expr:<assoc=right> NOT_OP not_expr
		|string_expr
		|bool_type;
bool_type:TRUE|FALSE|ID;

string_expr: string_expr CONCAT_OP string_expr
			|binary1_expr;

binary1_expr: binary1_expr (INT_DIV_OP| MOD_OP) binary1_expr
			| binary2_expr
			|binary1_type;
binary1_type:INTEGER_LIT|ID;

binary2_expr:binary2_expr (FLOAT_DIV_OP|MUL_OP) binary2_expr
			| binary3_expr
			|binary2_type;
binary2_type:INTEGER_LIT|FLOAT_LIT|ID;

binary3_expr:binary3_expr (ADD_OP|SUB_OP) binary3_expr
			| bool_expr
			|binary2_type;
			

bool_expr: bool_expr (AND_OP|OR_OP)bool_expr
			|relation_expr1
			|bool_type;

relation_expr1: <assoc=none> relation_expr1 (EQUAL_OP|NOT_EQUAL_OP) relation_expr1
				|relation_expr2
				|relation_type1;
relation_type1:INTEGER_LIT|STRING_LIT|FLOAT_LIT|CHARACTER|TRUE|FALSE|ID;

relation_expr2:<assoc=none>  relation_expr2 (LESS_OP|GREATER_OP|LESS_EQUAL_OP|GREATER_EQUAL_OP)relation_expr2
				|relation_type2;
relation_type2:INTEGER|FLOAT_LIT|ID|'('expression')';
				
*/
///////////////////////////////////////////////////////////////////////////////////////



/////////////////////////////////////////////////////////////////////////////////////
/* 		5.1
ari_expr: (ADD_OP|SUB_OP)? aex1| aex1 (ADD_OP|SUB_OP) aex1;
aex1: aex2 (INT_DIV_OP| MOD_OP) aex2  | aex3 (FLOAT_DIV_OP|MUL_OP) aex3 ;
aex2: '('expression')'|ari_type2;
aex3: '('expression')'|ari_type1;
ari_type1: INTEGER_LIT|FLOAT_LIT|ID;
ari_type2: INTEGER_LIT|ID;


		5.2
bool_type: ID|TRUE|FALSE;
bool_expr:bex1 (AND_OP|OR_OP) bex1|bex1;
bex1: NOT_OP bex2|bex2;
bex2:'(' expression ')'|bool_type;

//		5.3????????????????????????????????????
rel_expr1: rexp1 (EQUAL_OP|NOT_EQUAL_OP) rexp1|rexp1;
rel_expr2: rexp2 (LESS_OP|GREATER_OP|LESS_EQUAL_OP|GREATER_EQUAL_OP)rexp2|rexp2;
rexp:TRUE|FALSE;
rexp1:'(' expression ')'|rexp;///???????????????
rexp2:'('expression')'|rexp;///////////?????????????????????????????

//		5.4
string_expr:<assoc=left>sexp1 CONCAT_OP sexp1|sexp1;
sexp1: '('expression')'|STRING_LIT;

// 		5.5
index_expr: (ID|member_acess) LEFT_SQUARE_BRACKET expression  RIGHT_SQUARE_BRACKET;

// 		5.6 ?????????????????????????
member_acess: (expression_object|SELF|ID) DOT ID list_expression?;
expression_object:string_expr|index_expr;



//		5.7
create_object: NEW ID '('list_expression')';


// 		5.8 SELF
///////////////////////////////////////////////////////////////////////////////////////////
*/


////////////
stmt:assign_stmt|if_stmt|while_stmt|break_stmt|continue_stmt|return_stmt|block_stmt|invocation_stmt;

//		6.1


block_stmt:LEFT_PARENTHESIS declare* stmt* RIGHT_PARENTHESIS; // co sua  (declare| stmt)*
 
//		6.2
assign_stmt: expression ASS_OP expression SEMI_COLON;

//		6.3
if_stmt: IF expression THEN stmt (ELSE stmt)?;

//		6.4
while_stmt: WHILE expression DO stmt;

//		6.5
break_stmt:BREAK SEMI_COLON;

//		6.6
continue_stmt: CONTINUE SEMI_COLON;

//		6.7
return_stmt:	RETURN expression SEMI_COLON;

//		6.8
invocation_stmt:expression DOT ID LEFT_BRACKET list_expression? RIGHT_BRACKET SEMI_COLON;
				//| SELF DOT ID LEFT_BRACKET list_expression? RIGHT_BRACKET SEMI_COLON;

 /* 
p1: (p1 '||' p2) |p2;
 p2: (p3 '==' p3)| p3; 
 p3: ('!'p3) | p4; 
 p4: '(' p1 ')' | ID; 
*/

 
///////////////////////////////////////////////////////////////////////////////////
//LP: '{';

///////////////////////////////		Phase1               /////////////////////////////

//			3.2 Con sai
COMMENTS: (('(*'(.)*?'*)')|('#'(~[\n\r])*[\n\r])) -> skip ; // da them \r o [\n]
//COMMENTS2: (('(*'~[*)]*'*)')|('#'(~[\n\r])*[\n\r])) -> skip ;
//fragment COMMENT_TRY: (('(*'.*('*)'|EOF))|('#'.*[\n])) -> skip ;
//COMMENT:'[*'(~[*\]])*? EOF;


//  		3.1
CHARACTER:'\''('\\t'|'\\n'|'\\f'|'\\r'|(~[\t\n\f\r]))'\'';

//			3.4
 BOOL:'bool';
BREAK:'break';
 CLASS: 'class';
 CONTINUE:'continue';
 DO:'do';
 ELSE:'else';
 EXTENDS:'extends';
 FLOAT:'float';
 IF:'if';
 INTEGER:'integer';
 NEW:'new';
 STRING:'string';
 THEN:'then';
 WHILE:'while';
 RETURN:'return';
 TRUE:'true';
 FALSE:'false';
 VOID:'void';
 NULL:'null';
 SELF:'self';
 FINAL:'final';
 STATIC:'static';
KEYWORDS: BOOL | BREAK | CLASS | CONTINUE | DO | ELSE |EXTENDS | FLOAT | IF | INTEGER | NEW | STRING |THEN | WHILE | RETURN | TRUE | FALSE | VOID | NULL | SELF  | FINAL | STATIC;

//			3.3
ID : ([a-zA-Z]|'_')([a-zA-Z0-9]|'_')* ;             // match lower-case identifiers

//			3.5
 ASS_OP: ':=';
 ADD_OP:'+';
 SUB_OP:'-';
 MUL_OP:'*';
 FLOAT_DIV_OP:'/';
INT_DIV_OP:'\\';
 MOD_OP:'%';
 NOT_EQUAL_OP:'<>';
 EQUAL_OP:'==';
 EQUAL_OP_2:'=';
 LESS_OP:'<';
 GREATER_OP: '>';
 LESS_EQUAL_OP:'<=';
GREATER_EQUAL_OP:'>=';
OR_OP:'||';
 AND_OP:'&&';
 NOT_OP:'!';
 CONCAT_OP:'^';
//fragment NEW_OP:'new';

OPERATOR: ASS_OP| ADD_OP| SUB_OP | MUL_OP |FLOAT_DIV_OP|INT_DIV_OP|MOD_OP|NOT_EQUAL_OP|EQUAL_OP|EQUAL_OP_2|LESS_OP|GREATER_OP|LESS_EQUAL_OP|GREATER_EQUAL_OP|OR_OP|AND_OP|NOT_OP|CONCAT_OP; // bay cho dau =

//			3.6
 LEFT_SQUARE_BRACKET:'[';
 RIGHT_SQUARE_BRACKET:']';
LEFT_BRACKET:'(';
RIGHT_BRACKET:')';
 COMMA:',';
 DOT:'.';
 COLON:':';
 SEMI_COLON:';';
 LEFT_PARENTHESIS:'{';
 RIGHT_PARENTHESIS:'}';
SEPARATOR: LEFT_SQUARE_BRACKET|RIGHT_SQUARE_BRACKET|LEFT_BRACKET|RIGHT_BRACKET|COMMA|SEMI_COLON|DOT|COLON|LEFT_PARENTHESIS|RIGHT_PARENTHESIS;

//			3.7.2
FLOAT_LIT: [0-9]+(('.'[0-9]*)|(('.'[0-9]*)?(('E'|'e')('+'|'-')?[0-9]+)));

//			3.7.1
INTEGER_LIT:[0-9]+;

//			3.7.3
//BOOLEAN : 'true'|'false';

fragment UNCLOSE_STRING:'"'('\\\\'|'\\t'|'\\"'|'\\n'|'\\f'|'\\r'|'\\b'|(~[\\\\\t\"\n\f\r\b\n]))*;
ERROR_UNCLOSE_STRING: (UNCLOSE_STRING){if(true) throw new bkool.parser.UncloseString(getText());};

fragment ESCAPE_STRING: '"'('\\\\'|'\\t'|'\\"'|'\\n'|'\\f'|'\\r'|'\\b'|(~[\\\\\t\"\n\f\r\b]))*'\\'(~[\\\\\t\"\n\f\r\b]);
ERROR_ESCAPE_STRING: (ESCAPE_STRING){if(true) throw new bkool.parser.IllegalEscape(getText());};

//			3.7.4
STRING_LIT:'"'('\\\\'|'\\t'|'\\"'|'\\n'|'\\f'|'\\r'|'\\b'|(~[\\\\\t\"\n\f\r\b]))*'"' ;

//RP: '}';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

////////////////////////////////////////////////////////////
fragment CHARACTER_ERROR: ~[COMMENTS STRING_LIT CHARACTER FLOAT_LIT INTEGER_LIT RP LP KEYWORDS ID OPERATOR SEPARATOR];
fragment CHARACTER_ERROR2:'?'|'\''|'@'|'$'|'`'| '&' |'|'|'~';
ERROR_TOKEN :(.){if(true) throw new bkool.parser.ErrorToken(getText());};

///////////////////////////////////////////// END Phase1 ///////////////////////////////////////////////////////////////////////////////