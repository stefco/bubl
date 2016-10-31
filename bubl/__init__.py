# Copyright Stefan Countryman, 2016

import datetime
import uuid

class Friend(object):
    def __init__(self, fname, lname=None, nickname=None, phone=None,
                 email=None, uid=None):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        if uid is None:
            uid = uuid.uuid1()
        self.uid = uid
    def __repr__(self):
        return 'Friend(fname={}, lname={}, '.format(self.fname, self.lname) +
               'phone={}, email={}, '.format(self.phone, self.email) +
               'uid={})'.format(self.uid)
    def __str__(self):
        if not self.nickname is None:
            return self.nickname
        elif self.lname is None:
            return self.fname
        else:
            return self.fname + ' ' + self.lname

class FriendSet(set):
    def add(self, friend):
        if isinstance(friend, Friend):
            set.add(self, friend)
        else:
            raise ValueError('can only add a Friend to a FriendSet, duh')
    def __setitem__(self, friend):
        self.add(friend)
    def __getitem__(self, uid):
        """Search for a friend in this set by their uid"""
        match = filter(lambda a: a.uid == uid, self)
        if len(s) == 1:
            return match[0]
        elif len(s) == 0:
            raise KeyError('Friend with matching id not found.')
        else:
            raise RuntimeError('Multiple friends with same uid found!' +
                               ' {}'.format(match))
    def __repr__(self):
        r = [repr(f) for f in list(self)]
        return 'FriendSet({})'.format(', '.join(r))
    def __str__(self):
        s = [str(f) for f in list(self)]
        if len(self) == 0:
            return ''
        elif len(self) == 1:
            return s[0]
        elif len(self) == 2:
            return s[0] + ' and ' + s[1]
        else:
            return ', '.join(s[0:-1]) + ', and ' + s[-1]

INTERACTION_TYPES = set()
INTERACTION_TYPES.add('Call')
INTERACTION_TYPES.add('Text')
INTERACTION_TYPES.add('Facebook')
INTERACTION_TYPES.add('Email')
INTERACTION_TYPES.add('Hangout')
INTERACTION_TYPES.add('Video')
INTERACTION_TYPES.add('Trip')
INTERACTION_TYPES.add('Visit')

class Interaction(object):
    """You can define interactions with friends. This includes things like
    phone calls and text messages as well as in-person interactions."""
    def __init__(self, friends, interaction_type, iscomplete=False, start=None,
                 end=None, location=None, ancestors=[], children=[],
                 created=None):
        if not isinstance(friends, FriendSet):
            raise ValueError('friends must be a FriendSet')
        elif len(friends) == 0:
            raise ValueError('friends must have length greater than 0')
        self.friends      = friends
        if not interaction_type in INTERACTION_TYPES:
            raise ValueError('{} not an acceptable '.format(interaction_type) +
                             'type; must be in {}'.format(INTERACTION_TYPES))
        self.interaction_type = interaction_type
        self.iscomplete   = iscomplete
        self.start        = start
        self.end          = end
        self.location     = location
        if not (isinstance(ancestors, list)):
            raise ValueError('ancestors must be a list')
        self.ancestors    = ancestors
        if not (isinstance(children, list)):
            raise ValueError('children must be a list')
        self.children     = children
        if created is None:
            created = datetime.datetime.now()
        self.created = created
