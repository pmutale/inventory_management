import os


def read_pgpass(dbname, host=None, port=None, engine=None, env=None):
    """
    Intends to read the .pgpass file stored on the local environment. Its the intentions
    that everyone make that file on their dev environment
    ==> http://www.postgresql.org/docs/9.3/static/libpq-pgpass.html
    :param engine:
    :param port:
    :param host:
    :param dbname: Database name
    :return:
    """
    import sys
    from pathlib import Path

    home_path = str(Path.home())

    no_database_found = """
        Your {path}/.pgpass file doesn"t have database "{dbname}" for host "{host}:{port}".

        To switch to a PostgreSQL database, add a line to the ~/.pgpass file
        containing it"s credentials.
        See http://www.postgresql.org/docs/9.3/static/libpq-pgpass.html
        """.format(
        dbname=dbname, path=home_path, host=host or "*", port=port or "*"
    )
    no_pgpass_notification = """
    You don"t have a {0}/.pgpass file so. Please create one!

    To switch to a PostgreSQL database, create a ~/.pgpass file
    containing it"s credentials.
    See http://www.postgresql.org/docs/9.3/static/libpq-pgpass.html
    """.format(
        home_path
    )

    try:
        pgpass = os.path.join(home_path, ".pgpass")
        pgpass_lines = open(pgpass).read().split()
    except IOError:
        # Print instructions
        print(no_pgpass_notification)
    else:
        for match in (dbname, "*"):
            for line in pgpass_lines:
                words = line.strip().split(":")
                if (
                    words[2] == match
                    and words[0] == (host or words[0])
                    and words[1] == (port or words[1])
                ):
                    return dict(
                        ENGINE=engine,
                        NAME=dbname,
                        USER=words[3],
                        PASSWORD=words[4],
                        HOST=words[0],
                        PORT=words[1],
                        TEST=dict(NAME='test_inventory')
                    )
        print(no_database_found)
    return sys.exit(
        "Error: You don't have a database setup, Please create a ~/.pgpass file "
    )
