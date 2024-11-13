from alembic_utils.pg_extension import PGExtension
from alembic_utils.pg_trigger import PGTrigger
from alembic_utils.pg_function import PGFunction

pgcrypto_ext = PGExtension(
    schema="public",
    signature="pgcrypto"
)

hash_password_function = PGFunction(
    schema="public",
    signature="hash_password_function()",
    definition=""" 
RETURNS TRIGGER
AS
$$
BEGIN
NEW.password := crypt(NEW.password, gen_salt('bf'));
RETURN NEW;
END;
$$
LANGUAGE plpgsql;
"""
)

hash_password_trigger = PGTrigger(
    schema="public",
    signature="hash_password_trigger",
    definition="""
BEFORE INSERT OR UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION hash_password_function();
""",
    on_entity="users"
)



"""
SELECT password = crypt(:password, password)
AS is_valid
FROM users
WHERE username = :username;
"""