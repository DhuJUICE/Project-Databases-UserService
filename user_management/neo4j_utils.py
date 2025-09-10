from neo4j import GraphDatabase
from django.conf import settings


def create_developer_node(dev_id, first_name, last_name, email, username):
    """
    Creates a Developer node in Neo4j and closes the connection afterward.
    """
    driver = GraphDatabase.driver(
        settings.NEO4J_URI,
        auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
    )

    try:
        with driver.session() as session:
            session.run(
                """
                CREATE (d:Developer {
                    id: $id,
                    first_name: $first_name,
                    last_name: $last_name,
                    email: $email,
                    username: $username
                })
                """,
                id=dev_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username
            )
    finally:
        driver.close()  # Ensures the driver is always closed


def get_developers(exclude_username):
    """
    Fetch all developers except the one with the given username.

    Args:
        exclude_username (str): The username to exclude.

    Returns:
        list[dict]: A list of developers (dicts with id, first_name, last_name, email, username).
    """
    driver = GraphDatabase.driver(
        settings.NEO4J_URI,
        auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
    )

    query = """
    MATCH (d:Developer)
    WHERE d.username <> $exclude_username
    RETURN d.id AS id,
           d.first_name AS first_name,
           d.last_name AS last_name,
           d.email AS email,
           d.username AS username
    """

    try:
        with driver.session() as session:
            result = session.run(query, {"exclude_username": exclude_username})
            developers = [
                {
                    "id": record["id"],
                    "first_name": record["first_name"],
                    "last_name": record["last_name"],
                    "email": record["email"],
                    "username": record["username"],
                }
                for record in result
            ]
            return developers
    finally:
        driver.close()  # Ensures the driver is always closed
