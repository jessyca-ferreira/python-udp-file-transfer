# python-rdt-server
**_Observação_**: no vídeo que acompanha esta entrega, _todos_ os membros da equipe participaram do vídeo, na seguinte ordem: Pedro Martins, Letícia Barbosa, Jéssyca Ferreira, Paulo Rafael, Maike Henrique, Beatriz Oliveira.

## Instruções de execução

* Execute `server.py` para incializar o servidor em uma janela do terminal
* Execute `client.py` para inicializar o cliente em uma janela do terminar
  * A nossa implementação suporta múltiplos clientes. Para inicializar um cliente adicional, basta executar `client.py` em uma janela diferente do terminal
* No cliente, insira comandos ou mensagens que serão enviadas ao servidor para que este realize o broadcast para todos os clientes conectados
  * Para inciar a conexão, o cliente precisa utilizar o comando "hi, meu nome eh <nome_do_usuario>
  * Em seguida, estará apto para receber ou enviar mensagens.
  * Ao receber ou enviar uma mensagem, será impresso no terminal servidor a etapa do protocolo RDT realizada.
  * Além disso, temos dois comandos especiais: 'bye', responsável por desconectar um cliente, tornando-o incapaz de receber ou enviar mensagens e finalizando sua execução, e 'list', que retorna a lista de conexões ativas
* O arquivo `rdt.py` não precisa ser executado, pois foi importado em ambos `client.py` e `server.py`


## Equipe 4

Beatriz de Oliveira Barros - bob@cin.ufpe.br

Jessyca Ferreira da Silva -	jfs7@cin.ufpe.br

Letícia Barbosa Lins Pedrosa - lblp@cin.ufpe.br

Maike Henrique Rodrigues de Menezes	- mhrm2@cin.ufpe.br

Paulo Rafael Barros de Aguiar	- prba@cin.ufpe.br

Pedro Martins da Silva - pms5@cin.ufpe.br
