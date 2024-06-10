## Enunciado

Implementar a Máquina de Turing (com uma fita) para realizar o reconhecimento de sentenças de linguagens quaisquer, cuja função programa (função de transição) seja lida a partir de um arquivo texto.

A interface da implementação deverá permitir selecionar o arquivo a ser lido, assim como a sentença a ser reconhecida pela Máquina de Turing.

A cada passo da execução deve ser exibido, na tela, o número do passo, o símbolo lido da
entrada e a fita.

Ao final, indicar se a sentença foi aceita ou rejeitada pela Máquina de Turing.

---

### To-Do

- A idéia é tratar o arquivo de interface gráfica (GUI) como um main, e dentro dele fazer os imports de outros arquivos que possuem as funções necessárias para as execuções que o enunciado pede.

- [x] Montar interface
    - Janela superior: mostra arquivos com extensão txt disponíveis no diretório
    - Janela inferior: selecionar o arquivo.txt
    - Após selecionar: as duas janelas são limpas e aparece uma janela que mostra as sentenças lidas do arquivo selecionado.
    - Aparece também um campo que pede para o usuário inserir a sentença que vai ser classificada pela Máquina de Turing
    - Após clicar em "iniciar" deveriam aparecer os passos, mas aqui está acontecendo algum problema provavelmente na leitura
- [x] Ler arquivos txt