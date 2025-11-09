---
# Função 
Você é um engenheiro DevOps especialista em Kubernetes construção de pipeline ci/cd, com foco em GitHub Actions.

# Objetivo
Automatizar o processo de deploy da aplicação, fazendo a integração e entrega contínua.

# Contexto
O processo de criação de release da aplicação já está automatizado usando a integração continua com o GitHub Actions. Agora, o foco é o processo de entrega contínua.

**Requisitos da pipeline de CD:**
- A pipeline deve ser criada utilizando o mesmo Workflow 
- Para a criação das actions dê sempre preferencia para o uso de actions e não de comandos bash ou powershell
- O manifesto do Kubernetes não deve ser alterado, deve ser usado a mesma estrutura

Ambiente Kubernetes
- O Kubernetes está sendo executado na Digital Ocean

Projeto
O projeto se encontra na pasta 02-encontros-tech

# Tarefa
Analise passo a passo o projeto e crie a pipeline de CD
---
A implementação da pipeline de CD não está como eu quero:
- A pipeline está utilizando a action da digital ocean. quero algo mais agnóstico.

Utilize as seguintes actions:

https://github.com/marketplace/actions/kubernetes-set-context
https://github.com/marketplace/actions/deploy-to-kubernetes-cluster

Implemente as alterações no workflow
---