# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tracelet_status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tracelet_status.proto',
  package='easylocate',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15tracelet_status.proto\x12\neasylocate\"\x1b\n\rStatusRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x9a\x01\n\x0eStatusResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x16\n\x0epower_up_count\x18\x02 \x01(\x05\x12\x14\n\x0chas_position\x18\x03 \x01(\x08\x12\x1d\n\x15has_server_connection\x18\x04 \x01(\x08\x12\x10\n\x08has_time\x18\x05 \x01(\x08\x12\x1d\n\x15\x65loc_module_status_ok\x18\x06 \x01(\x08\x62\x06proto3')
)




_STATUSREQUEST = _descriptor.Descriptor(
  name='StatusRequest',
  full_name='easylocate.StatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='easylocate.StatusRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=64,
)


_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='easylocate.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='easylocate.StatusResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='power_up_count', full_name='easylocate.StatusResponse.power_up_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_position', full_name='easylocate.StatusResponse.has_position', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_server_connection', full_name='easylocate.StatusResponse.has_server_connection', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_time', full_name='easylocate.StatusResponse.has_time', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eloc_module_status_ok', full_name='easylocate.StatusResponse.eloc_module_status_ok', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=221,
)

DESCRIPTOR.message_types_by_name['StatusRequest'] = _STATUSREQUEST
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _STATUSREQUEST,
  __module__ = 'tracelet_status_pb2'
  # @@protoc_insertion_point(class_scope:easylocate.StatusRequest)
  ))
_sym_db.RegisterMessage(StatusRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _STATUSRESPONSE,
  __module__ = 'tracelet_status_pb2'
  # @@protoc_insertion_point(class_scope:easylocate.StatusResponse)
  ))
_sym_db.RegisterMessage(StatusResponse)


# @@protoc_insertion_point(module_scope)
