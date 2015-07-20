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

      

  # apply the type conversion atom to the program...
  def arithmetic_TYPE_atom(self, linenumber):
    # Validate arguments...
    assert(type(linenumber) is int or type(linenumber) is long)
    if linenumber < 0:
      raise ValueError("TypeAtom requires a positive line number")

    if linenumber >= len(self.programtextlist):
      raise ValueError("TypeAtom requires a line number (" + str(linenumber) 
            + ") less than the number of lines in the file (" + str(len(self.programtextlist)) + ")")

    programline = self.programtextlist[linenumber]

    # in case where "if (a == 2 + 3) {" or "else if (a == 2 + 3) {"
    keywords = ['if', 'else', 'else if', 'for', 'while']
    for keyword in keywords:
      if keyword in programline:
        programline = re.sub(keyword, '', programline)

    # assume: each line has only one such experssion, not "var1 = 1 + 2; var2 = 2 + 3;"
    comparelist = ['=', '==', '>', '<', '>=', '<=', '<>', '!=']    
    variablelist = []

    for operator in comparelist:
      if operator in programline:
        # lines like "var = 2 + 3;", "var == 2 + 3" or "var > 2 + 3;"
        # first remove spaces and get "var==2+3"
        programline = programline.replace(' ', '')

        # split to get var, and 2+3. filter(None, list) removes '' from list
        variable, expression = filter(None, re.split(operator, programline))
        
        # remove math operators: "[-(){}+*/;]" will not appear in variablelist
        variablelist = filter(None, re.split("[-(){}+*/;]", expression))

    variabletype = []
    for variable in variablelist:
      variable = int_or_float(variable)
      typeofvariable = type(variable)
      if typeofvariable is str:
        raise ValueError("TypeAtom currently do not handle dynamic types.")
      variabletype.append(typeofvariable)

    if variabletype[1:] == variabletype[:-1]:
      # all variable types are identical
      raise ValueError("TypeAtom requires implicit type conversion.")
    else:
      # some variable types are different
      print "There is an implicit type conversion."
      return variabletype

    
def int_or_float(number):
  try:
    return int(number)
  except ValueError:
    return float(number)
