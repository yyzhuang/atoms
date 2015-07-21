import atoms_of_confusion_API

# This test demonstrates the proper use of the atoms_of_confusion clas
# to add the indentation atom of confusion
print('======Unit Test 1======')

sampleprogramtext = ['double a = 1;']

# create a new instance of the atoms_of_confusion clas with the sample program text
atoms_of_confusionClass = atoms_of_confusion_API.atoms_of_confusion(sampleprogramtext)

# print out the original program text
atoms_of_confusionClass.printprogram()

# add the atom of confusion
try:
  atoms_of_confusionClass.convert_TYPE_atom(0)
  atoms_of_confusionClass.printprogram()
except ValueError as e:
  print "there was an error!", str(e)


print('======Unit Test 2======')

sampleprogramtext = ['  double a;', '  a = 1;']

# create a new instance of the atoms_of_confusion clas with the sample program text
atoms_of_confusionClass = atoms_of_confusion_API.atoms_of_confusion(sampleprogramtext)

# print out the original program text
atoms_of_confusionClass.printprogram()

# add the atom of confusion
try:
  atoms_of_confusionClass.convert_TYPE_atom(1)
  atoms_of_confusionClass.printprogram()
except ValueError as e:
  print "there was an error!", str(e)


print('======Unit Test 3======')

sampleprogramtext = ['  double m, a, n;', '  a = 1;']

# create a new instance of the atoms_of_confusion clas with the sample program text
atoms_of_confusionClass = atoms_of_confusion_API.atoms_of_confusion(sampleprogramtext)

# print out the original program text
atoms_of_confusionClass.printprogram()

# add the atom of confusion
try:
  atoms_of_confusionClass.convert_TYPE_atom(1)
  atoms_of_confusionClass.printprogram()
except ValueError as e:
  print "there was an error!", str(e)


print('======Unit Test 4======')

sampleprogramtext = ['  int m, n;', '  double b, a;', '  a = 1;']

# create a new instance of the atoms_of_confusion clas with the sample program text
atoms_of_confusionClass = atoms_of_confusion_API.atoms_of_confusion(sampleprogramtext)

# print out the original program text
atoms_of_confusionClass.printprogram()

# add the atom of confusion
try:
  atoms_of_confusionClass.convert_TYPE_atom(2)
  atoms_of_confusionClass.printprogram()
except ValueError as e:
  print "there was an error!", str(e)
