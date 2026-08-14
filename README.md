# javatotxt

Junta um projeto Java inteiro num único arquivo de texto. Percorre as pastas, pega o código-fonte e empilha tudo em `saida_projeto.txt`.

Repositório: [github.com/Luizhp86/javatotxt](https://github.com/Luizhp86/javatotxt)

---

## Para que serve

Quando você precisa do projeto *como um bloco só*, não como dezenas de arquivos soltos.

Casos em que isso ajuda:

- **colocar o código num LLM** (ChatGPT, Claude, Gemini, Ollama) para pedir resumo, refatoração, busca de bug ou documentação
- **revisão e auditoria** — um único arquivo para buscar, imprimir ou anexar
- **handoff** — mandar o fonte para alguém que não vai clonar o Git
- **indexar / RAG** — gerar um corpus textual do módulo Java

Não compila, não analisa e não formata como IDE. Só coleta e concatena.

---

## Como o motor funciona

Um script Python, sem dependência externa (`java_to_word_converter.py` — o nome é histórico; a saída é `.txt`).

1. Parte do diretório atual (`os.getcwd()`)
2. Caminha todas as subpastas (`os.walk`)
3. Para cada arquivo com extensão `.java`, `.xml`, `.properties`, `.gradle` ou `.md`:
   - escreve o nome do arquivo
   - escreve o conteúdo (UTF-8; se falhar, tenta Latin-1)
4. Grava `saida_projeto.txt` na raiz de onde você rodou o comando

Pastas de build (`target`, `build`) entram na caminhada se existirem. Se o volume ficar grande, rode a partir do módulo que importa (ex.: `src/`) ou limpe artefatos antes.

---

## Como usar

### Requisitos

- Python 3.6+
- Nenhuma biblioteca extra (`pip` não é necessário)

### Uso rápido

Coloque o script na raiz do projeto Java (ou copie o `.py` para lá) e rode:

```bash
git clone https://github.com/Luizhp86/javatotxt.git
cd /caminho/do/seu/projeto-java
python /caminho/do/javatotxt/java_to_word_converter.py
```

Ou, se o script já estiver na pasta do projeto:

```bash
python java_to_word_converter.py
```

Saída:

```
saida_projeto.txt
```

Cabeçalho típico:

```
Projeto Java: meu-servico

Diretório: .
Arquivo: pom.xml
...
Diretório: src\main\java\com\exemplo
Arquivo: Application.java
package com.exemplo;
...
```

### Ajustar o que entra

No próprio script, a linha que filtra extensões:

```python
if file.endswith(('.java', '.xml', '.properties', '.gradle', '.md')):
```

Inclua `.kt`, `.yml`, `.sql` etc. se o módulo tiver. Exclua `.xml` se não quiser `pom.xml` / `AndroidManifest` no pacote.

Para mudar o nome do arquivo de saída, edite `output_path` em `main()`.

---

## Limites (de propósito)

- Não ignora `target/`, `.git/` ou `node_modules/` — rode na pasta certa
- Não recebe caminho por argumento: o diretório de trabalho é a origem
- Arquivos binários das extensões listadas podem gerar lixo; o script tenta Latin-1 e segue
- Projetos enormes geram `.txt` grande demais para alguns modelos — nesse caso, rode por módulo

---

## Licença

MIT. Use e adapte à vontade.
