import sys

class Token:
    def __init__(self, value, type):
        self.value = value
        self.type = type

class Node:
    def __init__(self, value,children:list):
        self.value = value
        self.children = children

    def evaluate(self):
        pass

class PrePro:
    @staticmethod
    def filter(code):
        i = 0
        filtered_code = ""
        
        while i < len(code):
            # If a comment starts
            if i < len(code) - 1 and code[i] == '/' and code[i + 1] == '/':
                # Skip till end of line or end of string
                while i < len(code) and code[i] != '\n':
                    i += 1
                # # Skip newline character itself
                # if i < len(code) and code[i] == '\n':
                #     i += 1
            else:
                filtered_code += code[i]
                i += 1
        
        return filtered_code


class BinOp(Node):


    def evaluate(self,sym_table):

        left=self.children[0].evaluate(sym_table)[0]
        left_type=self.children[0].evaluate(sym_table)[1]

        right=self.children[1].evaluate(sym_table)[0]
        right_type=self.children[1].evaluate(sym_table)[1]

        if self.value == '+':
            if left_type != 'doce' or right_type != 'doce':
                raise Exception('Type mismatch on sum')
            result = left + right
            return (int(result),'doce')
        elif self.value == '-':
            if left_type != 'doce' or right_type != 'doce':
                raise Exception('Type mismatch on sub')
            result = left - right
            return (int(result),'doce')
        elif self.value == '*':
            if left_type != 'doce' or right_type != 'doce':
                raise Exception('Type mismatch on mult')
            result = left * right
            return (int(result),'doce')
        elif self.value == '/':
            if left_type != 'doce' or right_type != 'doce':
                raise Exception('Type mismatch on div')
            result = left // right
            return (int(result),'doce')
        elif self.value == '==':
            if left_type != right_type:
                raise Exception('Type mismatch on equal')
            result = left == right
            return (int(result),'doce')
        
        elif self.value == '||':
            if left_type != 'doce' or right_type != 'doce':
                raise Exception('Type mismatch on or')
            result = left or right
            return (int(result),'doce')
        
        elif self.value == '&&':
            if left_type != 'doce' or right_type != 'doce':
                raise Exception('Type mismatch on and')
            result = left and right
            return (int(result),'doce')

        elif self.value == '>':
            result = left > right
            return (int(result),'doce')
        elif self.value == '<':
            result = left < right
            return (int(result),'doce')
        elif self.value == '.':
            result = str(left) + str(right)
            return (str(result),'salgado')
        else:
            raise Exception('Invalid operator')
        
class UnOp(Node):
    def evaluate(self,sym_table):
        if self.value == '+':
            return (self.children[0].evaluate(sym_table)[0],'doce')
        elif self.value == '-':
            return (-self.children[0].evaluate(sym_table)[0],'doce')
        elif self.value == '!':
            return (not self.children[0].evaluate(sym_table)[0],'doce')
        else:
            raise Exception('Invalid operator')
        
class IntVal(Node):
    def evaluate(self,sym_table):
        return (int(self.value),'doce')
    
class NoOp(Node):
    def evaluate(self,sym_table):
        pass

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def set(self, identifier, value):
        if value[1] == self.symbols[identifier][1]:
            if identifier not in self.symbols:
                raise Exception(f"'{identifier}' not found in the symbol table")
            else:
                self.symbols[identifier] = value
        else: 
            raise Exception(f"Type mismatch: {identifier} is of type {self.symbols[identifier][1]} and {value} is of type {value[1]}")

    def get(self, identifier):
        if identifier in self.symbols:
            return self.symbols[identifier]
        else:
            raise Exception(f"'{identifier}' not found in the symbol table")
        
    def create(self,identifier,value):
        if identifier in self.symbols:
            raise Exception(f"'{identifier}' already declared")
        else:
            self.symbols[identifier] = (None,value)
        
class Assignment(Node):
    def evaluate(self, sym_table):
        #print("Evaluating assignment")
        #print(self.children[0].value)
        identifier=self.value
        value = self.children[0].evaluate(sym_table)
        sym_table.set(identifier,value)
        #print(f"Set {identifier} to {value} in SymbolTable.")
        return value

