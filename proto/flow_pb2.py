# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/flow.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10proto/flow.proto\x12\x04\x66low\"%\n\x10\x46lowMessageClass\x12\x11\n\tmalicious\x18\x01 \x01(\x08\"\xf8\x01\n\x0b\x46lowMessage\x12\x10\n\x08OutBytes\x18\x01 \x01(\x04\x12\x0f\n\x07OutPkts\x18\x02 \x01(\x04\x12\x0f\n\x07InBytes\x18\x03 \x01(\x04\x12\x0e\n\x06InPkts\x18\x04 \x01(\x04\x12\x13\n\x0bIPV4SrcAddr\x18\x05 \x01(\t\x12\x13\n\x0bIPV4DstAddr\x18\x06 \x01(\t\x12\x0f\n\x07L7Proto\x18\x07 \x01(\x02\x12\x11\n\tL4DstPort\x18\x08 \x01(\r\x12\x11\n\tL4SrcPort\x18\t \x01(\r\x12 \n\x18\x46lowDurationMilliseconds\x18\n \x01(\x04\x12\x10\n\x08Protocol\x18\x0b \x01(\r\x12\x10\n\x08TCPFlags\x18\x0c \x01(\r2]\n\x15\x46lowMessageClassifier\x12\x44\n\x11\x43lassifyStreaming\x12\x11.flow.FlowMessage\x1a\x16.flow.FlowMessageClass\"\x00(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.flow_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FLOWMESSAGECLASS._serialized_start=26
  _FLOWMESSAGECLASS._serialized_end=63
  _FLOWMESSAGE._serialized_start=66
  _FLOWMESSAGE._serialized_end=314
  _FLOWMESSAGECLASSIFIER._serialized_start=316
  _FLOWMESSAGECLASSIFIER._serialized_end=409
# @@protoc_insertion_point(module_scope)
