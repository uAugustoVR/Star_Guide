![Licença: CC BY-NC 4.0](https://img.shields.io/badge/Licença-CC%20BY--NC%204.0-blue)

# Star_Guide

**Star_Guide** é um projeto inovador que tem como objetivo fornecer um repositório de imagens do espaço com as devidas referências e descrições. Este projeto combina tecnologia e astronomia para entregar uma experiência única.

## 🌟 Funcionalidades

- Repositório de imagens espaciais com descrições detalhadas.
- Sistema de cadastro e login obrigatório para acessar o conteúdo.

## 🛠️ Tecnologias Utilizadas

- **Linguagem de Programação**: Python 3.10
- **Framework**: Django
- **Bibliotecas**: Listadas no arquivo `requirements.txt`

## 🚀 Como Instalar e Executar o Projeto

### Pré-requisitos

- Python 3.10
- Git
- Virtualenv (recomendado)

### Passos

1. Clone este repositório ou faça o download do arquivo `.zip`:
   ```bash
   git clone https://...
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd Star_Guide
   ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate    # Para Windows
   ```

4. Instale as dependências listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

5. Gere uma nova chave para o Django:
   ```bash
   cd scripts
   python secret_key_generator.py
   ```
   Copie e cole a toda a string da chave em um arquivo .env
   EX.: SECRET_KEY = key....

6. Execute o projeto:
   ```bash
   python manage.py runserver
   ```

7. Acesse o site em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## 📖 Como Usar

1. Cadastre-se no site ou faça login com suas credenciais.
2. Explore o repositório de imagens e aprenda mais sobre o espaço.
3. Para administrar o site e gerenciar o banco de dados, crie um superusuário com privilégios administrativos:
   ```bash
   python manage.py createsuperuser
   ```
   Siga as instruções para definir um nome de usuário, e-mail e senha. Após criado, acesse o painel administrativo em [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## 📜 Licença
Este projeto está licenciado sob a Creative Commons Atribuição-NãoComercial 4.0 Internacional (CC BY-NC 4.0).

📌 Isso significa que:
✅ Você pode usar, modificar e compartilhar o código somente para fins não comerciais.
🚫 O uso comercial deste código não é permitido sem a autorização do autor.
🔗 Para mais detalhes, consulte os termos completos da [LICENSE](LICENSE): [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

---

_Explore as estrelas com o **Star_Guide** e amplie seus horizontes!_