class Identifier(Node):
    def evaluate(self, sym_table):
        return sym_table.get(self.value)
    
class Block(Node):
    def evaluate(self, sym_table):
        #print("Evaluating block")
        last_result = None
        for child in self.children:
            #print(f"Evaluating statement: {type(child).__name__}") 
            last_result = child.evaluate(sym_table)
            # print(last_result)
        return last_result
    
class Program(Node):
    def evaluate(self, sym_table):
        #print("Evaluating block")
        last_result = None
        for child in self.children:
            #print(f"Evaluating statement: {type(child).__name__}") 
            last_result = child.evaluate(sym_table)
            # print(last_result)
        return last_result
    
class Print(Node):
    def evaluate(self, sym_table):
        val = self.children[0].evaluate(sym_table)[0]
        print(val)

class Scanln(Node):
    def evaluate(self, sym_table):
        return (int(input()),'doce')
    
class If(Node):
    def evaluate(self, sym_table):
        condition = self.children[0].evaluate(sym_table)
        if condition[0]:
            return self.children[1].evaluate(sym_table)
        else:
            return self.children[2].evaluate(sym_table)
        
class For(Node):
    def evaluate(self, sym_table):
        self.children[0].evaluate(sym_table)
        while self.children[1].evaluate(sym_table)[0]:
            self.children[3].evaluate(sym_table)
            self.children[2].evaluate(sym_table)

class Vardec(Node):
    def evaluate(self, sym_table):
        
        if len(self.children) ==1:
            sym_table.create(self.children[0].value,self.value)

        else:
            sym_table.create(self.children[0].value,self.value)
            sym_table.set(self.children[0].value,self.children[1].evaluate(sym_table))

class StrVal(Node):
    def evaluate(self, sym_table):
        # print(self.value)
        return (self.value,'salgado')
    
class FuncTable(Node):
    table={}

    def get(name):
        if name in FuncTable.table:
            return FuncTable.table[name]
        else:
            raise Exception(f"Function {name} not found")
        
    def set(identifier, value):
        if value[1] != FuncTable.table[identifier][1]:
            raise Exception(f"Type mismatch: {identifier} is of type {FuncTable.table[identifier][1]} and {value} is of type {value[1]}")
        FuncTable.table[identifier] = value
    
    def create(name,type,node):
        if name in FuncTable.table:
            raise Exception(f"Function {name} already declared")
        else:
            FuncTable.table[name] = (node,type)

class FuncDec(Node):
    def evaluate(self, sym_table):
        FuncTable.create(self.children[0].children[0].value,self.children[0].value,self)

class FuncCall(Node):
    def evaluate(self, sym_table):
        func_name=self.value
        func_node, type = FuncTable.get(func_name)
        func_st=SymbolTable()
        for i in range(len(self.children)):
            func_node.children[i+1].evaluate(func_st)
            func_st.set(func_node.children[i+1].children[0].value,self.children[i].evaluate(sym_table))

        ret_block = func_node.children[-1].evaluate(func_st)
        if ret_block is not None:
            if type == ret_block[1]:
                return ret_block
            else:
                raise Exception("Type mismatch on Funcall")
            

class Return(Node):
    def evaluate(self, sym_table):
        return self.children[0].evaluate(sym_table)


    

