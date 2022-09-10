db.createUser(
    {
        user: "fastapi",
        pwd: "password12345",
        roles: [
            {role: "readWrite",
            db: "fastapi"}
        ]
    }
)

db.createCollection("users")
db.createCollection("posts")


// (create entries with user data)
db.users.insert([ {"username": "user1", "email": "user1@gmail.com"}, {"username": "user2", "email": "user2@gmail.com"} ])

// (create entries with posts)
db.posts.insert([ {"title": "post 1", "content": "Content of the post 1"}, {"title": "post 2", "content": "Content of the post 2"}])