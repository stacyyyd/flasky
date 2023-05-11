# unit tests

# dont need to import pytest, if we want to skip our test we need to import pytest
def test_read_all_crystals_returns_empty_list(client):
    # arrange

    # act
    response = client.get("/crystals")
    response_body = response.get_json()


    # assert
    assert response_body == []
    assert response.status_code == 200

def test_read_crystal_by_id(make_two_crystals,client):
    response = client.get("/crystals/2")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id" : 2,
        "name": "garnet",
        "color": "red",
        "powers": "awesomeness"
    }

def test_create_crystal(client):
    response = client.post("/crystals", json={
        "name": "tigers eye",
        "color": "golden brown",
        "powers": "focus the mind"
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Yayyy Crystal tigers eye successfully created"