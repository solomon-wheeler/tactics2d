# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataset.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import tactics2d.dataset_parser.womd_proto.pb3.label_pb2 as label__pb2
import tactics2d.dataset_parser.womd_proto.pb3.map_pb2 as map__pb2
import tactics2d.dataset_parser.womd_proto.pb3.vector_pb2 as vector__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\rdataset.proto\x12\x12waymo.open_dataset\x1a\x0blabel.proto\x1a\tmap.proto\x1a\x0cvector.proto"\x1b\n\x0bMatrixShape\x12\x0c\n\x04\x64ims\x18\x01 \x03(\x05"O\n\x0bMatrixFloat\x12\x10\n\x04\x64\x61ta\x18\x01 \x03(\x02\x42\x02\x10\x01\x12.\n\x05shape\x18\x02 \x01(\x0b\x32\x1f.waymo.open_dataset.MatrixShape"O\n\x0bMatrixInt32\x12\x10\n\x04\x64\x61ta\x18\x01 \x03(\x05\x42\x02\x10\x01\x12.\n\x05shape\x18\x02 \x01(\x0b\x32\x1f.waymo.open_dataset.MatrixShape"l\n\nCameraName"^\n\x04Name\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x46RONT\x10\x01\x12\x0e\n\nFRONT_LEFT\x10\x02\x12\x0f\n\x0b\x46RONT_RIGHT\x10\x03\x12\r\n\tSIDE_LEFT\x10\x04\x12\x0e\n\nSIDE_RIGHT\x10\x05"]\n\tLaserName"P\n\x04Name\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03TOP\x10\x01\x12\t\n\x05\x46RONT\x10\x02\x12\r\n\tSIDE_LEFT\x10\x03\x12\x0e\n\nSIDE_RIGHT\x10\x04\x12\x08\n\x04REAR\x10\x05"\x1e\n\tTransform\x12\x11\n\ttransform\x18\x01 \x03(\x01"X\n\x08Velocity\x12\x0b\n\x03v_x\x18\x01 \x01(\x02\x12\x0b\n\x03v_y\x18\x02 \x01(\x02\x12\x0b\n\x03v_z\x18\x03 \x01(\x02\x12\x0b\n\x03w_x\x18\x04 \x01(\x01\x12\x0b\n\x03w_y\x18\x05 \x01(\x01\x12\x0b\n\x03w_z\x18\x06 \x01(\x01"\xa3\x03\n\x11\x43\x61meraCalibration\x12\x31\n\x04name\x18\x01 \x01(\x0e\x32#.waymo.open_dataset.CameraName.Name\x12\x11\n\tintrinsic\x18\x02 \x03(\x01\x12\x30\n\textrinsic\x18\x03 \x01(\x0b\x32\x1d.waymo.open_dataset.Transform\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0e\n\x06height\x18\x05 \x01(\x05\x12g\n\x19rolling_shutter_direction\x18\x06 \x01(\x0e\x32\x44.waymo.open_dataset.CameraCalibration.RollingShutterReadOutDirection"\x8d\x01\n\x1eRollingShutterReadOutDirection\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rTOP_TO_BOTTOM\x10\x01\x12\x11\n\rLEFT_TO_RIGHT\x10\x02\x12\x11\n\rBOTTOM_TO_TOP\x10\x03\x12\x11\n\rRIGHT_TO_LEFT\x10\x04\x12\x12\n\x0eGLOBAL_SHUTTER\x10\x05"\xcd\x01\n\x10LaserCalibration\x12\x30\n\x04name\x18\x01 \x01(\x0e\x32".waymo.open_dataset.LaserName.Name\x12\x19\n\x11\x62\x65\x61m_inclinations\x18\x02 \x03(\x01\x12\x1c\n\x14\x62\x65\x61m_inclination_min\x18\x03 \x01(\x01\x12\x1c\n\x14\x62\x65\x61m_inclination_max\x18\x04 \x01(\x01\x12\x30\n\textrinsic\x18\x05 \x01(\x0b\x32\x1d.waymo.open_dataset.Transform"\xf6\x03\n\x07\x43ontext\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x42\n\x13\x63\x61mera_calibrations\x18\x02 \x03(\x0b\x32%.waymo.open_dataset.CameraCalibration\x12@\n\x12laser_calibrations\x18\x03 \x03(\x0b\x32$.waymo.open_dataset.LaserCalibration\x12\x30\n\x05stats\x18\x04 \x01(\x0b\x32!.waymo.open_dataset.Context.Stats\x1a\xa4\x02\n\x05Stats\x12J\n\x13laser_object_counts\x18\x01 \x03(\x0b\x32-.waymo.open_dataset.Context.Stats.ObjectCount\x12K\n\x14\x63\x61mera_object_counts\x18\x05 \x03(\x0b\x32-.waymo.open_dataset.Context.Stats.ObjectCount\x12\x13\n\x0btime_of_day\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0f\n\x07weather\x18\x04 \x01(\t\x1aJ\n\x0bObjectCount\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.waymo.open_dataset.Label.Type\x12\r\n\x05\x63ount\x18\x02 \x01(\x05"\xfd\x01\n\nRangeImage\x12\x1e\n\x16range_image_compressed\x18\x02 \x01(\x0c\x12$\n\x1c\x63\x61mera_projection_compressed\x18\x03 \x01(\x0c\x12#\n\x1brange_image_pose_compressed\x18\x04 \x01(\x0c\x12#\n\x1brange_image_flow_compressed\x18\x05 \x01(\x0c\x12%\n\x1dsegmentation_label_compressed\x18\x06 \x01(\x0c\x12\x38\n\x0brange_image\x18\x01 \x01(\x0b\x32\x1f.waymo.open_dataset.MatrixFloatB\x02\x18\x01"\xe0\x02\n\x17\x43\x61meraSegmentationLabel\x12\x1e\n\x16panoptic_label_divisor\x18\x01 \x01(\x05\x12\x16\n\x0epanoptic_label\x18\x02 \x01(\x0c\x12q\n instance_id_to_global_id_mapping\x18\x03 \x03(\x0b\x32G.waymo.open_dataset.CameraSegmentationLabel.InstanceIDToGlobalIDMapping\x12\x13\n\x0bsequence_id\x18\x04 \x01(\t\x12\x1b\n\x13num_cameras_covered\x18\x05 \x01(\x0c\x1ah\n\x1bInstanceIDToGlobalIDMapping\x12\x19\n\x11local_instance_id\x18\x01 \x01(\x05\x12\x1a\n\x12global_instance_id\x18\x02 \x01(\x05\x12\x12\n\nis_tracked\x18\x03 \x01(\x08"\xe4\x02\n\x0b\x43\x61meraImage\x12\x31\n\x04name\x18\x01 \x01(\x0e\x32#.waymo.open_dataset.CameraName.Name\x12\r\n\x05image\x18\x02 \x01(\x0c\x12+\n\x04pose\x18\x03 \x01(\x0b\x32\x1d.waymo.open_dataset.Transform\x12.\n\x08velocity\x18\x04 \x01(\x0b\x32\x1c.waymo.open_dataset.Velocity\x12\x16\n\x0epose_timestamp\x18\x05 \x01(\x01\x12\x0f\n\x07shutter\x18\x06 \x01(\x01\x12\x1b\n\x13\x63\x61mera_trigger_time\x18\x07 \x01(\x01\x12 \n\x18\x63\x61mera_readout_done_time\x18\x08 \x01(\x01\x12N\n\x19\x63\x61mera_segmentation_label\x18\n \x01(\x0b\x32+.waymo.open_dataset.CameraSegmentationLabel"l\n\x0c\x43\x61meraLabels\x12\x31\n\x04name\x18\x01 \x01(\x0e\x32#.waymo.open_dataset.CameraName.Name\x12)\n\x06labels\x18\x02 \x03(\x0b\x32\x19.waymo.open_dataset.Label"\xa1\x01\n\x05Laser\x12\x30\n\x04name\x18\x01 \x01(\x0e\x32".waymo.open_dataset.LaserName.Name\x12\x32\n\nri_return1\x18\x02 \x01(\x0b\x32\x1e.waymo.open_dataset.RangeImage\x12\x32\n\nri_return2\x18\x03 \x01(\x0b\x32\x1e.waymo.open_dataset.RangeImage"\xad\x04\n\x05\x46rame\x12,\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x1b.waymo.open_dataset.Context\x12\x18\n\x10timestamp_micros\x18\x02 \x01(\x03\x12+\n\x04pose\x18\x03 \x01(\x0b\x32\x1d.waymo.open_dataset.Transform\x12/\n\x06images\x18\x04 \x03(\x0b\x32\x1f.waymo.open_dataset.CameraImage\x12)\n\x06lasers\x18\x05 \x03(\x0b\x32\x19.waymo.open_dataset.Laser\x12/\n\x0claser_labels\x18\x06 \x03(\x0b\x32\x19.waymo.open_dataset.Label\x12@\n\x16projected_lidar_labels\x18\t \x03(\x0b\x32 .waymo.open_dataset.CameraLabels\x12\x37\n\rcamera_labels\x18\x08 \x03(\x0b\x32 .waymo.open_dataset.CameraLabels\x12:\n\x0eno_label_zones\x18\x07 \x03(\x0b\x32".waymo.open_dataset.Polygon2dProto\x12\x34\n\x0cmap_features\x18\n \x03(\x0b\x32\x1e.waymo.open_dataset.MapFeature\x12\x35\n\x0fmap_pose_offset\x18\x0b \x01(\x0b\x32\x1c.waymo.open_dataset.Vector3db\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dataset_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_MATRIXFLOAT"].fields_by_name["data"]._loaded_options = None
    _globals["_MATRIXFLOAT"].fields_by_name["data"]._serialized_options = b"\020\001"
    _globals["_MATRIXINT32"].fields_by_name["data"]._loaded_options = None
    _globals["_MATRIXINT32"].fields_by_name["data"]._serialized_options = b"\020\001"
    _globals["_RANGEIMAGE"].fields_by_name["range_image"]._loaded_options = None
    _globals["_RANGEIMAGE"].fields_by_name["range_image"]._serialized_options = b"\030\001"
    _globals["_MATRIXSHAPE"]._serialized_start = 75
    _globals["_MATRIXSHAPE"]._serialized_end = 102
    _globals["_MATRIXFLOAT"]._serialized_start = 104
    _globals["_MATRIXFLOAT"]._serialized_end = 183
    _globals["_MATRIXINT32"]._serialized_start = 185
    _globals["_MATRIXINT32"]._serialized_end = 264
    _globals["_CAMERANAME"]._serialized_start = 266
    _globals["_CAMERANAME"]._serialized_end = 374
    _globals["_CAMERANAME_NAME"]._serialized_start = 280
    _globals["_CAMERANAME_NAME"]._serialized_end = 374
    _globals["_LASERNAME"]._serialized_start = 376
    _globals["_LASERNAME"]._serialized_end = 469
    _globals["_LASERNAME_NAME"]._serialized_start = 389
    _globals["_LASERNAME_NAME"]._serialized_end = 469
    _globals["_TRANSFORM"]._serialized_start = 471
    _globals["_TRANSFORM"]._serialized_end = 501
    _globals["_VELOCITY"]._serialized_start = 503
    _globals["_VELOCITY"]._serialized_end = 591
    _globals["_CAMERACALIBRATION"]._serialized_start = 594
    _globals["_CAMERACALIBRATION"]._serialized_end = 1013
    _globals["_CAMERACALIBRATION_ROLLINGSHUTTERREADOUTDIRECTION"]._serialized_start = 872
    _globals["_CAMERACALIBRATION_ROLLINGSHUTTERREADOUTDIRECTION"]._serialized_end = 1013
    _globals["_LASERCALIBRATION"]._serialized_start = 1016
    _globals["_LASERCALIBRATION"]._serialized_end = 1221
    _globals["_CONTEXT"]._serialized_start = 1224
    _globals["_CONTEXT"]._serialized_end = 1726
    _globals["_CONTEXT_STATS"]._serialized_start = 1434
    _globals["_CONTEXT_STATS"]._serialized_end = 1726
    _globals["_CONTEXT_STATS_OBJECTCOUNT"]._serialized_start = 1652
    _globals["_CONTEXT_STATS_OBJECTCOUNT"]._serialized_end = 1726
    _globals["_RANGEIMAGE"]._serialized_start = 1729
    _globals["_RANGEIMAGE"]._serialized_end = 1982
    _globals["_CAMERASEGMENTATIONLABEL"]._serialized_start = 1985
    _globals["_CAMERASEGMENTATIONLABEL"]._serialized_end = 2337
    _globals["_CAMERASEGMENTATIONLABEL_INSTANCEIDTOGLOBALIDMAPPING"]._serialized_start = 2233
    _globals["_CAMERASEGMENTATIONLABEL_INSTANCEIDTOGLOBALIDMAPPING"]._serialized_end = 2337
    _globals["_CAMERAIMAGE"]._serialized_start = 2340
    _globals["_CAMERAIMAGE"]._serialized_end = 2696
    _globals["_CAMERALABELS"]._serialized_start = 2698
    _globals["_CAMERALABELS"]._serialized_end = 2806
    _globals["_LASER"]._serialized_start = 2809
    _globals["_LASER"]._serialized_end = 2970
    _globals["_FRAME"]._serialized_start = 2973
    _globals["_FRAME"]._serialized_end = 3530
# @@protoc_insertion_point(module_scope)
