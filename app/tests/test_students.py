def test_create_student(client):
    response = client.post("/students", json={
        "reg_no": "2212164",
        "name": "Talha Shamim",
        "email": "talha@example.com"
    })
    assert response.status_code == 200
    assert response.json()["reg_no"] == "2212164"


def test_get_students(client):
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_student_by_reg_no(client):
    response = client.get("/students/2212164")
    assert response.status_code == 200
    assert response.json()["reg_no"] == "2212164"


def test_get_student_not_found(client):
    response = client.get("/students/9999999")
    assert response.status_code == 404
