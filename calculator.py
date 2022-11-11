"""
Super Calculator! 

Creator: Michael Gharoro
Reason behind creation: The teacher made me to it 😭
So what does it do you might ask? 
Well thank you for asking! This beautiful single threaded calculator can perform many operations on any 2 numbers including
addition, subtraction, logalgorithms, and the (useful) trig functions!
This calculator can also convert between bases 2, 10, and 16—How mythical!
Licence: Do not copy the code, Do not read the code, Do not breathe the code, I am the code 😔

How to use:

1. Install python
2. Run the file
3. Follow the instructions
4. Refer to step 3
5. How'd you get to this step? The previous one should have had you in a loop 😠

Additional Note: This looks funnier in my ide because the emojis have a slight slant to them which makes them look even more stupid

"""
import math
from typing import Any, Literal, Union

#constants!!

#my lovely table of mathematical operations and the arguments they take
#"n" is the number of arguments, "act" is a shorthand for a function which will perform the operation
mathtable = {
    'cvt': {
        'n': 1,
        'act': lambda a: a,
        'alts': ['convert', '~'],
        'info': 'This performs no operation. This would be useful if you are using the calculator only to convert between bases'
    },
    'add': {
        'n': 2,
        'act': lambda a, b: a + b,
        'alts': ['addition', 'plus', '+'],
        'info': 'Performs operation: a + b'
    },
    'sub': {
        'n': 2,
        'act': lambda a, b: a - b,
        'alts': ['subtract', 'subtraction', 'minus', '-'],
        'info': 'Performs operation: a - b'
    },
    'mul': {
        'n': 2,
        'act': lambda a, b: a * b,
        'alts': ['multiply', 'multiplication', 'mult', '*', 'x'],
        'info': 'Performs operation: a x b'
    },
    'div': {
        'n': 2,
        'act': lambda a, b: a / b,
        'alts': ['divide', 'division', '/'],
        'info': 'Performs operation: a / b'
    },
    'exp': {
        'n': 2,
        'act': lambda a, b: a ** b,
        'alts': ['power', 'exponent', 'exponential', '^', '**'],
        'info': 'Performs operation: a ** b'
    },
    'mod': {
        'n': 2,
        'act': lambda a, b: a % b,
        'alts': ['modulus', 'modulo', 'remainder', '%'],
        'info': 'Performs operation: a mod b'
    },
    'sqrt': {
        'n': 1,
        'act': lambda a: math.sqrt(a),
        'alts': ['sqroot', 'squareroot'],
        'info': 'Performs operation: sqrt(a)'
    },
    'nrt': {
        'n': 2,
        'act': lambda a, b: a ** (1 / b),
        'alts': ['nroot', 'root', 'nthroot'],
        'info': 'Performs operation: bth root of a (ex: [a, b] = [27, 3] = the cube root of 27)'
    },
    'log': {
        'n': 2,
        'act': lambda a, b: math.log(a, b),
        'alts': ['logalgorithm', 'logalgorithmic'],
        'info': 'Performs operation: log b, a: (ex: [a, b] = [25, 3] = the log base 3 of 25)'
    },
    'fct': {
        'n': 1,
        'act': lambda a: math.factorial(a),
        'alts': ['factorial', '!'],
        'info': 'Performs operation: a!'
    },
    'rcp': {
        'n': 1,
        'act': lambda a: 1 / a,
        'alts': ['reciprocal'],
        'info': 'Performs operation: 1 / a'
    },
    'inv': {
        'n': 1,
        'act': lambda a: a * -1,
        'alts': ['inverse'],
        'info': 'Performs operation: a x -1'
    },
    'sin': {
        'n': 1,
        'act': lambda a: math.sin(a),
        'alts': ['sine'],
        'info': 'Performs operation: sin(a)'
    },
    'cos': {
        'n': 1,
        'act': lambda a: math.cos(a),
        'alts': ['cosine'],
        'info': 'Performs operation: cos(a)'
    },
    'tan': {
        'n': 1,
        'act': lambda a: math.tan(a),
        'alts': ['tangent'],
        'info': 'Performs operation: tan(a)'
    },
    'asin': {
        'n': 1,
        'act': lambda a: math.asin(a),
        'alts': ['arcsine', 'arcsin'],
        'info': 'Performs operation: asin(a)'
    },
    'acos': {
        'n': 1,
        'act': lambda a: math.acos(a),
        'alts': ['arcos', 'arcosine'],
        'info': 'Performs operation: acos(a)'
    },
    'atan': {
        'n': 1,
        'act': lambda a: math.atan(a),
        'alts': ['arctan', 'arctangent'],
        'info': 'Performs operation: atan(a)'
    },
    'sinh': {
        'n': 1,
        'act': lambda a: math.sinh(a),
        'alts': [],
        'info': 'Performs operation: sinh(a)'
    },
    'cosh': {
        'n': 1,
        'act': lambda a: math.cosh(a),
        'alts': [],
        'info': 'Performs operation: cosh(a)'
    },
    'tanh': {
        'n': 1,
        'act': lambda a: math.tanh(a),
        'alts': [],
        'info': 'Performs operation: cosh(a)'
    },
    'asinh': {
        'n': 1,
        'act': lambda a: math.asinh(a),
        'alts': [],
        'info': 'Performs operation: asinh(a)'
    },
    'acosh': {
        'n': 1,
        'act': lambda a: math.acosh(a),
        'alts': [],
        'info': 'Performs operation: acosh(a)'
    },
    'atanh': {
        'n': 1,
        'act': lambda a: math.atanh(a),
        'alts': [],
        'info': 'Performs operation: atanh(a)'
    },
    'deg': {
        'n': 1,
        'act': lambda a: math.degrees(a),
        'alts': ['degrees'],
        'info': 'Performs operation: deg(a)'
    },
    'rad': {
        'n': 1,
        'act': lambda a: math.radians(a),
        'alts': ['radians'],
        'info': 'Performs operation: rad(a)'
    },
}

