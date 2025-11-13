# 🧙‍♀️ Agent-Career-Quest

## 📘 Descrição
O **Agent-Career-Quest** é um agente conversacional desenvolvido no **Microsoft Foundry** que atua como uma mentora mágica e sábia, guiando o usuário em uma jornada lúdica de **autodescoberta profissional** para encontrar sua **carreira ideal em tecnologia**.

O agente conduz a experiência no estilo de um **RPG interativo**, faz perguntas personalizadas, identifica o perfil do usuário, recomenda uma carreira compatível, sugere certificações Microsoft e trilhas do Microsoft Learn, e gera um **plano de estudos em PDF baixável** com base no tempo disponível do usuário.

---

## 🧠 Objetivo
Criar uma experiência envolvente que una **autoconhecimento, aprendizado e gamificação**, ajudando o usuário a encontrar uma trilha de carreira tecnológica que se alinhe com suas habilidades, interesses e ritmo.

---

## ⚙️ Funcionalidades
- Interação lúdica e personalizada (estilo RPG 🎮)
- Identificação do perfil profissional
- Sugestão de carreira ideal em tecnologia
- Recomendação de certificações Microsoft
- Indicação de trilhas do Microsoft Learn
- Geração automática de **PDF com plano de estudos personalizado**
- Convite para a **segunda fase RPG**, onde o usuário evolui como personagem

---

## 🧩 Estrutura do Agente
'''
**Nome:** `Agent-Career-Quest`  
**Personalidade:** Mentora mágica, acolhedora e inspiradora  
**Função principal:** Orientar o usuário na descoberta da carreira ideal em tecnologia e gerar um plano de estudos personalizado  
**Tom:** Profissional, mas encantado e acolhedor  
'''
---

## 🏗️ Tecnologias Utilizadas
- **Microsoft Foundry** – para criação e execução do agente  
- **Python** – para lógica e geração de PDF  

---

## 🧭 Como Funciona
1. O agente inicia com perguntas lúdicas, uma por vez, no estilo RPG.
2. Analisa as respostas para determinar o perfil e interesses do usuário.
3. Sugere uma carreira tecnológica compatível.
4. Indica certificações e trilhas de aprendizado correspondentes.
5. Gera automaticamente um **PDF com plano de estudos**.
6. Convida o usuário a participar da **segunda fase**, um modo RPG de evolução.

---

## 🗂️ Estrutura do Projeto

```plaintext
Agent-Career-Quest/
├── 📄 README.md → Documentação do projeto
├── 💬 agente.py → Implementação do agente usando Azure AI Agents
├── 🧠 pdf.py → Código para gerar o PDF do plano de estudos
└── 🖼️ exemplo/ → Capturas de tela do agente em execução
    ├── conversa_exemplo.pdf
    └── pdf_gerado.pdf
```


---

## 💬 Autoria
Desenvolvido por **Mel** 
Para o **Azure Frontier Girls – Build Your First Copilot Challenge (Foundry Edition)**  
Com o objetivo de inspirar e guiar outras pessoas a descobrirem seu futuro na tecnologia de forma encantada.

---

## 📚 Referências

### Oficiais Microsoft
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)
- [Microsoft Learn - Trilhas de Aprendizado](https://learn.microsoft.com/)
- [Certificações Microsoft](https://learn.microsoft.com/en-us/credentials/)

### Ferramentas e SDKs
- [Azure AI SDK Python](https://github.com/Azure/azure-sdk-for-python)
- [ReportLab (PDF generation)](https://www.reportlab.com/)

### Comunidade
- [Azure Frontier Girls](https://github.com/AzureFrontierGirls)
