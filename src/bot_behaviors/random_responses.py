#########################################################################
#                                                                       #
#                       Grupo Developers                                #
#                                                                       #
#                GNU General Public License v3                          #
#                                                                       #
#########################################################################

import random


async def random_response(message):
    if 'devbot' in message.text.lower():
        response, reply = get_random_response()
        await message.reply(response, reply=reply)


def get_random_response():
    possible_responses = [
        ("Oi, você me chamou?", 1),
        ("*fumaça surgindo do além* QUEM OUSA ME INVOCAR!!!", 0),
        ("Não sei, não quero saber e tenho ódio de quem sabe, Pergunta pro outro bot lá o Daniel", 1),
        ("To dormindo!!!", 1),
        ("Que?", 1),
        ("Error: 41110xb0.. mentira eu não tenho erro nenhum, sou perfeito!", 0),
        ("JÁ QUE FALA TANTO DE MIM, PORQUE NÃO AJUDA A ME PROGRAMAR?", 1),
        ("Fala com os meus criadores, não pedi pra nascer...", 1),
        ("Eu gosto de batata!", 0),
        ("Poderia estar programando em vez de ficar falando comigo...", 1)
    ]
    return random.choice(possible_responses)
