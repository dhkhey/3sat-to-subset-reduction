SAT = [['x','~y','z'], ['x', 'y', '~z'], ['~x', '~y', 'z'], ['~x', 'y', '~z']]

#SAT = [['x','y','z'], ['x','~y','z'], ['x','y','~z'], ['x','~y','~z'], ['~x','y','z'],
#['~x','y','~z'], ['~x','~y','z'], ['~x','~y','~z']] #THIS IS UNSATISFIABLE

numOfClauses = len(SAT)
targetNumLen = numOfClauses + 3

equation = ''
for subset in SAT:
	equation += '(' + subset[0] + '∨' + subset[1] + '∨' + subset[2] + ')'
	equation += '∧'
equation = equation[:-1]

print(f'3-SAT equation: {equation}')
print(f'\n*****Performing reduction: 3-SAT ≤𝑝 SUBSET-SUM*****\n')

print(f'Reduced to the following SUBSET-SUM problem:')

clauseDigits = 0
for i in range(numOfClauses):
	clauseDigits += 4*10**i

variableDigits = 0
for i in range(numOfClauses, targetNumLen):
	variableDigits += 10**i

targetNum = variableDigits + clauseDigits
print(f'targetNum = {targetNum}')

clauseInt = []
for i in range(numOfClauses):
	clauseInt.append(2*10**i)
	clauseInt.append(10**i)
	
#print(f'clauseInt = {clauseInt}')

varDigitOfVarInt = []
for i in range(numOfClauses, targetNumLen):
	varDigitOfVarInt += 2*[(10**i)]

	
clauseDigitOfVarInt = []

def findClauseDigitsOfVarInt(VarName):
	varIntCount = 0
	inverseCount = 0
	inverse = "~" + VarName
	for i in range(numOfClauses):
		if VarName in SAT[i]:
			varIntCount += 10**(numOfClauses - i - 1)
		elif inverse in SAT[i]:
			inverseCount += 10**(numOfClauses - i - 1)
	clauseDigitOfVarInt.append(inverseCount)
	clauseDigitOfVarInt.append(varIntCount)

findClauseDigitsOfVarInt('z')
findClauseDigitsOfVarInt('y')
findClauseDigitsOfVarInt('x')


varInt = [x+y for x,y in zip(clauseDigitOfVarInt, varDigitOfVarInt)]
#print(f'var int = {varInt}')

problemSet = varInt + clauseInt

print(f'Set = {problemSet}')

lenOfproblemSet = len(problemSet)


def findSubset(problemSet, targetNum):
    result = []
    def find(problemSet, targetNum, path=()):
        if not problemSet:
            return
        if problemSet[0] == targetNum:
            result.append(path + (problemSet[0],))
        else:
            find(problemSet[1:], targetNum - problemSet[0], path + (problemSet[0],))
            find(problemSet[1:], targetNum, path)
    find(problemSet, targetNum)
    return result

result = findSubset(problemSet, targetNum)
if not result: #if result is empty
	print()
	print("***This SUBSET-SUM is UNSATISFIABLE. Therefore, 3-SAT is also UNSATISFIABLE***")
else:
	print()
	print(f'***This SUBSET-SUM is SATISFIABLE. Therefore, 3-SAT is also SATISFIABLE***')
	print()
	print(f'All subsets whose elements sum to {targetNum}:')
	print()
	a = 1
	for subset in result:
		print(f'subset{a}:{list(subset)}')
		if subset[0] == problemSet[0]:
			z = 0
		else:
			z = 1
		if subset[1] == problemSet[2]:
			y = 0
		else:
			y = 1
		if subset[2] == problemSet[4]:
			x = 0
		else:
			x = 1
		a += 1
		print(f'	Corresponding satisfying conditions of 3-SAT: x = {x}, y = {y}, z = {z}')
		print()
