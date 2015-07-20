import atoms_of_confusion_API

# This test demonstrates the proper use of the atoms_of_confusion clas
# to add the indentation atom of confusion
print('======Unit Test 1======')

sampleprogramtext = ['if ( a == 2/3)', '  printf("a=%.3f", a);']

# create a new instance of the atoms_of_confusion clas with the sample program text
atoms_of_confusionClass = atoms_of_confusion_API.atoms_of_confusion(sampleprogramtext)

# print out the original program text
atoms_of_confusionClass.printprogram()

# add the atom of confusion
try:
  atoms_of_confusionClass.arithmetic_TYPE_atom(0)
  atoms_of_confusionClass.printprogram()
except ValueError:
  print "there was an error!"


print('\n\n======Unit Test 2======')

# This contains the program
# for (int i = 0; i < 2/3; i++) {
#   printf("a=%.3f", a);
# }
sampleprogramtext = ['for (int i = 0; i < 2/3; i++) {', '  printf("a=%.3f", a);', '}']

# create a new instance of the atoms_of_confusion clas with the sample program text
atoms_of_confusionClass = atoms_of_confusion_API.atoms_of_confusion(sampleprogramtext)

# print out the original program text
atoms_of_confusionClass.printprogram()

# add the atom of confusion
try:
  atoms_of_confusionClass.arithmetic_TYPE_atom(0)
  atoms_of_confusionClass.printprogram()
except ValueError:
  print "there was an error!"


print('\n\n======Unit Test 3======')

# This contains the program
# double a = 2/3;
sampleprogramtext = ['double a = 2/3;']

# create a new instance of the atoms_of_confusion clas with the sample program text
atoms_of_confusionClass = atoms_of_confusion_API.atoms_of_confusion(sampleprogramtext)

# print out the original program text
atoms_of_confusionClass.printprogram()

# add the atom of confusion
try:
  atoms_of_confusionClass.arithmetic_TYPE_atom(0)
  atoms_of_confusionClass.printprogram()
except ValueError as e:
  print "there was an error!", str(e)


print('\n\n======Unit Test 4======')

# This contains the program
# double a = 2/3;
sampleprogramtext = ['double a = 2.5/3;']

# create a new instance of the atoms_of_confusion clas with the sample program text
atoms_of_confusionClass = atoms_of_confusion_API.atoms_of_confusion(sampleprogramtext)

# print out the original program text
atoms_of_confusionClass.printprogram()

# add the atom of confusion
try:
  atoms_of_confusionClass.arithmetic_TYPE_atom(0)
  atoms_of_confusionClass.printprogram()
except ValueError as e:
  print "there was an error!", str(e)
