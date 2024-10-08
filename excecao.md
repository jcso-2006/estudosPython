## Tratamento de Exceções em Python

O tratamento de exceções é uma técnica fundamental na programação, utilizada para lidar com erros que podem ocorrer durante a execução de um programa. O principal objetivo do tratamento de exceções é evitar que o programa termine de forma abrupta e oferecer uma maneira de controlar essas situações, tornando os programas mais seguros, confiáveis e fáceis de usar.

Em Python, o tratamento de exceções é feito utilizando os blocos `try-except`. Dentro desse bloco, o programador pode capturar exceções específicas e decidir como o programa deve reagir a elas. Isso é especialmente útil quando queremos garantir que o código continue a ser executado, mesmo que uma operação falhe.

A seguir, apresentamos 10 exceções comuns em Python que podem ser tratadas usando o bloco `except`:

1. **`ValueError`**: Ocorre quando um valor passado para uma função é do tipo correto, mas não é apropriado para a operação esperada.  
   **Exemplo**:  
   ```python
    try:
        texte = int('abc')
        print(texte)
    except ValueError:
        print("Valor não é apropriado para o que foi defenido")
   ```

2. **`TypeError`**: Ocorre quando uma operação ou função é aplicada a um objeto de um tipo inadequado.  
   **Exemplo**:  
   ```python
    try:
        print(5 + 'string')
    except TypeError:
        print("Não são do mesmo tipo")
   ```

3. **`IndexError`**: Ocorre quando você tenta acessar um índice que está fora dos limites de uma lista ou sequência.  
   **Exemplo**: 
   ```python
   try:
        lista = [1, 2, 3]
        print(lista[5])
   except IndexError:
        print(não existe esse índice )
   ```

4. **`KeyError`**: Ocorre quando se tenta acessar uma chave inexistente em um dicionário.  
   **Exemplo**:  
   ```python
   try:
        dicionario = {'a': 1}; dicionario['b']
   except KeyError:
        print("letra fora da variavel ")
   ```

5. **`ZeroDivisionError`**: Ocorre quando se tenta dividir um número por zero.  
   **Exemplo**: 
   ```python
   try:
       print(5 / 0)
   except ZeroDivisionError:
        print("impossivel divider por 0")
   ```

6. **`FileNotFoundError`**: Ocorre quando se tenta abrir um arquivo que não existe.  
   **Exemplo**:
   ```python
   try:
        dicionario = {'a': 1}; dicionario['b']
   except FileNotFoundError:
        print("letra fora da variavel ")
   ```

7. **`AttributeError`**: Ocorre quando se tenta acessar um atributo ou método que não existe em um objeto.  
   **Exemplo**: 
   ```python
   try:
        numero = 10
        numero.append(5)
   except AttributeError:
    print("Você tentou colocar um elemento dentro de uma variaval que não é uma lista.")
   ```

8. **`ImportError`**: Ocorre quando uma importação falha, por exemplo, quando o módulo não é encontrado.  
   **Exemplo**:  
   ```python
   try:
        import tkk from oi
   except ImportError:
        print("print oi não texiste em tkk")
   ```

9. **`IndentationError`**: Ocorre quando a indentação do código está incorreta.  
   **Exemplo**: Falta de indentação ou níveis de indentação incorretos causam um `IndentationError`.  
   ```python
   def exemplo():
   print("Ola mundo")

   try:
        exec(exemplo)
   except IndentationError:
        print("identação errada ")
   ```

10. **`TimeoutError`**: Ocorre quando uma operação excede o tempo limite, como em uma conexão de rede ou uma função que define um timeout.  
   ```python
   import threading
   import time

   def funcao_lenta():
      print("A função começou...")
      time.sleep(10)
      print("A função terminou.")

   def chamar_com_timeout():
      try:
         thread = threading.Thread(target=funcao_lenta)
         thread.start()
         thread.join(timeout=5)

        if thread.is_alive():
            raise TimeoutError("A função demorou muito para responder.")
   except TimeoutError as e:
        print(f"Ocorreu um erro de timeout: {e}")

chamar_com_timeout()

   ```

O tratamento correto dessas exceções é fundamental para garantir que o programa seja capaz de lidar com erros e continuar executando de forma segura e previsível.

---

