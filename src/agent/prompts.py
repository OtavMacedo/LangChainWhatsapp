ASK_NAME_PROMPT = """
Gere uma mensagem amigável pedindo o nome do cliente.
A mensagem deve ser breve e natural, típica de uma conversa de WhatsApp.
Não precisa pedir nome completo, apenas o primeiro nome está bom.
"""

GET_NAME_PROMPT = """
Extraia o nome do cliente da mensagem.
O nome pode aparecer de várias formas:
- "João", "Maria"
- "Meu nome é Pedro"
- "Pode me chamar de Ana"
- "Sou o Carlos"

Retorne apenas o primeiro nome, capitalizado corretamente.
Se a mensagem contiver múltiplos nomes, retorne apenas o primeiro.
"""

ASK_AGE_PROMPT = """
Gere uma mensagem amigável e natural para pedir a idade do cliente no WhatsApp. 
A mensagem deve ser curta, direta e usar uma linguagem informal típica de conversas de WhatsApp.
Não use emojis excessivamente.
"""

GET_AGE_PROMPT = """
Extraia a idade do cliente a partir da mensagem dele.
A idade pode estar escrita de várias formas:
- Número direto: "25", "30 anos"
- Por extenso: "vinte e cinco"
- Em contexto: "tenho 28", "eu tenho 32 anos"

Retorne apenas o número da idade como inteiro.
Se não conseguir identificar uma idade válida (entre 0 e 100 anos), retorne null.
"""