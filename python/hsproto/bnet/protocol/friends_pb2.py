# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/protocol/friends.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .. import protocol_0_pb2 as bnet_dot_protocol__0__pb2
from . import attribute_pb2 as bnet_dot_protocol_dot_attribute__pb2
from . import invitation_pb2 as bnet_dot_protocol_dot_invitation__pb2
from .. import protocol_1_pb2 as bnet_dot_protocol__1__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/protocol/friends.proto',
  package='bnet.protocol.friends',
  syntax='proto2',
  serialized_pb=_b('\n\x1b\x62net/protocol/friends.proto\x12\x15\x62net.protocol.friends\x1a\x15\x62net/protocol_0.proto\x1a\x1d\x62net/protocol/attribute.proto\x1a\x1e\x62net/protocol/invitation.proto\x1a\x15\x62net/protocol_1.proto\"x\n\x11\x41ssignRoleRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\ttarget_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x0c\n\x04role\x18\x03 \x03(\x05\"\xc7\x01\n\x06\x46riend\x12#\n\x02id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x35\n\tattribute\x18\x02 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12\x0c\n\x04role\x18\x03 \x03(\r\x12\x12\n\nprivileges\x18\x04 \x01(\x04\x12\x18\n\x10\x61ttributes_epoch\x18\x05 \x01(\x04\x12\x11\n\tfull_name\x18\x06 \x01(\t\x12\x12\n\nbattle_tag\x18\x07 \x01(\t\"u\n\x12\x46riendNotification\x12-\n\x06target\x18\x01 \x01(\x0b\x32\x1d.bnet.protocol.friends.Friend\x12\x30\n\x0fgame_account_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\"m\n\x14GenericFriendRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\ttarget_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\"M\n\x15GenericFriendResponse\x12\x34\n\rtarget_friend\x18\x01 \x01(\x0b\x32\x1d.bnet.protocol.friends.Friend\"Y\n\x19SubscribeToFriendsRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x11\n\tobject_id\x18\x02 \x01(\x04\"[\n\x1bUnsubscribeToFriendsRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x11\n\tobject_id\x18\x02 \x01(\x04\"\x88\x01\n\x1dUpdateFriendStateNotification\x12\x35\n\x0e\x63hanged_friend\x18\x01 \x01(\x0b\x32\x1d.bnet.protocol.friends.Friend\x12\x30\n\x0fgame_account_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\"\xc2\x01\n\x18UpdateFriendStateRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\ttarget_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x35\n\tattribute\x18\x03 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12\x18\n\x10\x61ttributes_epoch\x18\x04 \x01(\x04\"y\n\x12ViewFriendsRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\ttarget_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x0c\n\x04role\x18\x03 \x03(\r\"E\n\x13ViewFriendsResponse\x12.\n\x07\x66riends\x18\x01 \x03(\x0b\x32\x1d.bnet.protocol.friends.Friend\"\x9e\x01\n\x10\x46riendInvitation\x12\x16\n\x0e\x66irst_received\x18\x01 \x01(\x08\x12\x0c\n\x04role\x18\x02 \x03(\r2d\n\rfriend_invite\x12$.bnet.protocol.invitation.Invitation\x18g \x01(\x0b\x32\'.bnet.protocol.friends.FriendInvitation\"\x94\x01\n\x16InvitationNotification\x12\x38\n\ninvitation\x18\x01 \x01(\x0b\x32$.bnet.protocol.invitation.Invitation\x12\x30\n\x0fgame_account_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x0e\n\x06reason\x18\x03 \x01(\r\"\x9e\x02\n\x16\x46riendInvitationParams\x12\x14\n\x0ctarget_email\x18\x01 \x01(\t\x12\x19\n\x11target_battle_tag\x18\x02 \x01(\t\x12\x1a\n\x12inviter_battle_tag\x18\x03 \x01(\t\x12\x19\n\x11inviter_full_name\x18\x04 \x01(\t\x12\x1c\n\x14invitee_display_name\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x03(\r2p\n\rfriend_params\x12*.bnet.protocol.invitation.InvitationParams\x18g \x01(\x0b\x32-.bnet.protocol.friends.FriendInvitationParams\"\xc8\x02\n\x1aSubscribeToFriendsResponse\x12\x13\n\x0bmax_friends\x18\x01 \x01(\r\x12 \n\x18max_received_invitations\x18\x02 \x01(\r\x12\x1c\n\x14max_sent_invitations\x18\x03 \x01(\r\x12!\n\x04role\x18\x04 \x03(\x0b\x32\x13.bnet.protocol.Role\x12.\n\x07\x66riends\x18\x05 \x03(\x0b\x32\x1d.bnet.protocol.friends.Friend\x12>\n\x10sent_invitations\x18\x06 \x03(\x0b\x32$.bnet.protocol.invitation.Invitation\x12\x42\n\x14received_invitations\x18\x07 \x03(\x0b\x32$.bnet.protocol.invitation.Invitation')
  ,
  dependencies=[bnet_dot_protocol__0__pb2.DESCRIPTOR,bnet_dot_protocol_dot_attribute__pb2.DESCRIPTOR,bnet_dot_protocol_dot_invitation__pb2.DESCRIPTOR,bnet_dot_protocol__1__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ASSIGNROLEREQUEST = _descriptor.Descriptor(
  name='AssignRoleRequest',
  full_name='bnet.protocol.friends.AssignRoleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.friends.AssignRoleRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='bnet.protocol.friends.AssignRoleRequest.target_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.AssignRoleRequest.role', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=283,
)


_FRIEND = _descriptor.Descriptor(
  name='Friend',
  full_name='bnet.protocol.friends.Friend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.friends.Friend.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.friends.Friend.attribute', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.Friend.role', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='privileges', full_name='bnet.protocol.friends.Friend.privileges', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes_epoch', full_name='bnet.protocol.friends.Friend.attributes_epoch', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='bnet.protocol.friends.Friend.full_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_tag', full_name='bnet.protocol.friends.Friend.battle_tag', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=485,
)


_FRIENDNOTIFICATION = _descriptor.Descriptor(
  name='FriendNotification',
  full_name='bnet.protocol.friends.FriendNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='bnet.protocol.friends.FriendNotification.target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.friends.FriendNotification.game_account_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=487,
  serialized_end=604,
)


_GENERICFRIENDREQUEST = _descriptor.Descriptor(
  name='GenericFriendRequest',
  full_name='bnet.protocol.friends.GenericFriendRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.friends.GenericFriendRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='bnet.protocol.friends.GenericFriendRequest.target_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=606,
  serialized_end=715,
)


_GENERICFRIENDRESPONSE = _descriptor.Descriptor(
  name='GenericFriendResponse',
  full_name='bnet.protocol.friends.GenericFriendResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_friend', full_name='bnet.protocol.friends.GenericFriendResponse.target_friend', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=717,
  serialized_end=794,
)


_SUBSCRIBETOFRIENDSREQUEST = _descriptor.Descriptor(
  name='SubscribeToFriendsRequest',
  full_name='bnet.protocol.friends.SubscribeToFriendsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.friends.SubscribeToFriendsRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.friends.SubscribeToFriendsRequest.object_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=796,
  serialized_end=885,
)


_UNSUBSCRIBETOFRIENDSREQUEST = _descriptor.Descriptor(
  name='UnsubscribeToFriendsRequest',
  full_name='bnet.protocol.friends.UnsubscribeToFriendsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.friends.UnsubscribeToFriendsRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.friends.UnsubscribeToFriendsRequest.object_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=887,
  serialized_end=978,
)


_UPDATEFRIENDSTATENOTIFICATION = _descriptor.Descriptor(
  name='UpdateFriendStateNotification',
  full_name='bnet.protocol.friends.UpdateFriendStateNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='changed_friend', full_name='bnet.protocol.friends.UpdateFriendStateNotification.changed_friend', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.friends.UpdateFriendStateNotification.game_account_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=981,
  serialized_end=1117,
)


_UPDATEFRIENDSTATEREQUEST = _descriptor.Descriptor(
  name='UpdateFriendStateRequest',
  full_name='bnet.protocol.friends.UpdateFriendStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.friends.UpdateFriendStateRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='bnet.protocol.friends.UpdateFriendStateRequest.target_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.friends.UpdateFriendStateRequest.attribute', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes_epoch', full_name='bnet.protocol.friends.UpdateFriendStateRequest.attributes_epoch', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1120,
  serialized_end=1314,
)


_VIEWFRIENDSREQUEST = _descriptor.Descriptor(
  name='ViewFriendsRequest',
  full_name='bnet.protocol.friends.ViewFriendsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.friends.ViewFriendsRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='bnet.protocol.friends.ViewFriendsRequest.target_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.ViewFriendsRequest.role', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1316,
  serialized_end=1437,
)


_VIEWFRIENDSRESPONSE = _descriptor.Descriptor(
  name='ViewFriendsResponse',
  full_name='bnet.protocol.friends.ViewFriendsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='friends', full_name='bnet.protocol.friends.ViewFriendsResponse.friends', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1439,
  serialized_end=1508,
)


_FRIENDINVITATION = _descriptor.Descriptor(
  name='FriendInvitation',
  full_name='bnet.protocol.friends.FriendInvitation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_received', full_name='bnet.protocol.friends.FriendInvitation.first_received', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.FriendInvitation.role', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='friend_invite', full_name='bnet.protocol.friends.FriendInvitation.friend_invite', index=0,
      number=103, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1511,
  serialized_end=1669,
)


_INVITATIONNOTIFICATION = _descriptor.Descriptor(
  name='InvitationNotification',
  full_name='bnet.protocol.friends.InvitationNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='invitation', full_name='bnet.protocol.friends.InvitationNotification.invitation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.friends.InvitationNotification.game_account_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='bnet.protocol.friends.InvitationNotification.reason', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1672,
  serialized_end=1820,
)


_FRIENDINVITATIONPARAMS = _descriptor.Descriptor(
  name='FriendInvitationParams',
  full_name='bnet.protocol.friends.FriendInvitationParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_email', full_name='bnet.protocol.friends.FriendInvitationParams.target_email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_battle_tag', full_name='bnet.protocol.friends.FriendInvitationParams.target_battle_tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inviter_battle_tag', full_name='bnet.protocol.friends.FriendInvitationParams.inviter_battle_tag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inviter_full_name', full_name='bnet.protocol.friends.FriendInvitationParams.inviter_full_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invitee_display_name', full_name='bnet.protocol.friends.FriendInvitationParams.invitee_display_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.FriendInvitationParams.role', index=5,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='friend_params', full_name='bnet.protocol.friends.FriendInvitationParams.friend_params', index=0,
      number=103, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1823,
  serialized_end=2109,
)


_SUBSCRIBETOFRIENDSRESPONSE = _descriptor.Descriptor(
  name='SubscribeToFriendsResponse',
  full_name='bnet.protocol.friends.SubscribeToFriendsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_friends', full_name='bnet.protocol.friends.SubscribeToFriendsResponse.max_friends', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_received_invitations', full_name='bnet.protocol.friends.SubscribeToFriendsResponse.max_received_invitations', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_sent_invitations', full_name='bnet.protocol.friends.SubscribeToFriendsResponse.max_sent_invitations', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.SubscribeToFriendsResponse.role', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friends', full_name='bnet.protocol.friends.SubscribeToFriendsResponse.friends', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sent_invitations', full_name='bnet.protocol.friends.SubscribeToFriendsResponse.sent_invitations', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='received_invitations', full_name='bnet.protocol.friends.SubscribeToFriendsResponse.received_invitations', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2112,
  serialized_end=2440,
)

_ASSIGNROLEREQUEST.fields_by_name['agent_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_ASSIGNROLEREQUEST.fields_by_name['target_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_FRIEND.fields_by_name['id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_FRIEND.fields_by_name['attribute'].message_type = bnet_dot_protocol_dot_attribute__pb2._ATTRIBUTE
_FRIENDNOTIFICATION.fields_by_name['target'].message_type = _FRIEND
_FRIENDNOTIFICATION.fields_by_name['game_account_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_GENERICFRIENDREQUEST.fields_by_name['agent_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_GENERICFRIENDREQUEST.fields_by_name['target_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_GENERICFRIENDRESPONSE.fields_by_name['target_friend'].message_type = _FRIEND
_SUBSCRIBETOFRIENDSREQUEST.fields_by_name['agent_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_UNSUBSCRIBETOFRIENDSREQUEST.fields_by_name['agent_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_UPDATEFRIENDSTATENOTIFICATION.fields_by_name['changed_friend'].message_type = _FRIEND
_UPDATEFRIENDSTATENOTIFICATION.fields_by_name['game_account_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_UPDATEFRIENDSTATEREQUEST.fields_by_name['agent_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_UPDATEFRIENDSTATEREQUEST.fields_by_name['target_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_UPDATEFRIENDSTATEREQUEST.fields_by_name['attribute'].message_type = bnet_dot_protocol_dot_attribute__pb2._ATTRIBUTE
_VIEWFRIENDSREQUEST.fields_by_name['agent_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_VIEWFRIENDSREQUEST.fields_by_name['target_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_VIEWFRIENDSRESPONSE.fields_by_name['friends'].message_type = _FRIEND
_INVITATIONNOTIFICATION.fields_by_name['invitation'].message_type = bnet_dot_protocol_dot_invitation__pb2._INVITATION
_INVITATIONNOTIFICATION.fields_by_name['game_account_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_SUBSCRIBETOFRIENDSRESPONSE.fields_by_name['role'].message_type = bnet_dot_protocol__1__pb2._ROLE
_SUBSCRIBETOFRIENDSRESPONSE.fields_by_name['friends'].message_type = _FRIEND
_SUBSCRIBETOFRIENDSRESPONSE.fields_by_name['sent_invitations'].message_type = bnet_dot_protocol_dot_invitation__pb2._INVITATION
_SUBSCRIBETOFRIENDSRESPONSE.fields_by_name['received_invitations'].message_type = bnet_dot_protocol_dot_invitation__pb2._INVITATION
DESCRIPTOR.message_types_by_name['AssignRoleRequest'] = _ASSIGNROLEREQUEST
DESCRIPTOR.message_types_by_name['Friend'] = _FRIEND
DESCRIPTOR.message_types_by_name['FriendNotification'] = _FRIENDNOTIFICATION
DESCRIPTOR.message_types_by_name['GenericFriendRequest'] = _GENERICFRIENDREQUEST
DESCRIPTOR.message_types_by_name['GenericFriendResponse'] = _GENERICFRIENDRESPONSE
DESCRIPTOR.message_types_by_name['SubscribeToFriendsRequest'] = _SUBSCRIBETOFRIENDSREQUEST
DESCRIPTOR.message_types_by_name['UnsubscribeToFriendsRequest'] = _UNSUBSCRIBETOFRIENDSREQUEST
DESCRIPTOR.message_types_by_name['UpdateFriendStateNotification'] = _UPDATEFRIENDSTATENOTIFICATION
DESCRIPTOR.message_types_by_name['UpdateFriendStateRequest'] = _UPDATEFRIENDSTATEREQUEST
DESCRIPTOR.message_types_by_name['ViewFriendsRequest'] = _VIEWFRIENDSREQUEST
DESCRIPTOR.message_types_by_name['ViewFriendsResponse'] = _VIEWFRIENDSRESPONSE
DESCRIPTOR.message_types_by_name['FriendInvitation'] = _FRIENDINVITATION
DESCRIPTOR.message_types_by_name['InvitationNotification'] = _INVITATIONNOTIFICATION
DESCRIPTOR.message_types_by_name['FriendInvitationParams'] = _FRIENDINVITATIONPARAMS
DESCRIPTOR.message_types_by_name['SubscribeToFriendsResponse'] = _SUBSCRIBETOFRIENDSRESPONSE

AssignRoleRequest = _reflection.GeneratedProtocolMessageType('AssignRoleRequest', (_message.Message,), dict(
  DESCRIPTOR = _ASSIGNROLEREQUEST,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.AssignRoleRequest)
  ))
_sym_db.RegisterMessage(AssignRoleRequest)

Friend = _reflection.GeneratedProtocolMessageType('Friend', (_message.Message,), dict(
  DESCRIPTOR = _FRIEND,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.Friend)
  ))
_sym_db.RegisterMessage(Friend)

FriendNotification = _reflection.GeneratedProtocolMessageType('FriendNotification', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDNOTIFICATION,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.FriendNotification)
  ))
_sym_db.RegisterMessage(FriendNotification)

GenericFriendRequest = _reflection.GeneratedProtocolMessageType('GenericFriendRequest', (_message.Message,), dict(
  DESCRIPTOR = _GENERICFRIENDREQUEST,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.GenericFriendRequest)
  ))
_sym_db.RegisterMessage(GenericFriendRequest)

GenericFriendResponse = _reflection.GeneratedProtocolMessageType('GenericFriendResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENERICFRIENDRESPONSE,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.GenericFriendResponse)
  ))
_sym_db.RegisterMessage(GenericFriendResponse)

SubscribeToFriendsRequest = _reflection.GeneratedProtocolMessageType('SubscribeToFriendsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBETOFRIENDSREQUEST,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.SubscribeToFriendsRequest)
  ))
_sym_db.RegisterMessage(SubscribeToFriendsRequest)

UnsubscribeToFriendsRequest = _reflection.GeneratedProtocolMessageType('UnsubscribeToFriendsRequest', (_message.Message,), dict(
  DESCRIPTOR = _UNSUBSCRIBETOFRIENDSREQUEST,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.UnsubscribeToFriendsRequest)
  ))
_sym_db.RegisterMessage(UnsubscribeToFriendsRequest)

UpdateFriendStateNotification = _reflection.GeneratedProtocolMessageType('UpdateFriendStateNotification', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEFRIENDSTATENOTIFICATION,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.UpdateFriendStateNotification)
  ))
