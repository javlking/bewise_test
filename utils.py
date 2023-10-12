import aiohttp


# Отправка запроса на внешний API
async def get_q_from_url(url, questions_number):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url.format(amount=questions_number))

        if response.status == 200:
            questions = await response.json()

            return questions

