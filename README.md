# ✍️ Django Blog Engine - Automação com Signals e Testes de Integridade

Este projeto demonstra a implementação de funcionalidades inteligentes e automações no back-end utilizando **Django Signals** e a garantia de qualidade através de **Testes Unitários/Integridade**. O foco principal é a consistência de dados e a experiência do administrador.

---

# 📝 Resumo (Resume)
Neste projeto, desenvolvi um sistema de postagens onde a lógica de criação de **Slugs** (URLs amigáveis) é automatizada via `pre_save` signals, garantindo que todo post possua um identificador único sem intervenção manual. Para assegurar que essa automação e a persistência no banco de dados não quebrem em futuras atualizações, implementei uma suíte de testes utilizando o `TestCase` do Django. No painel administrativo, utilizei recursos avançados como `prepopulated_fields` e `list_editable` para otimizar o fluxo de trabalho editorial.



## 🚀 Tecnologias e Ferramentas (Tech Stack)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Pytest](https://img.shields.io/badge/Testing-Django_TestCase-green?style=for-the-badge)](https://docs.djangoproject.com/en/stable/topics/testing/)

## 📋 Funcionalidades em Destaque
* **Automação via Signals:** Uso do decorador `@receiver(pre_save)` para interceptar o salvamento de objetos e gerar slugs automaticamente com `slugify`.
* **Testes de Integridade:** Implementação de métodos de teste para validar a criação de objetos e o comportamento esperado das automações de banco de dados.
* **Gestão Editorial Avançada:** Configuração do `PostAdmin` com campos editáveis diretamente na lista (`list_editable`) e preenchimento dinâmico de slugs em tempo real.
* **Ciclo de Vida do Modelo:** Diferenciação entre `auto_now_add` (criação) e `auto_now` (atualização) para controle total da cronologia das postagens.
* **UX de Admin Profissional:** Inclusão de filtros laterais e campos de busca otimizados para grandes volumes de conteúdo.
* **Consistência de Dados:** Validação de escolhas limitadas via `STATUS_CHOICES` (Rascunho/Publicado).



---

# 👨‍💻 Sobre mim (About Me)
Olá, meu nome é **Kaio**, tenho 22 anos. Como meu foco é o **Back-End com Python**, entendo que automação e testes são o que diferencia um sistema amador de um produto de mercado. No Front-End com **Cypress**, eu testava a interface; aqui no Back-End, testo a integridade dos dados e a lógica de negócio. Usar Signals me permite manter os modelos limpos, enquanto os TestCases me dão a tranquilidade necessária para escalar o projeto com segurança.

### Entre em contato (Contact me)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=092E20)](https://linkedin.com/in/kaio-grativol-baldo-071a74150/)
[![Instagram](https://img.shields.io/badge/Instagram-000?style=for-the-badge&logo=instagram&logoColor=092E20)](https://www.instagram.com/kaiull__/)
[![GitHub](https://img.shields.io/badge/Github-000?style=for-the-badge&logo=github&logoColor=092E20)](https://github.com/SeuUsuarioAqui)

---
*Projeto desenvolvido para consolidar o uso de automações de modelo e boas práticas de testes automatizados no Django.*