#THE GREAT WALL OF CHINA!!!!!!!!!!!!
theGreatWallOfChina = """*******************************
!THE GREAT LIST OF OPERATIONS!

#SPECIALS#
cvt: this operation does nothing. This is useful if you simply want to convert numbers between bases

Algebraic: add, sub, mul, div, exp, sqrt, mod, nrt, log, fct, rcp, inv

Trigonometric: sin, cos, tan

Trigonometric Inverse: asin, acos, atan

Trigonometric Hyperbolic: sinh, cosh, tanh

Trigonometric Hyperbolic Inverse: asinh, acosh, atanh

Angle Conversion: deg, rad

*******************************
"""

#initialize!!
print("""NOTE: Before you begin, take note that any numbers passed as input would require a prefix. The following prefixes are accepted
hex: #
binary: 0b
int: DOES NOT REQUIRE A PREFIX; WHOLE NUMBER WILL BE PARSED

additional notes: 
    * negative numbers will always be preceded by a (-), even in binary. Binary numbers will not be output in 2s compliment mode
    * if you input a negative number without an operation, you may be met with a missing argument error.
        this is because the system thinks you're trying to do subtraction.
    * Decimal numbers are not allowed, only whole numbers are permitted.
""")
#functions!!

def parseUserNumberToBase(s: str) -> Union[tuple[int, str], tuple[None, None]]:
    """parses and returns the base of the provided input, along with it's parsed version"""
    if len(s) < 1: return (None, None)
    if s.startswith('#'):
        return (16, s[1: len(s)])
    elif s.startswith('0b'):
        return (2, s[2: len(s)])
    else:
        return (10, s)

def getParsedBase(s: str, b: int):
    try:
        return int(s, b)
    except Exception:
        return None

def getClosestMatch(inp):
    longestMatch = ''
    matchSymbol = ''
    for op in mathtable:
        if op in inp and len(op) > len(longestMatch):
            longestMatch = op
            matchSymbol = op
        else:
            for alt in mathtable[op]['alts']:
                if alt in inp and len(alt) > len(longestMatch):
                    longestMatch = op
                    matchSymbol = alt
    
    return (longestMatch, matchSymbol) if longestMatch != '' else (None, None)

def getUserValuesAndOperation() -> tuple[str, list[int]]:
    inp = input('Please enter your desired operation\t').lower()

    operator: Union[str, None] = None
    suboperands: list[str] = []
    operands: list[int] = []

    helpSplit = inp.strip().split(' ')
    if helpSplit[0] == 'help':
        if len(helpSplit) > 1:
            (reHelp, reMatch) = getClosestMatch(helpSplit[1])
            if reHelp and reMatch:
                f = mathtable[reHelp]
                print(f"""Help for operation: {reHelp}

parameters: {f['n']}
info: {f['info']}
aliases: {f['alts']}
                """)
                return getUserValuesAndOperation()
            else:
                print(f'{reHelp} is not a valid operation. Remove any additional arguments if you want a list of operations')
                return getUserValuesAndOperation()
        else:
            print(theGreatWallOfChina)
            return getUserValuesAndOperation()

    (op, opSymbol) = getClosestMatch(inp)

    if not op:
        print('No valid operator has been input. Please try again')
        return getUserValuesAndOperation()

    res = inp.split(opSymbol)

    for i in res:
        if i == '':
            res.remove(i)

    if len(res) >= 1:
        if len(res) == mathtable[op]['n']:
            operator = op
            suboperands = res
        else:
            print(f'Your operation {op} does not have the required amount of operands. It requires {mathtable[op]["n"]}, but {len(res)} were provided.') #type: ignore
            return getUserValuesAndOperation()

    if not operator:
        print('No valid operator has been input. Please try again')
        return getUserValuesAndOperation()

    suboperands = [v.replace(' ', '') for v in suboperands]

    for suboperand in suboperands:
        (base, value) = parseUserNumberToBase(suboperand)

        if not base or not value:
            print(f'inferred number {suboperand} is invalid. Please try again.')
            return getUserValuesAndOperation()

        intValue = getParsedBase(value, base)

        if intValue == None:
            print(f'inferred number {suboperand} is malformed. Please try again')
            return getUserValuesAndOperation()

        operands.append(intValue)


    return (operator, operands) #type: ignore

def getLastDigit(n: int):
    """gets the last digit in a number(i hope)"""
    return n if n < 10 else getLastDigit(n - 10)

def getNumericalSuffix(n: int):
    """gets a suffix based on 'n'"""
    d = getLastDigit(n)
    if d == 1:
        return 'st'
    elif d == 2:
        return 'nd'
    elif d == 3:
        return 'rd'
    else:
        return 'th'


#main code!!

(operator, values) = getUserValuesAndOperation()

res = mathtable[operator]['act'](*values)

outMode = input('what is your prefered output mode? (hex, int, bin)(int is default) \t').strip().lower()

if outMode == 'hex' or outMode == 'hexadecimal' or outMode == 'h':
    o = hex(res).replace('0x', '')
    print(f'The result of your operations is [hexadecimal] #{o}')
elif outMode == 'bin' or outMode == 'binary' or outMode == 'b':
    o = bin(res).replace('0b', '')
    print(f'The result of your operations is [binary] 0b{o}')
elif outMode == 'int' or outMode == 'integer' or outMode == 'i':
    print(f'The result of your operations is [integer] {res}')
else:
    print(f'The result of your operation is [integer] {res}\ninteger mode was defaulted to because the provided output mode {outMode} is invalid')