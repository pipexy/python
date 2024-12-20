# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pipeline_pb2 as pipeline__pb2


class VideoProcessorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateShortVideo = channel.unary_unary(
                '/pipeline.VideoProcessor/CreateShortVideo',
                request_serializer=pipeline__pb2.VideoRequest.SerializeToString,
                response_deserializer=pipeline__pb2.VideoResponse.FromString,
                )


class VideoProcessorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateShortVideo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VideoProcessorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateShortVideo': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateShortVideo,
                    request_deserializer=pipeline__pb2.VideoRequest.FromString,
                    response_serializer=pipeline__pb2.VideoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pipeline.VideoProcessor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VideoProcessor(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateShortVideo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pipeline.VideoProcessor/CreateShortVideo',
            pipeline__pb2.VideoRequest.SerializeToString,
            pipeline__pb2.VideoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class MovementDetectorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DetectMovement = channel.unary_unary(
                '/pipeline.MovementDetector/DetectMovement',
                request_serializer=pipeline__pb2.ImageRequest.SerializeToString,
                response_deserializer=pipeline__pb2.DetectionResponse.FromString,
                )


class MovementDetectorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DetectMovement(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MovementDetectorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DetectMovement': grpc.unary_unary_rpc_method_handler(
                    servicer.DetectMovement,
                    request_deserializer=pipeline__pb2.ImageRequest.FromString,
                    response_serializer=pipeline__pb2.DetectionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pipeline.MovementDetector', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MovementDetector(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DetectMovement(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pipeline.MovementDetector/DetectMovement',
            pipeline__pb2.ImageRequest.SerializeToString,
            pipeline__pb2.DetectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ObjectDetectorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DetectObjects = channel.unary_unary(
                '/pipeline.ObjectDetector/DetectObjects',
                request_serializer=pipeline__pb2.ImageRequest.SerializeToString,
                response_deserializer=pipeline__pb2.ObjectsResponse.FromString,
                )


class ObjectDetectorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DetectObjects(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ObjectDetectorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DetectObjects': grpc.unary_unary_rpc_method_handler(
                    servicer.DetectObjects,
                    request_deserializer=pipeline__pb2.ImageRequest.FromString,
                    response_serializer=pipeline__pb2.ObjectsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pipeline.ObjectDetector', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ObjectDetector(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DetectObjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pipeline.ObjectDetector/DetectObjects',
            pipeline__pb2.ImageRequest.SerializeToString,
            pipeline__pb2.ObjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class TranscriberStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Transcribe = channel.unary_unary(
                '/pipeline.Transcriber/Transcribe',
                request_serializer=pipeline__pb2.AudioRequest.SerializeToString,
                response_deserializer=pipeline__pb2.TextResponse.FromString,
                )


class TranscriberServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Transcribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TranscriberServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Transcribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Transcribe,
                    request_deserializer=pipeline__pb2.AudioRequest.FromString,
                    response_serializer=pipeline__pb2.TextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pipeline.Transcriber', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Transcriber(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Transcribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pipeline.Transcriber/Transcribe',
            pipeline__pb2.AudioRequest.SerializeToString,
            pipeline__pb2.TextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class CaptionerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateCaption = channel.unary_unary(
                '/pipeline.Captioner/GenerateCaption',
                request_serializer=pipeline__pb2.VideoRequest.SerializeToString,
                response_deserializer=pipeline__pb2.TextResponse.FromString,
                )


class CaptionerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GenerateCaption(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CaptionerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateCaption': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateCaption,
                    request_deserializer=pipeline__pb2.VideoRequest.FromString,
                    response_serializer=pipeline__pb2.TextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pipeline.Captioner', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Captioner(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GenerateCaption(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pipeline.Captioner/GenerateCaption',
            pipeline__pb2.VideoRequest.SerializeToString,
            pipeline__pb2.TextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DescriberStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateDescription = channel.unary_unary(
                '/pipeline.Describer/GenerateDescription',
                request_serializer=pipeline__pb2.ContentRequest.SerializeToString,
                response_deserializer=pipeline__pb2.TextResponse.FromString,
                )


class DescriberServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GenerateDescription(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DescriberServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateDescription': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateDescription,
                    request_deserializer=pipeline__pb2.ContentRequest.FromString,
                    response_serializer=pipeline__pb2.TextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pipeline.Describer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Describer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GenerateDescription(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pipeline.Describer/GenerateDescription',
            pipeline__pb2.ContentRequest.SerializeToString,
            pipeline__pb2.TextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class RssCreatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateRssEntry = channel.unary_unary(
                '/pipeline.RssCreator/CreateRssEntry',
                request_serializer=pipeline__pb2.RssRequest.SerializeToString,
                response_deserializer=pipeline__pb2.RssResponse.FromString,
                )


class RssCreatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateRssEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RssCreatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateRssEntry': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRssEntry,
                    request_deserializer=pipeline__pb2.RssRequest.FromString,
                    response_serializer=pipeline__pb2.RssResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pipeline.RssCreator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RssCreator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateRssEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pipeline.RssCreator/CreateRssEntry',
            pipeline__pb2.RssRequest.SerializeToString,
            pipeline__pb2.RssResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