class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next = None
        self.selectNext()

    def selectNext(self):

        while self.position < len(self.source) and (self.source[self.position] == " " or self.source[self.position] == "\t"):
            self.position += 1


        if self.position >= len(self.source):
            self.next = Token(None, 'EOF')
            return

        char = self.source[self.position]
        self.position += 1

        if char in ['+', '-', '*', '/']:
            self.next = Token(char, 'OPERATOR')
        elif char in ['(', ')']:
            self.next = Token(char, 'PARENTHESIS')
        elif char == '\n':
            self.next = Token(char, 'BREAKLINE')
        elif char == ' ':
            self.next = Token(char, 'SPACE')
        elif char == '\t':
            self.next = Token(char, 'TAB')   
        elif char == '=':
            if self.position < len(self.source) and self.source[self.position] == '=':
                self.next = Token('==', 'COMPARE')
                self.position += 1
            else:
                self.next = Token(char, 'EQUALS')
        elif char == '|':
            if self.position < len(self.source) and self.source[self.position] == '|':
                self.next = Token('||', 'OR')
                self.position += 1
        elif char == '&':
            if self.position < len(self.source) and self.source[self.position] == '&':
                self.next = Token('&&', 'AND')
                self.position += 1
        elif char == '"':
            string = ''
            char = self.source[self.position]
            while char != '"':
                string += char
                if self.position >= len(self.source):
                    raise Exception(f"Unexpected end of string")
                self.position += 1
                char = self.source[self.position]
    
            self.next = Token(string, 'STRING')  
            self.position += 1   
        elif char == '.':
            self.next = Token(char, 'CONCAT')
        elif char == '>':
            self.next = Token(char, 'GREATER')
        elif char == '<':
            self.next = Token(char, 'LESS')
        elif char == '!':
            self.next = Token(char, 'NOT')
        elif char == ';':
            self.next = Token(char, 'SEMICOLON')
        elif char == '{':
            self.next = Token(char, 'OPEN_BRACKET')
        elif char == '}':
            self.next = Token(char, 'CLOSE_BRACKET')
        elif char == ',':
            self.next = Token(char, 'COMMA')
        elif char.isdigit():
            number = ''
            while char.isdigit():
                number += char
                if self.position >= len(self.source):
                    break
                char = self.source[self.position]
                if char.isdigit():
                    self.position += 1
                elif char in ['+', '-', '*', '/','(', ')',";",' ','\n',","] or char.isalpha() or char == '_':
                    break
                else:
                    raise Exception(f"Unexpected character 1 {char}")
            self.next = Token(int(number), 'NUMBER')
        elif char.isalpha():
            identifier = ''
            while char.isalnum() or char == '_':
                identifier += char
                if self.position >= len(self.source):
                    break
                char = self.source[self.position]
                if char.isalnum() or char == '_':
                    self.position += 1
                else:
                    break
            if identifier == 'refeicao':
                self.next = Token(identifier, 'PRINTLN')
            elif identifier == 'tempero':
                self.next = Token(identifier, 'SCANLN')
            elif identifier == 'experimentar':
                self.next = Token(identifier, 'IF')
            elif identifier == 'saboreando':
                self.next = Token(identifier, 'ELSE')
            elif identifier == 'degustando':
                self.next = Token(identifier, 'FOR')
            elif identifier == 'doce':
                self.next = Token(identifier, 'INT')
            elif identifier == 'salgado':
                self.next = Token(identifier, 'STR')
            elif identifier == 'comida':
                self.next = Token(identifier, 'VAR')
            elif identifier == 'banquete':
                self.next = Token(identifier, 'FUNC')
            elif identifier == 'satisfeito':
                self.next = Token(identifier, 'RETURN')
            else:
                self.next = Token(identifier, 'IDENTIFIER')
                #print(f"Detected identifier: {identifier}")
        else:
            raise Exception(f"Unexpected character 2 {char}")



