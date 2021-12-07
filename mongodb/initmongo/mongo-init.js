db.auth('admin', 'admin')

db = db.getSiblingDB('comicsdb')

db.createUser({
  user: 'bruno',
  pwd: 'bruno123',
  roles: [
    {
	    role: 'dbOwner',
	    db: 'comicsdb'
    }
  ]
});

db.auth('bruno', 'bruno12');
db.grantRolesToUser("bruno", [ { role: "read", db: "comicsdb" } ])