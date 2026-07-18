import pytest
from django.test import AsyncClient, Client


@pytest.mark.asyncio
async def test_contador_view_retorna_tempo_decorrido():
    client = AsyncClient()
    response = await client.get("/contador/?segundos=1")
    assert response.status_code == 200
    data = response.json()
    assert data["aguardado_segundos"] == 1
    assert data["decorrido_real_segundos"] >= 1


@pytest.mark.asyncio
async def test_async_view_responde_sem_esperar_background():
    client = AsyncClient()
    response = await client.get("/contador/http-async/")
    assert response.status_code == 200
    assert response.content == b"Non-blocking HTTP request"


def test_sync_view_responde_apos_bloqueio():
    client = Client()
    response = client.get("/contador/http-sync/")
    assert response.status_code == 200
    assert response.content == b"Blocking HTTP request"
