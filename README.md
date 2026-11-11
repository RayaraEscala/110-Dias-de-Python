# 🐍 110 Dias de Python

> Um exercício por dia, durante 110 dias, para sair do zero e aprender Python na prática: escrevendo código, errando, corrigindo e publicando.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20andamento-yellow)
![Progresso](https://img.shields.io/badge/progresso-0%2F110-lightgrey)

---

## 📌 Sobre o projeto

Este repositório documenta minha jornada de **110 dias** resolvendo, um por dia, os exercícios do curso de Python em vídeo (Curso em Vídeo, do professor Gustavo Guanabara). Cada exercício vira um pequeno projeto: um script que resolve um problema real, do cálculo de desconto ao jogo de dados.

**Por que 110 dias, um exercício por dia?**
Constância vence intensidade. Programar um pouco todo dia fixa a sintaxe, cria o hábito de resolver problemas e deixa um histórico público de evolução (os commits contam a história).

## 🎯 Objetivos

- Dominar os fundamentos de Python: variáveis, operadores, strings, condições, laços, estruturas de dados, funções e módulos.
- Desenvolver **lógica de programação** e o raciocínio de decompor problemas.
- Criar o hábito de **versionar código com Git/GitHub**.
- Montar um portfólio que mostre evolução real, não só o resultado final.

## 🗂️ Estrutura do repositório

```
110-dias-de-python/
├── README.md
├── mundo-01-fundamentos/
│   ├── ex001_deixando_tudo_pronto.py
│   ├── ex002_respondendo_ao_usuario.py
│   └── ...
├── mundo-02-estruturas-de-controle/
│   └── ...
├── mundo-03-estruturas-compostas/
│   └── ...
└── anotacoes/
    └── diario.md        # aprendizados, dúvidas e erros de cada dia
```

> Convenção de nomes: `exNNN_nome_do_exercicio.py` (tudo minúsculo, sem acento, com `_`).

## ▶️ Como executar

```bash
# 1. Clone o repositório
git clone https://github.com/SEU-USUARIO/110-dias-de-python.git
cd 110-dias-de-python

# 2. Confira a versão do Python (3.8+)
python --version

# 3. Execute qualquer exercício
python mundo-01-fundamentos/ex002_respondendo_ao_usuario.py
```

Alguns exercícios usam bibliotecas externas (por exemplo, o #021 que toca um MP3):

```bash
pip install pygame
```

---

## 🧠 Metodologia de estudo (como aprender de verdade)

Assistir aula não é o mesmo que aprender. A rotina diária deste projeto:

1. **Assistir** à aula do módulo (ou rever a anterior) e **anotar** os conceitos com as suas palavras.
2. **Tentar sozinha primeiro**: antes de ver a resolução, passe pelo menos 15 minutos tentando. A dificuldade é onde o aprendizado acontece.
3. **Digitar, nunca copiar**: escrever o código fixa a sintaxe.
4. **Testar com vários valores**: normais, zero, negativos, texto no lugar de número. Isso treina o olhar para erros.
5. **Comparar** com a resolução do professor e anotar o que ele fez diferente.
6. **Refatorar**: reescrever com nomes melhores, comentários e menos repetição.
7. **Commitar**: um commit por exercício, com mensagem clara.
8. **Registrar no diário**: o que aprendi, o que travou, o que revisar.

### ✍️ Padrão de commits

```
feat: ex012 - calculando descontos
fix: ex012 - corrige formatação de casas decimais
docs: atualiza progresso no README
```

### 🔁 Revisão espaçada

Nos dias **7, 14, 30 e 60**, refaça um exercício antigo **sem consultar nada**. Se conseguir, o conceito está fixado; se não, volte à aula correspondente.

---

## 📊 Progresso

| Mundo | Tema | Exercícios | Concluídos |
|-------|------|-----------|------------|
| 1 | Fundamentos: entrada/saída, tipos, operadores, módulos, textos, condições | #001 a #035 | 0/35 |
| 2 | Condições aninhadas e laços (`for`, `while`) | #036 a #071 | 0/36 |
| 3 | Tuplas, listas, dicionários, funções, módulos e pacotes | #072 a #110 | 0/39 |
| **Total** | | | **0/110** |

> Atualize o selo de progresso e esta tabela conforme avançar.

---

## 📚 Aulas do curso

| Aula | Tema | Conceito central |
|------|------|------------------|
| #01 | Seja um Programador | O que é programar |
| #02 | Para que serve o Python? | Usos e áreas da linguagem |
| #03 | Instalando o Python 3 e o IDLE | Ambiente de desenvolvimento |
| #04 | Primeiros comandos em Python 3 | `print()` e execução |
| #05 | Instalando o PyCharm e o QPython3 | IDEs e Python no celular |
| #06 | Tipos Primitivos e Saída de Dados | `int`, `float`, `str`, `bool`, `input()` |
| #07 | Operadores Aritméticos | `+ - * / // % **` e precedência |
| #08 | Utilizando Módulos | `import`, `math`, `random` |
| #09 | Manipulando Texto | Fatiamento e métodos de `str` |
| #10 | Condições (Parte 1) | `if`, `else`, operadores de comparação |
| #11 | Cores no Terminal | Códigos ANSI |
| #12 | Condições Aninhadas | `elif`, decisões encadeadas |
| #13 | Estrutura de repetição `for` | `range()`, iteração |
| #14 | Estrutura de repetição `while` | Laços condicionais |
| #15 | Interrompendo repetições `while` | `break`, flags, validação |
| #16 | Tuplas | Sequências imutáveis |
| #17 | Listas (Partes 1 e 2) | Sequências mutáveis, listas compostas, matrizes |
| #19 | Dicionários | Estrutura chave-valor |
| #20 | Funções (Parte 1) | `def`, parâmetros, retorno |
| #21 | Funções (Parte 2) | Escopo, argumentos opcionais, `*args` |
| #22 | Módulos e Pacotes | Criar e importar seus próprios módulos |

---

## ✅ Exercícios e habilidades desenvolvidas

Um exercício por dia, com as habilidades que cada um desenvolve.

### 🌱 Mundo 1: Fundamentos (Dias 1 a 35)

| Dia | Exercício | Habilidades desenvolvidas |
|----:|-----------|---------------------------|
| 1 | #001 Deixando tudo pronto | Configuração do ambiente, primeiro script, `print()` |
| 2 | #002 Respondendo ao Usuário | `input()`, `print()`, interação com o usuário |
| 3 | #003 Somando dois números | Conversão de tipos (`int()`), operador `+` |
| 4 | #004 Dissecando uma Variável | `type()`, métodos como `isnumeric()`, `isalpha()`, `isupper()` |
| 5 | #005 Antecessor e Sucessor | Aritmética básica, expressões |
| 6 | #006 Dobro, Triplo, Raiz Quadrada | Operadores, potenciação, raiz com `**` |
| 7 | #007 Média Aritmética | `float`, soma e divisão, ordem das operações |
| 8 | #008 Conversor de Medidas | Conversão de unidades, múltiplas saídas |
| 9 | #009 Tabuada | Multiplicação, formatação da saída, f-strings |
| 10 | #010 Conversor de Moedas | Cálculo com `float`, formatação `:.2f` |
| 11 | #011 Pintando Parede | Cálculo de área e rendimento, proporção |
| 12 | #012 Calculando Descontos | Porcentagem, modelagem de regra de negócio |
| 13 | #013 Reajuste Salarial | Porcentagem, acréscimos, formatação monetária |
| 14 | #014 Conversor de Temperaturas | Fórmulas, precisão numérica |
| 15 | #015 Aluguel de Carros | Cálculo composto (valor fixo + variável) |
| 16 | #016 Quebrando um número | Módulo `math`, `trunc()`, parte inteira |
| 17 | #017 Catetos e Hipotenusa | `math.hypot()`, `pow()`, `sqrt()` |
| 18 | #018 Seno, Cosseno e Tangente | `math.radians()`, `sin`, `cos`, `tan` |
| 19 | #019 Sorteando um item na lista | Módulo `random`, `choice()`, primeira lista |
| 20 | #020 Sorteando uma ordem na lista | `shuffle()`, manipulação de listas |
| 21 | #021 Tocando um MP3 | Bibliotecas externas, `pip`, uso de documentação |
| 22 | #022 Analisador de Textos | `upper()`, `lower()`, `len()`, `strip()`, `split()` |
| 23 | #023 Separando dígitos de um número | Fatiamento, divisão inteira `//` e resto `%` |
| 24 | #024 Verificando as primeiras letras de um texto | Fatiamento, `startswith()`, comparação de strings |
| 25 | #025 Procurando uma string dentro de outra | Operador `in`, normalização de texto |
| 26 | #026 Primeira e última ocorrência de uma string | `find()`, `rfind()`, `count()` |
| 27 | #027 Primeiro e último nome de uma pessoa | `split()`, índices positivos e negativos |
| 28 | #028 Jogo da Adivinhação v.1.0 | `randint()`, `if/else`, comparação |
| 29 | #029 Radar eletrônico | Condicionais, cálculo de multa |
| 30 | #030 Par ou Ímpar? | Operador `%`, decisão binária |
| 31 | #031 Custo da Viagem | Condições por faixa de valor, cálculo de preço |
| 32 | #032 Ano Bissexto | Operadores lógicos `and`, `or`, `not` |
| 33 | #033 Maior e menor valores | Comparação de múltiplos valores, lógica |
| 34 | #034 Aumentos múltiplos | `if/elif/else`, faixas, porcentagens |
| 35 | #035 Analisando Triângulo v1.0 | Condições compostas, validação de regra geométrica |

### 🌿 Mundo 2: Estruturas de Controle (Dias 36 a 71)

| Dia | Exercício | Habilidades desenvolvidas |
|----:|-----------|---------------------------|
| 36 | #036 Aprovando Empréstimo | Condições aninhadas, regra de negócio |
| 37 | #037 Conversor de Bases Numéricas | `bin()`, `oct()`, `hex()`, menu com decisão |
| 38 | #038 Comparando números | Condicionais com três resultados possíveis |
| 39 | #039 Alistamento Militar | Datas, idade, módulo `datetime` |
| 40 | #040 Aquele clássico da Média | Condicionais por faixa, classificação |
| 41 | #041 Classificando Atletas | Categorização por idade, `elif` |
| 42 | #042 Analisando Triângulos v2.0 | Classificação (equilátero, isósceles, escaleno) |
| 43 | #043 Índice de Massa Corporal | Fórmula, faixas de classificação |
| 44 | #044 Gerenciador de Pagamentos | Descontos e juros por forma de pagamento |
| 45 | #045 GAME: Pedra, Papel e Tesoura | Lógica de jogo, `random`, regras de vitória |
| 46 | #046 Contagem regressiva | `for` com `range()` decrescente, `sleep()` |
| 47 | #047 Contagem de pares | `range()` com passo, filtragem |
| 48 | #048 Soma de ímpares múltiplos de três | Acumuladores, condições dentro de laços |
| 49 | #049 Tabuada v.2.0 | Laço `for` com formatação |
| 50 | #050 Soma dos pares | Acumulador, filtro com `%` |
| 51 | #051 Progressão Aritmética | Laços, padrões numéricos |
| 52 | #052 Números primos | Laços, contadores, algoritmo de divisibilidade |
| 53 | #053 Detector de Palíndromo | Strings, inversão, comparação |
| 54 | #054 Grupo da Maioridade | Laço com datas, contadores condicionais |
| 55 | #055 Maior e menor da sequência | Variáveis de controle, máximo e mínimo |
| 56 | #056 Analisador completo | Combinação de laços, acumuladores e condições |
| 57 | #057 Validação de Dados | `while`, validação de entrada |
| 58 | #058 Jogo da Adivinhação v2.0 | `while`, contador de tentativas, dicas |
| 59 | #059 Criando um Menu de Opções | Menu interativo, `while True`, `break` |
| 60 | #060 Cálculo do Fatorial | Laços `for` e `while`, acumulador multiplicativo |
| 61 | #061 Progressão Aritmética v2.0 | `while` com condição de parada |
| 62 | #062 Super Progressão Aritmética v3.0 | Laços dinâmicos, entrada do usuário |
| 63 | #063 Sequência de Fibonacci v1.0 | Variáveis auxiliares, atribuição simultânea |
| 64 | #064 Tratando vários valores v1.0 | Valor sentinela, `while` |
| 65 | #065 Maior e Menor valores | Laços com continuação interativa |
| 66 | #066 Vários números com flag | Flag de parada, `break` |
| 67 | #067 Tabuada v.3.0 | Laço com condição de saída, controle de fluxo |
| 68 | #068 Jogo do Par ou Ímpar | Laços, lógica de jogo, sequência de vitórias |
| 69 | #069 Análise de dados do grupo | Múltiplos contadores e filtros |
| 70 | #070 Estatísticas em produtos | Acumuladores, totais, mínimo e máximo |
| 71 | #071 Simulador de Caixa Eletrônico | Divisão e resto, notas e cédulas, algoritmo guloso |

### 🌳 Mundo 3: Estruturas Compostas e Funções (Dias 72 a 110)

| Dia | Exercício | Habilidades desenvolvidas |
|----:|-----------|---------------------------|
| 72 | #072 Número por Extenso | Tuplas, indexação |
| 73 | #073 Tuplas com Times de Futebol | Fatiamento de tuplas, `sorted()`, `index()` |
| 74 | #074 Maior e menor valores em Tupla | Tuplas com `random`, `max()`, `min()` |
| 75 | #075 Análise de dados em uma Tupla | `count()`, `index()`, percorrer tuplas |
| 76 | #076 Lista de Preços com Tupla | Tuplas alternando texto e número, formatação tabular |
| 77 | #077 Contando vogais em Tupla | Iteração aninhada, strings dentro de tuplas |
| 78 | #078 Maior e Menor valores na Lista | Listas, `append()`, posições de valores |
| 79 | #079 Valores únicos em uma Lista | Verificação de duplicatas com `in` |
| 80 | #080 Lista ordenada sem repetições | `insert()`, inserção ordenada |
| 81 | #081 Extraindo dados de uma Lista | `sort()`, `len()`, busca de valor |
| 82 | #082 Dividindo valores em várias listas | Separação por critério (pares e ímpares) |
| 83 | #083 Validando expressões matemáticas | Pilha com lista, parênteses balanceados |
| 84 | #084 Lista composta e análise de dados | Listas dentro de listas, médias e filtros |
| 85 | #085 Listas com pares e ímpares | Listas aninhadas, ordenação e agrupamento |
| 86 | #086 Matriz em Python | Matrizes (listas de listas), laços aninhados |
| 87 | #087 Mais sobre Matriz em Python | Soma de linhas e colunas, diagonais |
| 88 | #088 Palpites para a Mega Sena | Listas, `random`, `sort()`, geração de jogos |
| 89 | #089 Boletim com listas compostas | Estruturas aninhadas, média, consulta interativa |
| 90 | #090 Dicionário em Python | Criação de dicionário, chaves e valores |
| 91 | #091 Jogo de Dados em Python | Dicionários, `random`, ordenação com `sorted()` |
| 92 | #092 Cadastro de Trabalhador em Python | Dicionário com dados mistos, `datetime` |
| 93 | #093 Cadastro de Jogador de Futebol | Dicionário com listas, estatísticas |
| 94 | #094 Unindo dicionários e listas | Lista de dicionários, análises agregadas |
| 95 | #095 Aprimorando os Dicionários | Estruturas complexas, `copy()`, relatórios |
| 96 | #096 Função que calcula área | Primeira função com `def`, parâmetros |
| 97 | #097 Um print especial | Funções de formatação, reaproveitamento |
| 98 | #098 Função de Contador | Parâmetros, intervalos, `sleep()` |
| 99 | #099 Função que descobre o maior | Argumentos variáveis (`*args`) |
| 100 | #100 Funções para sortear e somar | Funções com listas, retorno de valores |
| 101 | #101 Funções para votação | Funções com `datetime`, retorno de classificação |
| 102 | #102 Função para Fatorial | Funções, parâmetro opcional, `return` |
| 103 | #103 Ficha do Jogador | Parâmetros opcionais, valores padrão |
| 104 | #104 Validando entrada de dados em Python | Função de validação, `isnumeric()`, tratamento de entrada |
| 105 | #105 Analisando e gerando Dicionários | Função que retorna dicionário, análise de notas |
| 106 | #106 Sistema interativo de ajuda em Python | `help()`, funções interativas, menu, cores no terminal |
| 107 | #107 Exercitando módulos em Python | Criar o próprio módulo, `import` |
| 108 | #108 Formatando Moedas em Python | Funções em módulo, formatação de moeda |
| 109 | #109 Formatando Moedas em Python (parte 2) | Módulos, parâmetros opcionais, evolução do código |
| 110 | #110 Reduzindo ainda mais seu programa | Pacotes, organização de código, refatoração |

---

## 🏆 Habilidades conquistadas ao final

- [ ] Entrada e saída de dados (`input`, `print`, f-strings)
- [ ] Tipos primitivos e conversões
- [ ] Operadores aritméticos, lógicos e de comparação
- [ ] Manipulação de strings (fatiamento e métodos)
- [ ] Uso de módulos da biblioteca padrão e externos
- [ ] Condicionais (`if`, `elif`, `else`) e condições aninhadas
- [ ] Laços `for` e `while`, com `break` e flags
- [ ] Tuplas, listas, matrizes e dicionários
- [ ] Funções (parâmetros, retorno, escopo, argumentos opcionais)
- [ ] Criação de módulos e pacotes próprios
- [ ] Versionamento com Git e GitHub

## 🚀 Próximos passos

- [ ] Tratamento de exceções (`try/except`)
- [ ] Arquivos (leitura e escrita)
- [ ] Programação orientada a objetos
- [ ] Testes automatizados (`pytest`)
- [ ] Um projeto integrador que una tudo o que foi aprendido

## 🤝 Contribuições e feedback

Sugestões de melhoria no código são bem-vindas! Abra uma *issue* ou envie um *pull request*.

## 🙏 Créditos

Exercícios e aulas do curso **Python 3 – Curso em Vídeo**, do professor **Gustavo Guanabara**. Todo o código deste repositório é de minha autoria, escrito durante o meu aprendizado.

## 👩‍💻 Autora

**Raya**
[LinkedIn](https://www.linkedin.com/in/SEU-PERFIL) · [GitHub](https://github.com/SEU-USUARIO)

---

⭐ Se este repositório te ajudou ou inspirou, deixe uma estrela!
