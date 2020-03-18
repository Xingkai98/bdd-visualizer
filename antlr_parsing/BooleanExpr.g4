grammar BooleanExpr;
compileUnit
    :   expr EOF
    ;
expr
   :   '(' expr ')'                         # parensExpr
   |   '¬' child=expr                       # negationExpr
   |   left=expr '∧' right=expr             # conjunctionExpr
   |   left=expr '∨' right=expr             # disjunctionExpr
   |   left=expr '<=>' right=expr           # biimpExpr
   |   left=expr '=>' right=expr            # impExr
   |   VARIABLE                             # variableExpr
   ;

VARIABLE :   [a-zA-Z]+[a-zA-Z0-9]*;
WS  :   [ \t\r\n] -> skip;