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
   |   NUM                                  # numberExpr
   ;

NUM :   [0-1]+;
WS  :   [ \t\r\n] -> skip;