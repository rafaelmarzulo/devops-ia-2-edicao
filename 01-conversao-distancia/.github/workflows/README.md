# CI/CD Pipeline - Conversão de Distância

Este diretório contém o workflow de CI/CD automatizado para a aplicação de conversão de distâncias.

## 📋 Visão Geral

O pipeline é executado automaticamente em:
- **Push** para branches `main` e `develop`
- **Pull Requests** para a branch `main`

## 🔄 Jobs do Pipeline

### 1. Quality & Tests
- Checkout do código
- Configuração do Python 3.12
- Instalação de dependências
- Lint com flake8 (verificação de sintaxe e estilo)
- Execução de testes unitários com pytest
- Geração de relatório de cobertura

### 2. Security Scan
- Scan de vulnerabilidades no código fonte usando Trivy
- Upload dos resultados para GitHub Security
- Detecção de vulnerabilidades CRITICAL e HIGH

### 3. Build Docker Image
- Build da imagem Docker com Buildx
- Cache otimizado para acelerar builds
- Teste funcional da imagem (health check HTTP)
- Scan de segurança da imagem Docker com Trivy

### 4. Deploy (apenas branch main)
- Login no Docker Hub
- Build e push da imagem com tags:
  - `latest` (branch principal)
  - `main-<sha>` (commit específico)
  - `main` (nome da branch)
- Upload apenas em push para a branch `main`

## 🔐 Secrets Necessários

Configure os seguintes secrets no repositório GitHub:

| Secret | Descrição |
|--------|-----------|
| `DOCKER_USERNAME` | Usuário do Docker Hub |
| `DOCKER_PASSWORD` | Token de acesso do Docker Hub |

### Como Configurar Secrets

1. Acesse: `Settings` → `Secrets and variables` → `Actions`
2. Clique em `New repository secret`
3. Adicione cada secret necessário

### Gerando Token do Docker Hub

1. Acesse: https://hub.docker.com/settings/security
2. Clique em `New Access Token`
3. Dê um nome (ex: `github-actions`)
4. Copie o token gerado
5. Use como valor do secret `DOCKER_PASSWORD`

## 🎯 Quality Gates

### Lint (flake8)
- Erros críticos de sintaxe bloqueiam o pipeline
- Avisos não bloqueiam mas são reportados

### Testes
- Cobertura de código gerada automaticamente
- Relatórios enviados para Codecov (se configurado)

### Security
- Scan de vulnerabilidades em código e dependências
- Scan de vulnerabilidades na imagem Docker
- Resultados integrados ao GitHub Security

## 🚀 Como Usar

### Desenvolvimento Local

```bash
# Instalar dependências
pip install -r requirements.txt
pip install flake8 pytest pytest-cov

# Executar lint
flake8 .

# Executar testes
pytest tests/ -v --cov=.

# Build Docker local
docker build -t conversao-distancia:local .

# Executar container
docker run -p 8000:8000 conversao-distancia:local
```

### Deploy Manual

```bash
# Build e push manual (caso necessário)
docker build -t seu-usuario/conversao-distancia:v1.0 .
docker push seu-usuario/conversao-distancia:v1.0

# Atualizar manifesto Kubernetes
kubectl apply -f k8s/manifesto.yaml
```

## 📊 Monitoramento

### Status do Pipeline
- Veja o status em: `Actions` tab do repositório
- Cada job mostra logs detalhados
- Falhas são notificadas via email/notificações do GitHub

### Métricas
- Tempo de build
- Cobertura de testes
- Vulnerabilidades detectadas
- Tamanho da imagem Docker

## 🔧 Customização

### Adicionar Novos Testes
1. Criar arquivos `test_*.py` em `tests/`
2. Usar fixtures do pytest
3. Pipeline executará automaticamente

### Adicionar Novos Ambientes
1. Duplicar job `deploy`
2. Adicionar condições específicas
3. Configurar secrets por ambiente

### Modificar Quality Gates
Edite `.flake8` para ajustar regras de lint:
```ini
[flake8]
max-line-length = 127
max-complexity = 10
```

## 📝 Troubleshooting

### Build Falha
- Verifique logs do job específico
- Confirme que todos os testes passam localmente
- Verifique se dependências estão atualizadas

### Deploy Falha
- Confirme que secrets estão configurados
- Verifique credenciais do Docker Hub
- Confirme que o registry está acessível

### Testes Falham
- Execute localmente: `pytest tests/ -v`
- Verifique logs detalhados no GitHub Actions
- Confirme que ambiente de teste está correto

## 🔗 Recursos Adicionais

- [GitHub Actions Documentation](https://docs.github.com/actions)
- [Docker Build Push Action](https://github.com/docker/build-push-action)
- [Trivy Scanner](https://github.com/aquasecurity/trivy)
- [pytest Documentation](https://docs.pytest.org/)
