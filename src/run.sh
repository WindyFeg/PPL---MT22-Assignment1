echo "Generatting..."
py run.py gen

echo "Testing Lexer..."
py run.py test LexerSuite

echo "Testing Parser..."
py run.py test ParserSuite