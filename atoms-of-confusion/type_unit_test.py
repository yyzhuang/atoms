import atoms_of_confusion_API

# This test demonstrates the proper use of the atoms_of_confusion clas
# to add the indentation atom of confusion
print('Unit Test 1')

# This contains the program
# if (foo)
#   goto fail;
# goto fail;
sampleprogramtext = ['if ( a == 2 + 3.0)', '  print a;']

# create a new instance of the atoms_of_confusion clas with the sample program text
atoms_of_confusionClass = atoms_of_confusion_API.atoms_of_confusion(sampleprogramtext)

# print out the original program text
atoms_of_confusionClass.printprogram()

# add the atom of confusion
print atoms_of_confusionClass.arithmetic_TYPE_atom(0)
