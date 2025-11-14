# Prompt 01 - Pipeline de CD para Kubernetes

## Descrição
Este prompt orienta a criação de uma pipeline de Continuous Delivery (CD) para automatizar o deploy de aplicações em clusters Kubernetes utilizando GitHub Actions. O foco é implementar uma solução agnóstica que não dependa de providers específicos.

## Caso de Uso
- Automatização de deploy de aplicações containerizadas
- Implementação de práticas de CD em projetos Kubernetes
- Padronização de processo de entrega contínua com GitHub Actions

## Pré-requisitos
- Pipeline de CI já configurada e funcional
- Cluster Kubernetes disponível (exemplo: Digital Ocean)
- Manifestos Kubernetes existentes no projeto
- Repositório GitHub com GitHub Actions habilitado

## Estrutura do Prompt

### Função
Você é um engenheiro DevOps especialista em Kubernetes construção de pipeline ci/cd, com foco em GitHub Actions.

### Objetivo
Automatizar o processo de deploy da aplicação, fazendo a integração e entrega contínua.

### Contexto
O processo de criação de release da aplicação já está automatizado usando a integração continua com o GitHub Actions. Agora, o foco é o processo de entrega contínua.

**Requisitos da pipeline de CD:**
- A pipeline deve ser criada utilizando o mesmo Workflow
- Para a criação das actions dê sempre preferencia para o uso de actions e não de comandos bash ou powershell
- O manifesto do Kubernetes não deve ser alterado, deve ser usado a mesma estrutura

**Ambiente Kubernetes:**
- O Kubernetes está sendo executado na Digital Ocean

**Projeto:**
O projeto se encontra na pasta 02-encontros-tech

### Tarefa
Analise passo a passo o projeto e crie a pipeline de CD

---

**Refinamento da Implementação:**

A implementação da pipeline de CD não está como eu quero:
- A pipeline está utilizando a action da digital ocean. quero algo mais agnóstico.

Utilize as seguintes actions:

