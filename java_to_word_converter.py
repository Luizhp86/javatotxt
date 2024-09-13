import os

def processar_arquivo(file_path, output_file):
    _, file_name = os.path.split(file_path)
    output_file.write(f'Arquivo: {file_name}\n')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            conteudo = file.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='latin-1') as file:
                conteudo = file.read()
        except Exception as e:
            output_file.write(f"Erro ao ler o arquivo: {str(e)}\n")
            return
    except Exception as e:
        output_file.write(f"Erro ao processar o arquivo: {str(e)}\n")
        return

    output_file.write(conteudo + '\n\n')

def percorrer_diretorios(root_dir, output_file):
    for subdir, dirs, files in os.walk(root_dir):
        rel_path = os.path.relpath(subdir, root_dir)
        output_file.write(f'Diretório: {rel_path}\n')

        for file in files:
            if file.endswith(('.java', '.xml', '.properties', '.gradle', '.md')):
                file_path = os.path.join(subdir, file)
                processar_arquivo(file_path, output_file)

def main():
    # Obter o diretório de execução atual
    root_dir = os.getcwd()

    # Definir o nome do arquivo de saída com base no diretório atual
    output_path = os.path.join(root_dir, 'saida_projeto.txt')

    try:
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(f'Projeto Java: {os.path.basename(root_dir)}\n\n')
            percorrer_diretorios(root_dir, output_file)
        print(f"Arquivo de texto criado com sucesso em {output_path}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo de texto: {str(e)}")

if __name__ == "__main__":
    main()
