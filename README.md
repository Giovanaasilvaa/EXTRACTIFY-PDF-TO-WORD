
<h1 align="center">📄 EXTRACTIFY - PDF TO WORD (PYTHON & FLASK)</h1>

<p align="center"><em>Converta PDFs em arquivos Word de forma rápida, simples e automática</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/último%20commit-junho-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/python-100%25-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/tecnologias-4-blue?style=flat-square" />
</p>

<h3 align="center">Tecnologias e ferramentas utilizadas:</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
</p>

---

## 📋 Sobre o Projeto

O **Extractify** é uma aplicação web desenvolvida com **Python (Flask)** que permite ao usuário fazer o **upload de um arquivo PDF** e **converter automaticamente o conteúdo para um arquivo Word (.docx)**.

Essa ferramenta realiza a **extração de texto de documentos PDF** usando a biblioteca **pdfplumber** e a **geração de arquivos Word** com a biblioteca **python-docx**.

> ⚠️ *O sistema faz apenas extração de texto simples. Layouts mais complexos, como tabelas ou imagens, podem não ser preservados.*

---

## 🧠 Funcionalidades

✅ Upload de arquivos PDF através de drag & drop ou botão  
✅ Extração automática de texto do PDF  
✅ Geração e download imediato do arquivo Word (.docx)  
✅ Feedback de progresso (mensagem de status)  
✅ Interface web leve e responsiva

---

## 🛠 Estrutura do Projeto

<pre>
/app.py → Backend Flask responsável pelas rotas e lógica de conversão
/assets → Arquivos estáticos como HTML, CSS, JS e vídeos
/assets/css → Estilo visual da página
/assets/js → Scripts JavaScript de interação (upload, drag & drop, etc)
/assets/videos → Vídeo de demonstração exibido na página
</pre>

---

## 🚀 Como Executar o Projeto

1. **Clone este repositório:**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/macOS
```

3. **Instale as dependências:**

```bash
pip install flask flask_cors pdfplumber python-docx
```

4. **Execute o servidor Flask:**

```bash
python app.py
```

5. **Acesse no navegador:**

```
http://localhost:5000
```

---

## 📂 Exemplo de Uso

✅ Faça upload de um arquivo PDF  
✅ O sistema irá processar  
✅ O download do Word começará automaticamente

---

## ⚠️ Limitações

- Não mantém formatação de layout (somente texto simples)
- Arquivos PDF muito grandes podem demorar mais

---

## 📦 Versão

1.0.0

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

## 📬 Contato

Giovana Marques Silva  
giovanamarquessilva24@gmail.com
