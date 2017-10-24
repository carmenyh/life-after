from ..database import registrationservice

def test_unvalidated_valid_user():
    username_in = "Janedoe"
    password_in = "Passw0rd"
    token_in = registrationservice.register({"username":username_in, "password":password_in})
    (username_out, password_out, validated_out, token_out) = registrationservice.get_registered_user(username_in)
    assert username_in == username_out
    assert password_in == password_out # TODO will need to check the hash when that is done
    assert token_in == token_out
    assert validated_out == "N"

if __name__ == '__main__':
    test_unvalidated_valid_user()