class Parser:

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.current = self.tokenizer.next

    
    def parseFactor(self):

        if (self.current.type == "OPERATOR" and self.current.value in ['+', '-']) or (self.current.type == "NOT" and self.current.value == '!'):
            unary_operator = self.current.value
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            return UnOp(unary_operator, [self.parseFactor()])
        
        elif self.current.type == 'STRING':
            value = self.current.value
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            return StrVal(value, [])

        elif self.current.type == 'NUMBER':
            value = self.current.value
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            return IntVal(value, [])

        elif self.current.type == "PARENTHESIS" and self.current.value == '(':
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            node = self.boolExpression()
            if self.current.type == "PARENTHESIS" and self.current.value == ')':
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                return node
            else:
                raise Exception('Expected closing parenthesis on factor')
        
        elif self.current.type == "IDENTIFIER":
            var = self.current.value
            node = Identifier(var, [])
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            if self.current.type == "PARENTHESIS" and self.current.value == "(":
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                result = FuncCall(var,[])
                while self.current.value != ")":
                    result.children.append(self.boolExpression())
                    if self.current.type == "COMMA":
                        self.tokenizer.selectNext()
                        self.current = self.tokenizer.next
                    else:
                        break
                if self.current.value == ")":
                    self.tokenizer.selectNext()
                    self.current = self.tokenizer.next
                    return result
                else:
                    raise Exception(f"Unexpected token after opening parenthesis should be a closing parenthesis: {self.current.value}")
            return node
        
        elif self.current.type == "SCANLN":
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            if self.current.type == "PARENTHESIS" and self.current.value == "(":
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                if self.current.type == "PARENTHESIS" and self.current.value == ")":
                    self.tokenizer.selectNext()
                    self.current = self.tokenizer.next
                    return Scanln("Scanln",[])
                else:
                    raise Exception('Expected closing parenthesis')
            else:
                raise Exception('Expected opening parenthesis')
        
        raise Exception(f'Invalid factor at {self.current.value} of type {self.current.type}')



    def parseTerm(self):
        result = self.parseFactor()

        while self.current.type == 'OPERATOR' and self.current.value in ['*', '/']:
            operator = self.current.value
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            
            result=BinOp(operator,[result,self.parseFactor()])
            

        return result

    def parseExpression(self):
        result = self.parseTerm()

        while (self.current.type == 'OPERATOR' and self.current.value in ['+', '-']) or (self.current.type == "CONCAT" and self.current.value == '.'):
            operator = self.current.value
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            result = BinOp(operator, [result, self.parseTerm()])

        return result
    
    def parseStatement(self):
        #print(f"Starting statement parsing at: {self.current.value}, {self.current.type}")
        if self.current.type == "BREAKLINE":
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            #print(f"Finished statement parsing, next token: {self.current.value}, {self.current.type}")
            return NoOp("", [])

        elif self.current.type == "IDENTIFIER":
            var_name = self.current.value
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next

            if self.current.value == "=":
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                expr = self.boolExpression()

                result = Assignment(var_name, [expr])
               
                if self.current.type == "BREAKLINE":
                    self.tokenizer.selectNext()
                    self.current = self.tokenizer.next
                    return result
                else:
                    raise Exception(f"Unexpected token after assignment: {self.current.value}")
                
            elif self.current.value == "(":
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                result = FuncCall(var_name,[])
                while self.current.value != ")":
                    result.children.append(self.boolExpression())
                    if self.current.type == "COMMA":
                        self.tokenizer.selectNext()
                        self.current = self.tokenizer.next
                    else:
                        break

                if self.current.value == ")":
                    self.tokenizer.selectNext()
                    self.current = self.tokenizer.next
                    if self.current.type == "BREAKLINE":
                        self.tokenizer.selectNext()
                        self.current = self.tokenizer.next
                        return result
                    else:
                        raise Exception(f"Unexpected token after assignment: {self.current.value}") 
            else:
                raise Exception(f"Unexpected token after identifier: {self.current.value}")
        
        
        elif self.current.type == "PRINTLN":
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            if self.current.value == "(":
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                expr = self.boolExpression()
                result = Print(None,[expr])
                if self.current.value == ")":
                    self.tokenizer.selectNext()
                    self.current = self.tokenizer.next
                    if self.current.type == "BREAKLINE":
                        self.tokenizer.selectNext()
                        self.current = self.tokenizer.next
                        return result
                    if self.current.type == "EOF":
                        return result
                    else:
                        raise Exception(f"Unexpected token after println: {self.current.value}")
                    
                else:
                    raise Exception(f"Unexpected token, should have a ) instead got : {self.current.value}")
                
            else:
                raise Exception(f"Unexpected token, should have a ( instead got : {self.current.value}")
                    #print(f"Finished statement parsing, next token: {self.current.value}, {self.current.type}")

                
        elif self.current.type == "IF":
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            condition = self.boolExpression()
            if_block = self.parseBlock()
            if self.current.type == "ELSE":
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                else_block = self.parseBlock()
                result = If(None, [condition, if_block, else_block])
            else:
                result = If(None, [condition, if_block])

            if self.current.type == "BREAKLINE":
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                return result
            
            
        elif self.current.type == "FOR":
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            assign=self.parseAssign()
            if self.current.type == "SEMICOLON":
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                condition = self.boolExpression()
                if self.current.type == "SEMICOLON":
                    self.tokenizer.selectNext()
                    self.current = self.tokenizer.next
                    increment=self.parseAssign()
                    block=self.parseBlock()
                    result = For(None, [assign, condition, increment, block])

            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            if self.current.type == "BREAKLINE":
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                return result
            
        
            else:
                raise Exception(f"Unexpected token after for: {self.current.value}")
            
        elif self.current.type == "VAR":
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            if self.current.type == "IDENTIFIER":
                ident=Identifier(self.current.value,[])
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                if self.current.type == "INT" or self.current.type == "STR":
                    type= self.current.value
                    variable= Vardec(type,[ident])
                    self.tokenizer.selectNext()
                    self.current = self.tokenizer.next
                    if self.current.type == "EQUALS":
                        self.tokenizer.selectNext()
                        self.current = self.tokenizer.next
                        result=Vardec(type,[ident,self.boolExpression()])
                        if self.current.type == "BREAKLINE":
                            self.tokenizer.selectNext()
                            self.current = self.tokenizer.next
                            return result
                        
                    elif self.current.type == "BREAKLINE":
                        self.tokenizer.selectNext()
                        self.current = self.tokenizer.next
                        return variable
                    else:
                        raise Exception(f"Unexpected token after vardec 1 : {self.current.value}")
                    
        
            else:
                raise Exception(f"Unexpected token after vardec 2 : {self.current.value}")
            
        elif self.current.type == "RETURN":
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            result = Return(None,[self.boolExpression()])
            if self.current.type == "BREAKLINE":
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                return result
            else:
                raise Exception(f"Unexpected token after return: {self.current.value}")
       
        else:
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            if self.current.type == "BREAKLINE":
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                return self.parseAssign()
            else:
                raise Exception(f" Teste {self.current.value}")
        
    def parseBlock(self):
        if self.current.type == 'OPEN_BRACKET':
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            if self.current.type == 'BREAKLINE':
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                result= Block("",[])
                while self.current.type != 'CLOSE_BRACKET':
                    result.children.append(self.parseStatement())
                if self.current.type == 'CLOSE_BRACKET':
                    self.tokenizer.selectNext()
                    self.current = self.tokenizer.next
                    return result
                else:
                    raise Exception(f"Unexpected token after Close Bracket: {self.current.value}")

            
            else:
                raise Exception(f"Unexpected token after Open Bracket: {self.current.value}")
            
    def relExpression(self):
        result = self.parseExpression()

        while self.current.type == 'COMPARE' or self.current.type == 'GREATER' or self.current.type == 'LESS':
            if self.current.type == 'COMPARE':
                operator = self.current.value
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                result = BinOp(operator, [result, self.parseExpression()])
            elif self.current.type == 'GREATER':
                operator = self.current.value
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                result = BinOp(operator, [result, self.parseExpression()])
            elif self.current.type == 'LESS':
                operator = self.current.value
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                result = BinOp(operator, [result, self.parseExpression()])

        return result
    
    def boolTerm(self):
        result = self.relExpression()

        while self.current.type == 'AND':
            operator = self.current.value
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            result = BinOp(operator, [result, self.relExpression()])

        return result
    
    def boolExpression(self):
       
        result = self.boolTerm()
    
        while self.current.type == 'OR':
            operator = self.current.value
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            result = BinOp(operator, [result, self.boolTerm()])

        return result
    
    def parseAssign(self):
        if self.current.type == 'IDENTIFIER':
            var_name = self.current.value
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            if self.current.type == 'EQUALS':
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                expr = self.parseExpression()
                return Assignment(var_name, [expr])
            elif self.current.type == 'PARENTHESIS' and self.current.value == "(":
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                result = FuncCall(var_name,[])
                while self.current.value != ")":
                    result.children.append(self.boolExpression())
                    if self.current.type == "COMMA":
                        self.tokenizer.selectNext()
                        self.current = self.tokenizer.next
                    else:
                        break
                if self.current.value == ")":
                    self.tokenizer.selectNext()
                    self.current = self.tokenizer.next
                    if self.current.type == "BREAKLINE":
                        self.tokenizer.selectNext()
                        self.current = self.tokenizer.next
                        return result
                    else:
                        raise Exception(f"Unexpected token after closing parenthesis should be a breakline: {self.current.value}")
                else:
                    raise Exception(f"Unexpected token after opening parenthesis should be a closing parenthesis: {self.current.value}")
            else:
                raise Exception(f"Unexpected token after identifier should be a equalm: {self.current.value}")
        else:
            raise Exception(f"Unexpected token, it is not a identifier: {self.current.value}")

    
    def parseProgram(self):
        resultado = Program("", [])
        while self.tokenizer.next.type != "EOF":
            while self.current.type == 'BREAKLINE':
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
            if self.current.type != "EOF":
                resultado.children.append(self.parseDeclaration())
        resultado.children.append(FuncCall("main",[]))
        return resultado
    
    def parseDeclaration(self):

        param_list = []
        
        if self.current.type == 'FUNC':
            self.tokenizer.selectNext()
            self.current = self.tokenizer.next
            if self.current.type == 'IDENTIFIER':
                func_name = self.current.value
                self.tokenizer.selectNext()
                self.current = self.tokenizer.next
                if self.current.type == 'PARENTHESIS' and self.current.value == '(':
                    self.tokenizer.selectNext()
                    self.current = self.tokenizer.next
                    while self.current.type == 'IDENTIFIER':
                        param_name = self.current.value
                        self.tokenizer.selectNext()
                        self.current = self.tokenizer.next
                        param_type = self.current.value
                        self.tokenizer.selectNext()
                        self.current = self.tokenizer.next
                        param_list.append((param_type,param_name))
                        if self.current.type == 'COMMA':
                            self.tokenizer.selectNext()
                            self.current = self.tokenizer.next
                        else:
                            break
                    if self.current.type == 'PARENTHESIS' and self.current.value == ')':
                        self.tokenizer.selectNext()
                        self.current = self.tokenizer.next
                        if self.current.type == 'INT' or self.current.type == 'STR':
                            func_type = self.current.value
                            self.tokenizer.selectNext()
                            self.current = self.tokenizer.next

                            result = FuncDec(None, [Vardec(func_type,[Identifier(func_name,[])])])

                            if len(param_list) > 0:
                                for i in range(len(param_list)):
                                    result.children.append(Vardec(param_list[i][0],[Identifier(param_list[i][1],[])]))
                            result.children.append(self.parseBlock())

                            if self.current.type == 'BREAKLINE':
                                self.tokenizer.selectNext()
                                self.current = self.tokenizer.next
                            else:
                                raise Exception(f"Unexpected token should be breakline: {self.current.value}")
                            return result
                        else:
                            print(f'value: {Parser.tokenizer.next.value}')
                            print(f'tipo: {Parser.tokenizer.next.type}')
                            raise Exception(f"Unexpected token should be a int or a string : {self.current.value}")
                    else:
                        raise Exception(f"Unexpected token should be a closing parenthesis: {self.current.value}")
                else:
                    raise Exception(f"Unexpected token should be an Open Parenthesis: {self.current.value}")
            else:
                raise Exception(f"Unexpected token after func, should be an identifier: {self.current.value}")
            
        else:
            raise Exception(f"Unexpected token, should be a func: {self.current.value}")
    


    @staticmethod
    def run(code):
        code = PrePro().filter(code)
        #print(code)
        tokenizer = Tokenizer(code)
        parser = Parser(tokenizer)

        result = parser.parseProgram()

        if parser.current.type != 'EOF':
            raise Exception(f'Invalid expression, stopped at {parser.current.value} of type {parser.current.type}')

        return result

def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py '<expression>'", file=sys.stderr)
        return
    try:
        with open (sys.argv[1], "r") as myfile:
            data=myfile.read()
        ast_root = Parser.run(data)
        sym_table = SymbolTable()
        ast_root.evaluate(sym_table)
    
    except Exception as e:
        print(str(e), file=sys.stderr)

if __name__ == "__main__":
    main()