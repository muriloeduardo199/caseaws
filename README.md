Subindo um repositorio para o GIT

-Primeiro vc usa o comando no terminal ao qual vai gerar uma pasta oculta.
 
 git init


-Depois usa o comando para poder enviar para o diretorio staging area onde prepara os arquivos para o proximo comit usando :

git add . ou git add <nome do arquivo>


-Pode usar o comando para verificar o status dos arquivos ou monitoramento dos mesmos

git status


-Usa se 'git remote' para gerenciar os repositorios monitarados 

git remote add origin <endereço>


-Por ultimo usa se o git push para encaminhar as mudancas commitadas para o GitHub

git push -u origin master


-Caso nao esteja conectado na sua conta voce precisa se conectar a ela usando os comandos:


git config --global user.name "<nome>"
git config --global user.email "<email>"


-Caso queira verificar qual branch esta:

git branch


-Se precisar mudar o nome da branch use o comando:

git branch -m <nome da branch que vc quer >