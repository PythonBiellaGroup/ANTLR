grammar JSON;

​json:   object
​    |   array
​    ;

object
    :   ​'{'​ pair (​','​ pair)* ​'}'​
​    |   ​'{'​ ​'}'​ ​// empty object​
​    ;

array
    :   ​'['​ value (​','​ value)* ​']'​
    |   ​'['​ ​']'​ ​// empty array​
    ;

pair
    :   STRING ​':'​ value ;

value
    :   STRING
    |   NUMBER
    |   object  ​// recursion​
    |   array   ​// recursion​
    |   ​'true'​  ​// keywords​
    |   ​'false'​
    |   ​'null'​
    ;