_sym_db.RegisterMessage(UpdateFriendStateNotification)

UpdateFriendStateRequest = _reflection.GeneratedProtocolMessageType('UpdateFriendStateRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEFRIENDSTATEREQUEST,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.UpdateFriendStateRequest)
  ))
_sym_db.RegisterMessage(UpdateFriendStateRequest)

ViewFriendsRequest = _reflection.GeneratedProtocolMessageType('ViewFriendsRequest', (_message.Message,), dict(
  DESCRIPTOR = _VIEWFRIENDSREQUEST,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.ViewFriendsRequest)
  ))
_sym_db.RegisterMessage(ViewFriendsRequest)

ViewFriendsResponse = _reflection.GeneratedProtocolMessageType('ViewFriendsResponse', (_message.Message,), dict(
  DESCRIPTOR = _VIEWFRIENDSRESPONSE,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.ViewFriendsResponse)
  ))
_sym_db.RegisterMessage(ViewFriendsResponse)

FriendInvitation = _reflection.GeneratedProtocolMessageType('FriendInvitation', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDINVITATION,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.FriendInvitation)
  ))
_sym_db.RegisterMessage(FriendInvitation)

InvitationNotification = _reflection.GeneratedProtocolMessageType('InvitationNotification', (_message.Message,), dict(
  DESCRIPTOR = _INVITATIONNOTIFICATION,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.InvitationNotification)
  ))
_sym_db.RegisterMessage(InvitationNotification)

FriendInvitationParams = _reflection.GeneratedProtocolMessageType('FriendInvitationParams', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDINVITATIONPARAMS,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.FriendInvitationParams)
  ))
_sym_db.RegisterMessage(FriendInvitationParams)

SubscribeToFriendsResponse = _reflection.GeneratedProtocolMessageType('SubscribeToFriendsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBETOFRIENDSRESPONSE,
  __module__ = 'bnet.protocol.friends_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.SubscribeToFriendsResponse)
  ))
_sym_db.RegisterMessage(SubscribeToFriendsResponse)

_FRIENDINVITATION.extensions_by_name['friend_invite'].message_type = _FRIENDINVITATION
bnet_dot_protocol_dot_invitation__pb2.Invitation.RegisterExtension(_FRIENDINVITATION.extensions_by_name['friend_invite'])
_FRIENDINVITATIONPARAMS.extensions_by_name['friend_params'].message_type = _FRIENDINVITATIONPARAMS
bnet_dot_protocol_dot_invitation__pb2.InvitationParams.RegisterExtension(_FRIENDINVITATIONPARAMS.extensions_by_name['friend_params'])

# @@protoc_insertion_point(module_scope)
