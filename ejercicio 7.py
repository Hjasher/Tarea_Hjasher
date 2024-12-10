# Ejercicio 7: Verificar Parentesis Balanceados
    #   Usa una pila para verificar si una cadena de paréntesis ((), {}, []) está balanceada.

def esta_balanceada(cadena):
    pila = []
    pares = {")": "(", "}": "{", "]": "["}
    
    for char in cadena:
        if char in "({[":
            pila.append(char)
        elif char in ")}]":
            if not pila or pila[-1] != pares[char]:
                return False
            pila.pop() 

    return len(pila) == 0 


print(esta_balanceada("("))
print(esta_balanceada("{[(])}"))
print(esta_balanceada("()"))       
print(esta_balanceada("(())"))    
print(esta_balanceada("()"))       
print(esta_balanceada("({[]})"))   
print(esta_balanceada("{[()]}"))   
print(esta_balanceada("{[(])}"))   
print(esta_balanceada("({[})")) 