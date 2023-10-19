# Conditional Statements (if, elif, else)

"""
operators

seen already =,+,-,/,*,%

type of operators

Comparison operators
------------------------------
Operator:==  name:equals  def:see if if to values are equal ex: "yes" == "yEs"
Operator:!=  name:not equals  def:see if if to values are not equal ex: "yes" != "yEs"

Operator: <  name:Greater than  def:- ex: 1 < 2
Operator: >  name:Greater less  def:- ex: 1 > 2

Operator: >=  name:Greater than or equal to  def:- ex: 1 >= 2
Operator: <=  name:Less than or equal to  def:- ex: 1 <= 2


Logical Operators

var1 is 1
var2 is 1
var3 is 2
------------------------------
and - return true if both values are true - var1 == var1 and var1 == var3

or -  if one of the statements is true =  var1 == var1 and var1 == var3

not - Reverse the result -  not(1 > 2)

"""

var1 = 1
var2 = 1
var3 = 2

if var1 == var1 and var1 == var3:
    print("statement is true")
    
if var1 == var1 or var1 == var3:
    print("statement is true")
    
if not(var1 == var1 and var1 == var3):
    print("statement is true")