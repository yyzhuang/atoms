import random
import string
import re

# This class is used to store a program so that we can apply or remove
# atoms of confusion.  
class atoms_of_confusion:
  
  # This contains the program itself
  # the format of this is [line0, line1, line2] so that this program:
  # """ Hello world"""
  # print 'hi'
  # 
  # is represented as: ['""" Hello world"""', "print 'hi'"]
  programtextlist = []
  
  def __init__(self, thisprogram):
    # do type checking to error earlier rather than later...
    assert(type(thisprogram) is list)
    for line in thisprogram:
      assert(type(line) is str)

    self.programtextlist = thisprogram[:]
    return

  # print the program out so it can be inspected...
  def printprogram(self):
    for programline in self.programtextlist:
      print(programline)

  # return a copy of the program so we can examine it.
  def getprogram(self):
    return self.programtextlist[:]

  # apply the indentation atom to the program...
  def add_INDENTATION_atom(self, linenumber, addspaces):
    # Validate arguments...
    assert(type(linenumber) is int or type(linenumber) is long)
    assert(type(addspaces) is int or type(addspaces) is long)
    if linenumber < 0:
      raise ValueError("IndentationAtom requires a positive line number")

    if linenumber >= len(self.programtextlist):
      raise ValueError("IndentationAtom requires a line number ("+str(linenumber)+") less than the number of lines in the file ("+str(len(self.programtextlist))+")")

    if addspaces==0:
      raise ValueError("IndentationAtom requires a non-zero number of spaces")

    # Okay, now we are ready to go!  Do we add or remove spaces?
    if addspaces > 0:  
      # prepend spaces...
      self.programtextlist[linenumber] = ' '*addspaces + self.programtextlist[linenumber]
    else:
      # remove spaces...
      # double check there are enough spaces to remove...
      if not self.programtextlist[linenumber].startswith(' '*(-addspaces)):
        raise ValueError("IndentationAtom: not enough spaces ("+str(addspaces)+") to remove on line "+str(linenumber))
      # if this is -3, do [3:] so that we cut off the first 3 characters
      self.programtextlist[linenumber] = self.programtextlist[linenumber][-addspaces:]

      

  # apply the arithmetic type conversion atom to the program...
  # this atom occurs when two integers divide each other, e.g., 2/3=0, 3/2=1.
  # note that if either of the operands is float, the resulr will be float: .1/2=.05
  def arithmetic_TYPE_atom(self, linenumber):
    # Validate arguments...
    assert(type(linenumber) is int or type(linenumber) is long)
    if linenumber < 0:
      raise ValueError("ArithmeticTypeAtom requires a positive line number")

    if linenumber >= len(self.programtextlist):
      raise ValueError("ArithmeticTypeAtom requires a line number (" + str(linenumber) 
            + ") less than the number of lines in the file (" + str(len(self.programtextlist)) + ")")

    programline = self.programtextlist[linenumber]
    if '/' not in programline:
      raise ValueError("ArithmeticTypeAtom requires a division operation")

    # currently the code handles simple arithmetic, no compound is handled yet
    # in case where "if (a == 2 / 3) {", "else if (a > 2 / 3) {" or "while (i > 3/2) {"
    keywords = ['if', 'else', 'else if', 'while']
    for keyword in keywords:
      if keyword in programline:
        # split "if (a == 2 / 3) {" into ["if (", "a == 2 / 3", ") {"]
        itemlist = re.split('([()])', programline)
        statementhead, statement, statementtail = itemlist[:2], itemlist[2], itemlist[3:]    
        break
    else:
        if 'for' in programline:
          # split "for (i = 0; i < 2/3; i++) {" into "for (i = 0; ", "i < 2/", "; i++"
          itemlist = re.split('([;])', programline)
          statementhead, statement, statementtail = itemlist[:2], itemlist[2], itemlist[3:]
        else:
          # only statements like "double a = 2/3;"
          itemlist = re.split('([;])', programline)
          statementhead, statement, statementtail = [], itemlist[0], itemlist[1:]

    # assume: each line has only one such experssion, not "var1 = 1 + 2; var2 = 2 + 3;"
    comparelist = ['=', '==', '>', '<', '>=', '<=', '<>', '!=']    
    variablelist = []

    for operator in comparelist:
      if operator in statement:
        # lines like "var = 2 / 3", "var == 2 / 3" or "var > 2 / 3"
        itemlist = re.split('([' + operator + ']+)', statement)
        for item in itemlist:
          if '/' not in item:
            statementhead.append(item)
          else:
            expression = item
            
        expression = expression.replace(' ', '')
        dividend, divisor = expression.split('/')
        break

    dividendtype = type_int_or_float(dividend)
    divisortype = type_int_or_float(divisor)

    if dividendtype is int and divisortype is int:
      line = ''
      for head in statementhead:
        line = line + str(head)
      line = line + ' (int) ' + expression
      for tail in statementtail:
        line = line + str(tail)
    else:
      # if one of the dividend or divisor is float, the result is float
      raise ValueError("There is no ArithmeticTypeAtom!")

    self.programtextlist[linenumber] = line


    
def type_int_or_float(number):
  # number is a string. return the type of number represents
  # if number is '2', then return int
  # if number is '2.0', then return float
  try:
    convertednumber = int(number)
  except ValueError:
    convertednumber = float(number)
    
  return type(convertednumber)
