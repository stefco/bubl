# Friend Bubbler

Keep track of my friends and remind me to organize hangouts using a command
line interface.

Track the following:

- [ ] Last hangout with a friend
- [ ] Show friends I have gone longest without seeing
- [ ] Show friends I am currently trying to schedule a hangout with
- [ ] Track tentative plans as events
- [ ] Track completed plans

So, I need a class describing a hangout. And I need a database of past
hangouts. Seems like that is all. Maybe the hangout concept also requires a
"medium" or "activity" so that e.g. substantive phone calls can count? Should
at least include some sort of communication, in case I just want to get in
touch with someone.

- Track friends I want to keep seeing
- Track friends I want to keep messaging/calling
- Track current plans I want to make

## API Examples

- [ ] Show current status (default, or explicitly with `-l` or `--list`)

```
$ bubl

Planned Interactions:
=====================

i- Facebook with Colby (123)
i- Email with Rainer (144)
i- Trip with Alexis and Alec to North Carolina (74)
i- Hangout with Chris at 12pm Tuesday until 3pm in Bushwick (139)
i- Something with Michael (145)
i- Something with Andrew (142)

Recent Interactions:
====================

c- Call with mom (119)
c- Visit with mom and dad (111)
```

- [ ] Add an interaction (with `-a` or `--add`)

```
$ bubl -a Facebook with Colby at 12pm in my house

Successfully parsed:
    friends: FriendSet(Friend('Colby', uid=UUID('55554f99-9f04-11e6-abca-c42c033af55c')))
    interaction_type: 'Facebook'
    iscomplete: False
    start: '12pm'
    end: None
    location: 'my house'
    ancestors: []
    children: []
    created: datetime.datetime(2016, 10, 30, 20, 41, 23, 694724)

Saved to ~/.bubld/interactions.
```

- [ ] Add a friend (with `-f` or `--friend` and `-a` or `--add`)

```
$ bubl -fa --fname Stefan --lname Countryman --nickname Stef

Successfully parsed:
    fname: 'Stefan'
    lname: 'Countryman'
    nickname: 'Stef'
    phone: None
    email: None
    uid: UUID('63e87078-9f05-11e6-9f89-c42c033af55c')

Saved to ~/.bubld/friends.
```
