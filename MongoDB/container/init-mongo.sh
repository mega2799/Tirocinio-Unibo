mongo -- "$MONGO_INITDB_DATABASE" <<EOF
    var rootUser = '$MONGO_INITDB_ROOT_USERNAME';
    var rootPassword = '$MONGO_INITDB_ROOT_PASSWORD';
    var admin = db.getSiblingDB('admin');
    admin.auth(rootUser, rootPassword);

    var user = '$ME_CONFIG_BASICAUTH_USERNAME';
    var passwd = '$(cat "$ME_CONFIG_BASICAUTH_PASSWORD")';
    db.createUser({user: user, pwd: passwd, roles: ["readWrite"]});
EOF
