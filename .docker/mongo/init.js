db.auth('mozio-admin', 'mozio-admin')

db.getSiblingDB('mozio').createUser(
    {
        user: "mozio-dev",
        pwd: "mozio-dev",
        roles: [{role: "readWrite", db: "mozio"}]
    }
)