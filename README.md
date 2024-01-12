# Amigo Secreto

## Preparação
### Participantes
Preencha a lista de participantes no arquivo `participants.txt`. Adicione o email de cada participante à frente do nome, separando com vírgula.

 - ***OBS: Apenas um nome / email por linha***
 - *Exemplo:* `Pedro, pedro@email.com`

### Envio de email
 - Crie um arquivo na raiz do projeto com o nome `.env`
 - Copie o conteúdo do arquivo `.env.example` e cole no arquivo `.env`
 - Preencha o arquivo com as informações necessárias
  - Ex: `EMAIL_FROM=emailamigosecreto@email.com`
 - A senha do email deve ser uma senha de aplicativo gerada no seu servidor de email (talvez seja necessário habilitar a verificação em duas etapas).

## Execução
Execute o arquivo python `main.py`

```bash
python ./main.py
```

## Resultados do sorteio
Visualize os resultados do sorteio na pasta `output`