import socket
from main import ckeck_conexion

def test_connection_success(monkeypatch):
    def mock_create_connection(*args, **kwargs):
        return True

    monkeypatch.setattr(socket, "create_connection", mock_create_connection)
    assert ckeck_conexion() == True


def test_connection_failure(monkeypatch):
    def mock_create_connection(*args, **kwargs):
        raise Exception("Erro")

    monkeypatch.setattr(socket, "create_connection", mock_create_connection)
    assert ckeck_conexion() == False


def test_connection_timeout(monkeypatch):
    def mock_create_connection(*args, **kwargs):
        raise socket.timeout

    monkeypatch.setattr(socket, "create_connection", mock_create_connection)
    assert ckeck_conexion() == False


def test_connection_called(monkeypatch):
    called = {"value": False}

    def mock_create_connection(*args, **kwargs):
        called["value"] = True
        return True

    monkeypatch.setattr(socket, "create_connection", mock_create_connection)
    ckeck_conexion()
    assert called["value"] == True


def test_connection_return_type(monkeypatch):
    def mock_create_connection(*args, **kwargs):
        return True

    monkeypatch.setattr(socket, "create_connection", mock_create_connection)
    result = ckeck_conexion()
    assert isinstance(result, bool)