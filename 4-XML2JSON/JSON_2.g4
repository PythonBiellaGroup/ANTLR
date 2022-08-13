grammar JSON;

​json:   object
​    |   array
​    ;

object
    :   ​'{'​ pair (​','​ pair)* ​'}'​
​    |   ​'{'​ ​'}'​ ​// empty object​
​    ;

​ pair
    :   STRING ​':'​ value ;