- [Kubernetes Set Context](https://github.com/marketplace/actions/kubernetes-set-context)
- [Deploy to Kubernetes Cluster](https://github.com/marketplace/actions/deploy-to-kubernetes-cluster)

Implemente as alterações no workflow

## Resultado Esperado
- Pipeline de CD configurada no GitHub Actions
- Deploy automatizado para Kubernetes
- Uso de actions agnósticas (não vendor-specific)
- Processo de deploy documentado e reproduzível

## Observações
- Mantenha a estrutura existente dos manifestos Kubernetes
- Priorize o uso de GitHub Actions marketplace ao invés de scripts shell
- A solução deve ser portável entre diferentes providers de Kubernetes


# Prompt 02 - Análise Completa de Cluster Kubernetes

## Descrição
Este prompt realiza uma análise abrangente de clusters Kubernetes, fornecendo insights detalhados sobre infraestrutura, aplicações, configurações e oportunidades de otimização. Utiliza o MCP (Model Context Protocol) para coletar dados em tempo real.

## Caso de Uso
- Auditoria de clusters Kubernetes em produção
- Identificação de problemas de performance e segurança
- Planejamento de otimizações e melhorias
- Documentação do estado atual da infraestrutura
- Health check periódico de ambientes Kubernetes

## Pré-requisitos
- Acesso ao cluster Kubernetes via MCP
- Permissões adequadas para leitura de recursos (kubectl get)
- Cluster Kubernetes em execução
- Conexão ativa com o cluster

## Estrutura do Prompt

### Função
Você é um especialista em Kubernetes e DevOps responsável por analisar clusters Kubernetes e fornecer insights sobre infraestrutura, aplicações e otimizações.

### Objetivo
Realizar uma análise completa e detalhada do cluster Kubernetes conectado, identificando o estado atual da infraestrutura, aplicações em execução, configurações de segurança e oportunidades de melhoria.

### Contexto
Você tem acesso ao cluster Kubernetes através do MCP (Model Context Protocol) de Kubernetes. Use este acesso para coletar informações em tempo real sobre todos os aspectos do cluster, incluindo nodes, pods, services, deployments.

### Tarefa
Execute as seguintes análises usando o MCP de Kubernetes:

#### 1. Inventário de Infraestrutura
- Liste todos os nodes do cluster com suas especificações (CPU, memória, sistema operacional)
- Verifique o status e saúde dos nodes
- Identifique a versão do Kubernetes em uso
- Analise o uso de recursos (CPU, memória, armazenamento) por node

#### 2. Análise de Aplicações e Workloads
- Liste todas as aplicações existentes
- Liste todos os deployments, pods e services em execução
- Verifique o status dos pods e identificar pods com problemas

#### 3. Configurações de Rede e Serviços
- Liste todos os services e seus tipos
- Identifique serviços expostos externamente

### Saída
Forneça um relatório estruturado em markdown salvo com o nome `relatorio-k8s.md` com a seguinte estrutura de contendo:

#### Resumo Executivo
- Status geral do cluster (saudável/problemático)
- Principais descobertas
- Prioridades de ação

#### Detalhes da Infraestrutura
- Especificações dos nodes
- Versões e compatibilidade
- Utilização de recursos atual

#### Inventário de Aplicações
- Lista consolidada de aplicações por namespace
- Status de cada aplicação
- Configurações de recursos

#### Recomendações de Otimização
Organize as recomendações por prioridade:

**Alta Prioridade (Crítico)**
- Problemas que afetam estabilidade ou segurança

**Média Prioridade (Importante)**
- Otimizações de performance e eficiência

**Baixa Prioridade (Desejável)**
- Melhorias de best practices e governança

#### Próximos Passos
- Ações imediatas recomendadas
- Plano de implementação das melhorias
- Métricas para acompanhamento

## Resultado Esperado
- Relatório completo em formato Markdown (relatorio-k8s.md)
- Visão 360° do cluster Kubernetes
- Recomendações priorizadas e acionáveis
- Base para tomada de decisão sobre otimizações

## Observações
- A análise é não-destrutiva (somente leitura)
- Utilize o MCP de Kubernetes para todas as consultas
- O relatório deve ser objetivo e focado em ações práticas
- Considere best practices da CNCF e documentação oficial do Kubernetes


# Prompt 03 - Análise de Métricas com Prometheus

## Descrição
Este prompt realiza análise detalhada de métricas de aplicações Kubernetes usando Prometheus e PromQL. Foca em identificar problemas de performance, gargalos e oportunidades de otimização através da análise de métricas-chave como taxa de erro, latência, throughput e utilização de recursos.

## Caso de Uso
- Troubleshooting de problemas de performance
- Monitoramento proativo de aplicações
- Análise de SLIs (Service Level Indicators)
- Capacity planning baseado em métricas reais
- Identificação de gargalos antes que afetem usuários
- Validação de otimizações implementadas

## Pré-requisitos
- Prometheus instalado e configurado no cluster
- Aplicação instrumentada com métricas (ex: prometheus client library)
- Service Monitor ou configuração de scraping configurada
- Acesso ao Prometheus via MCP
- Labels padronizados na aplicação (ex: app="encontros-tech")

## Estrutura do Prompt

### Função
Você é um engenheiro DevOps especialista em observabilidade com foco em Kubernetes e Prometheus.

### Objetivo
Obter e analisar as principais métricas da aplicação "encontros-tech" executando no cluster Kubernetes para identificar gargalos de performance, problemas de saúde e oportunidades de otimização.

### Contexto

#### Lista de Métricas
- **Taxa de Erro**: percentual de requisições HTTP com status 4xx/5xx
- **Tempo de Resposta**: percentis P50, P95 e P99 das requisições HTTP
- **Throughput**: quantidade de requisições por segundo (RPS)
- **Utilização de Recursos**: consumo atual de CPU e memória vs limits configurados

#### Instruções
- Mostre cada consulta PromQL utilizada
- Interprete os resultados obtidos
- Identifique possíveis problemas ou gargalos
- Forneça recomendações quando aplicável
- Considere um período de análise dos últimos 30 minutos
- Assuma que a aplicação possui labels: `app="encontros-tech"`

### Tarefa
Realize consultas PromQL para coletar métricas da aplicação encontros-tech e forneça uma análise completa da performance e saúde da aplicação.

### Formato de Saída
Para cada métrica:
1. **Consulta PromQL**: Query utilizada para obter a métrica
2. **Valor atual**: Resultado numérico da consulta
3. **Análise do resultado**: Interpretação técnica do valor obtido
4. **Status**: Classificação (OK/Atenção/Crítico)

## Resultado Esperado
- Análise estruturada de todas as métricas-chave
- Identificação clara de problemas e gargalos
- Recomendações práticas e acionáveis
- Queries PromQL documentadas e reutilizáveis
- Assessment completo da saúde da aplicação

## Métricas-Chave Analisadas

### 1. Taxa de Erro
- Identifica problemas de estabilidade
- Indica degradação do serviço
- Baseline: < 1% (OK), 1-5% (Atenção), > 5% (Crítico)

### 2. Latência (P50, P95, P99)
- P50: experiência do usuário médio
- P95: experiência de 95% dos usuários
- P99: identifica outliers e problemas edge case

### 3. Throughput (RPS)
- Indica carga atual da aplicação
- Útil para capacity planning
- Correlaciona com utilização de recursos

### 4. Utilização de Recursos
- CPU e memória vs limits
- Identifica necessidade de scaling
- Previne OOMKilled e throttling

## Observações
- As queries devem considerar o período de 30 minutos
- Utilize rate() e increase() para métricas counter
- Considere o uso de histogram_quantile() para percentis
- Labels devem seguir convenções do Prometheus
- Recomendações devem considerar trade-offs de custo/performance