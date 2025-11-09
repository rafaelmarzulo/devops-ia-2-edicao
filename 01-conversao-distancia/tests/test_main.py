import pytest
import sys
import os

# Adicionar o diretório pai ao path para importar o main
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app


@pytest.fixture
def client():
    """Fixture para criar um cliente de teste do Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_homepage_loads(client):
    """Testa se a página inicial carrega corretamente"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'hostname' in response.data or b'Conversor' in response.data.lower()


def test_convert_api_valid_conversion(client):
    """Testa conversão válida via API"""
    response = client.post('/convert-api',
                          json={
                              'conversion_type': '1',  # Metro para Quilômetros
                              'value': 1000
                          },
                          content_type='application/json')

    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['result'] == 1.0  # 1000 metros = 1 km
    assert data['unit'] == 'quilômetros'


def test_convert_api_invalid_value(client):
    """Testa conversão com valor inválido"""
    response = client.post('/convert-api',
                          json={
                              'conversion_type': '1',
                              'value': 'invalid'
                          },
                          content_type='application/json')

    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data


def test_convert_api_missing_data(client):
    """Testa conversão com dados faltando"""
    response = client.post('/convert-api',
                          json={},
                          content_type='application/json')

    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data


def test_convert_api_invalid_conversion_type(client):
    """Testa conversão com tipo inválido"""
    response = client.post('/convert-api',
                          json={
                              'conversion_type': '99',  # Tipo inexistente
                              'value': 100
                          },
                          content_type='application/json')

    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data


def test_meter_to_kilometer_conversion(client):
    """Testa conversão de metro para quilômetro"""
    response = client.post('/convert-api',
                          json={
                              'conversion_type': '1',
                              'value': 5000
                          },
                          content_type='application/json')

    data = response.get_json()
    assert data['result'] == 5.0


def test_kilometer_to_meter_conversion(client):
    """Testa conversão de quilômetro para metro"""
    response = client.post('/convert-api',
                          json={
                              'conversion_type': '2',
                              'value': 2
                          },
                          content_type='application/json')

    data = response.get_json()
    assert data['result'] == 2000.0


def test_meter_to_feet_conversion(client):
    """Testa conversão de metro para pés"""
    response = client.post('/convert-api',
                          json={
                              'conversion_type': '5',
                              'value': 1
                          },
                          content_type='application/json')

    data = response.get_json()
    assert abs(data['result'] - 3.28084) < 0.0001  # Tolerância para float


def test_form_conversion_valid(client):
    """Testa conversão via formulário POST"""
    response = client.post('/',
                          data={
                              'selectTemp': '1',
                              'valorRef': '1000'
                          },
                          follow_redirects=True)

    assert response.status_code == 200
    assert b'quilômetros' in response.data.lower() or b'resultado' in response.data.lower()


def test_form_conversion_invalid_value(client):
    """Testa conversão via formulário com valor inválido"""
    response = client.post('/',
                          data={
                              'selectTemp': '1',
                              'valorRef': 'abc'
                          },
                          follow_redirects=True)

    assert response.status_code == 200
    # Deve retornar a página com mensagem de erro
    assert b'html' in response.data.lower()
