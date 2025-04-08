# 📌 Tarefa 1 - Implementação do Padrão MTV

## Objetivo
Implementar uma aplicação Django seguindo o padrão Model-Template-View para gerenciar serviços de uma clínica médica.

## Aplicação
- A aplicação devera ser chamada de `clinica`

## 🛠 Modelos Requeridos

### 1. Médico
- Campos obrigatórios:
  - `nome` (CharField)
  - `especialidade` (CharField com choices)
  - `crm` (CharField, único)
  - `email` (EmailField, opcional)

### 2. Consulta
- Campos obrigatórios:
  - `paciente` (CharField)
  - `data` (DateTimeField)
  - `medico` (ForeignKey para Médico) = **models.ForeignKey(Medico, on_delete=models.CASCADE)**
  - `status` (CharField com choices: ['agendado', 'realizado', 'cancelado'])

## 🌐 Views e URLs

### Views obrigatórias:
1. `listar_medicos` - Lista todos os médicos cadastrados
2. `criar_consulta` - Formulário para agendar nova consulta
3. `detalhes_consulta` - Exibe informações de uma consulta específica - faltou 

### URLs:
- `/medicos/` → Listagem de médicos
- `/consultas/nova/` → Agendamento
- `/consultas/<int:id>/` → Detalhes da consulta - faltou 

## 🎨 Templates
`Os templates devem ser colocados na pasta templates/clinica`

### Arquivos necessários:

1. `listar_medicos.html` - Deve mostrar:
   - Tabela com lista de médicos
   - Filtro por especialidade - faltou 

2. `form_consulta.html` - Deve conter:
   - Formulário com validação - faltou 
   - Mensagens de erro/sucesso - faltou 

## ⚠️ Validações

### Para Médico:
- CRM deve ter formato XX/XXXXX - faltou 
- Nome mínimo de 5 caracteres - faltou 

### Para Consulta:
- Não permitir agendamentos no passado - faltou 
