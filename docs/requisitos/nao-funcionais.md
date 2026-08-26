# Requisitos Não-Funcionais (RNF)

Os requisitos não-funcionais definem os critérios de qualidade, desempenho e segurança que o IFVest deve atender para garantir uma operação robusta e confiável.

---

## 1. Desempenho e Capacidade

Foco na velocidade e na experiência de uso sob carga, conforme os estudos de **Testes Não-Funcionais**.

| ID | Requisito | Critério de Aceitação |
| :--- | :--- | :--- |
| **RNF01** | **Tempo de Resposta** | O sistema deve carregar as páginas principais em menos de 2 segundos em conexões de banda larga estáveis. |
| **RNF02** | **Carga e Escalabilidade** | A plataforma deve suportar até 500 usuários simultâneos sem degradação perceptível de performance (medido via JMeter). |
| **RNF03** | **Eficiência de Banco de Dados** | Consultas complexas ao banco de questões devem ser otimizadas para retornar resultados em menos de 500ms. |

---

## 2. Segurança e Privacidade

Foco na proteção de dados e conformidade legal, conforme o subprojeto de **Adequação à LGPD**.

| ID | Requisito | Critério de Aceitação |
| :--- | :--- | :--- |
| **RNF04** | **Proteção de Dados (LGPD)** | O sistema deve isolar os dados dos usuários através de *Security Rules* no Firebase, garantindo que um usuário acesse apenas suas próprias informações. |
| **RNF05** | **Criptografia de Senhas** | Nenhuma senha deve ser armazenada em texto plano; o sistema deve utilizar hash criptográfico (bcrypt) via Firebase Authentication. |
| **RNF06** | **Controle de Acesso** | O sistema deve implementar regras formais de controle de acesso (RBAC) para diferenciar permissões entre Alunos, Professores e Administradores. |

---

## 3. Usabilidade e Acessibilidade

Foco na inclusão e facilidade de aprendizado, conforme o subprojeto de **Acessibilidade**.

| ID | Requisito | Critério de Aceitação |
| :--- | :--- | :--- |
| **RNF07** | **Conformidade de Acessibilidade** | A interface deve atingir uma pontuação mínima de 90/100 em ferramentas de auditoria automatizada (Axe Core / Lighthouse). |
| **RNF08** | **Estética e Design** | O sistema deve seguir o guia de estilos e componentes definidos no Figma, garantindo consistência visual em todos os módulos. |
| **RNF09** | **Apreensibilidade** | Um novo usuário deve ser capaz de realizar o primeiro simulado ou quiz sem a necessidade de consultar manuais externos. |

---

## 4. Manutenibilidade e Confiabilidade

Foco na qualidade do código e facilidade de evolução, conforme o subprojeto de **Testes de Software**.

| ID | Requisito | Critério de Aceitação |
| :--- | :--- | :--- |
| **RNF10** | **Cobertura de Testes** | O código crítico do backend deve possuir uma cobertura de testes unitários superior a 80%. |
| **RNF11** | **Resiliência (Testes Mutantes)** | O sistema deve passar por testes de mutação (Stryker) para garantir que os testes existentes são capazes de detectar falhas reais no código. |
| **RNF12** | **Padronização de Código** | O projeto deve utilizar ESLint para garantir a conformidade com as regras de estilo de código estabelecidas pela equipe de frontend. |

---

## Ferramentas de Medição
O cumprimento destes requisitos é monitorado continuamente através das seguintes ferramentas:
*   **Performance:** JMeter e Selenium.
*   **Qualidade de Código:** Jest e Stryker.
*   **Acessibilidade:** Axe Core e ESLint.
*   **Segurança:** Firebase Security Rules.
