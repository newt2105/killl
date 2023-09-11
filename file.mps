* ENCODING=ISO-8859-1
NAME          test.lp
ROWS
 N  obj1       
 L  Constraint1
 G  Constraint2
COLUMNS
    x            obj1                              -3
    x            Constraint1                        1
    x            Constraint2                        2
    MARK0000  'MARKER'                 'INTORG'
    y            obj1                              -2
    y            Constraint1                        2
    y            Constraint2                       -1
    MARK0001  'MARKER'                 'INTEND'
RHS
    rhs          Constraint1                        5
    rhs          Constraint2                        3
BOUNDS
 UP bnd          x                                 10
 LI bnd          y            0
ENDATA
