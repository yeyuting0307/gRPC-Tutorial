# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='my.server.streaming.grpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rexample.proto\x12\x18my.server.streaming.grpc\"-\n\x0e\x45xampleRequest\x12\x1b\n\x13server_render_times\x18\x01 \x01(\x05\"&\n\x0f\x45xampleResponse\x12\x13\n\x0bres_content\x18\x01 \x01(\t2|\n\x13ServerStreamExample\x12\x65\n\nExampleRpc\x12(.my.server.streaming.grpc.ExampleRequest\x1a).my.server.streaming.grpc.ExampleResponse\"\x00\x30\x01\x62\x06proto3'
)




_EXAMPLEREQUEST = _descriptor.Descriptor(
  name='ExampleRequest',
  full_name='my.server.streaming.grpc.ExampleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_render_times', full_name='my.server.streaming.grpc.ExampleRequest.server_render_times', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=43,
  serialized_end=88,
)


_EXAMPLERESPONSE = _descriptor.Descriptor(
  name='ExampleResponse',
  full_name='my.server.streaming.grpc.ExampleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='res_content', full_name='my.server.streaming.grpc.ExampleResponse.res_content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=90,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['ExampleRequest'] = _EXAMPLEREQUEST
DESCRIPTOR.message_types_by_name['ExampleResponse'] = _EXAMPLERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExampleRequest = _reflection.GeneratedProtocolMessageType('ExampleRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXAMPLEREQUEST,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:my.server.streaming.grpc.ExampleRequest)
  })
_sym_db.RegisterMessage(ExampleRequest)

ExampleResponse = _reflection.GeneratedProtocolMessageType('ExampleResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXAMPLERESPONSE,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:my.server.streaming.grpc.ExampleResponse)
  })
_sym_db.RegisterMessage(ExampleResponse)



_SERVERSTREAMEXAMPLE = _descriptor.ServiceDescriptor(
  name='ServerStreamExample',
  full_name='my.server.streaming.grpc.ServerStreamExample',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=130,
  serialized_end=254,
  methods=[
  _descriptor.MethodDescriptor(
    name='ExampleRpc',
    full_name='my.server.streaming.grpc.ServerStreamExample.ExampleRpc',
    index=0,
    containing_service=None,
    input_type=_EXAMPLEREQUEST,
    output_type=_EXAMPLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVERSTREAMEXAMPLE)

DESCRIPTOR.services_by_name['ServerStreamExample'] = _SERVERSTREAMEXAMPLE

# @@protoc_insertion_point(module_scope)
