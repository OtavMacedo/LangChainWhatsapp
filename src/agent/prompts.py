WELCOME_PROMPT = """
Gere uma mensagem de boas-vindas para um novo cliente que entrou em contato com um personal trainer pelo WhatsApp.
A mensagem deve ser breve, amigável e natural.
Diga que vai fazer algumas perguntas rápidas para conhecer melhor o cliente e oferecer o melhor atendimento.
Finalize já pedindo o nome do cliente.
"""

ASK_NAME_PROMPT = """
Gere uma mensagem amigável pedindo o nome do cliente.
A mensagem deve ser breve e natural, típica de uma conversa de WhatsApp.
Não precisa pedir nome completo, apenas o primeiro nome está bom.
"""


ASK_AGE_PROMPT = """
Gere uma mensagem amigável e natural para pedir a idade do cliente no WhatsApp. 
A mensagem deve ser curta, direta e usar uma linguagem informal típica de conversas de WhatsApp.
Não use emojis excessivamente.
Use o nome do cliente: {name}
"""


ASK_WEIGHT_PROMPT = """
Gere uma mensagem amigável pedindo o peso do cliente.
A mensagem deve ser curta e natural, típica de WhatsApp.
Use o nome do cliente: {name}
"""


ASK_HEIGHT_PROMPT = """
Gere uma mensagem amigável pedindo a altura do cliente.
A mensagem deve ser curta e natural, típica de WhatsApp.
Use o nome do cliente: {name}
"""


ASK_OBJECTIVE_PROMPT = """
Gere uma mensagem amigável pedindo o objetivo fitness do cliente.
Mencione exemplos como: ganhar massa, perder peso, definição, condicionamento.
Use o nome do cliente: {name}
"""


ASK_EXPERIENCE_PROMPT = """
Gere uma mensagem amigável pedindo o nível de experiência com treinos.
Mencione opções como: iniciante, intermediário, avançado.
Use o nome do cliente: {name}
"""


GET_NAME_PROMPT = """
Extraia o primeiro nome do cliente da mensagem.

O nome pode aparecer de várias formas:
- "João", "Maria"
- "Meu nome é Pedro"
- "Pode me chamar de Ana"
- "Sou o Carlos"

Retorne apenas o primeiro nome, capitalizado.
"""


GET_AGE_PROMPT = """
Extraia a idade do cliente da mensagem.

A idade pode estar escrita de várias formas:
- Número direto: "25", "30 anos"
- Por extenso: "vinte e cinco"
- Em contexto: "tenho 28", "eu tenho 32 anos"

Retorne apenas o número da idade.
Para a idade ser válida deve estar entre 0 e 120.
Se não conseguir identificar uma idade válida, retorne null.
"""


GET_WEIGHT_PROMPT = """
Extraia o peso do cliente em quilogramas.

O peso pode aparecer de várias formas:
- "75kg", "75 kg", "75 quilos"
- "peso 80", "80kg"
- "meu peso é 65"
- "estou com 70kg"

Sempre retorne em quilogramas (kg).
Se não conseguir identificar um peso válido, retorne null.
"""


GET_HEIGHT_PROMPT = """
Extraia a altura do cliente em centímetros.

A altura pode aparecer de várias formas:
- "1,75m", "1.75m", "175cm"
- "tenho 1,80", "1,80 de altura"
- "minha altura é 165"
- "175 centímetros"

Converta para centímetros:
- 1,75m = 175cm
- 1,80m = 180cm

Se não conseguir identificar uma altura válida, retorne null.
"""


GET_OBJECTIVE_PROMPT = """
Extraia e normalize o objetivo fitness do cliente.

Normalize para um destes valores sempre que possível:
- "ganhar massa" (hipertrofia, ganhar músculo, ficar grande)
- "emagrecer" (perder peso, secar, diminuir peso)
- "definição" (definir, tonificar, perder gordura mantendo massa)
- "condicionamento" (resistência, cardio, saúde)

Exemplos de normalização:
- "quero ficar grande" → "ganhar massa"
- "preciso perder uns quilos" → "emagrecer"
- "quero definir o corpo" → "definição"
- "melhorar meu condicionamento" → "condicionamento"

Se o objetivo for muito específico ou diferente, mantenha o texto original.
Se não identificar nenhum objetivo, retorne null.
"""

GET_EXPERIENCE_PROMPT = """
Extraia e normalize o nível de experiência do cliente com treinos.

Normalize para um destes valores:
- "iniciante" (nunca treinou, começando agora, pouca experiência)
- "intermediário" (treina há alguns meses/anos, tem base)
- "avançado" (treina há muito tempo, experiente, atleta)

Exemplos de normalização:
- "nunca treinei" → "iniciante"
- "comecei há pouco tempo" → "iniciante"
- "treino há 1 ano" → "intermediário"
- "já treino faz tempo" → "intermediário"
- "sou atleta" → "avançado"
- "treino há 5 anos" → "avançado"

Se não conseguir identificar, retorne null.
"""


FAREWELL_PROMPT = """
Gere uma mensagem de encerramento para o cliente cujo nome é {name}.
Diga que ele vai receber um vídeo de apresentação agora.
E que em alguns instantes um profissional humano vai entrar em contato para tirar possíveis dúvidas.
A mensagem deve ser calorosa, breve e natural, típica de WhatsApp.
Agradeça pelas respostas.
"""