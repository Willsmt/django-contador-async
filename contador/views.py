import asyncio
import time
from time import sleep

import httpx
from django.http import HttpResponse, JsonResponse

_background_tasks = set()  # segura referência forte até a task terminar (evita GC prematuro)


# --- Exercício oficial: contador visível no terminal + chamada HTTP, non-blocking ---

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            r = await client.get("https://httpbin.org/")
            print(r)
    except httpx.HTTPError as e:
        print(f"Falha na chamada HTTP em background: {e}")


def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    try:
        r = httpx.get("https://httpbin.org/", timeout=10.0)
        print(r)
    except httpx.HTTPError as e:
        print(f"Falha na chamada HTTP: {e}")


async def async_view(request):
    loop = asyncio.get_running_loop()
    task = loop.create_task(http_call_async())
    _background_tasks.add(task)
    task.add_done_callback(_background_tasks.discard)
    return HttpResponse("Non-blocking HTTP request")


def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")


# --- Complementar (bonus): contador que o CLIENTE espera, pra provar concorrência
# entre requisições diferentes, não fire-and-forget dentro da mesma requisição ---

async def contador_view(request):
    segundos = int(request.GET.get("segundos", 3))
    inicio = time.monotonic()

    await asyncio.sleep(segundos)

    decorrido = time.monotonic() - inicio
    return JsonResponse({
        "aguardado_segundos": segundos,
        "decorrido_real_segundos": round(decorrido, 2),
    })
