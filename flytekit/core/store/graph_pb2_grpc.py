# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from flytekit.core.store import graph_pb2 as proto_dot_graph__pb2


class GraphServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WatchAllExecutions = channel.unary_stream(
                '/graph.v1.GraphService/WatchAllExecutions',
                request_serializer=proto_dot_graph__pb2.WatchAllExecutionsRequest.SerializeToString,
                response_deserializer=proto_dot_graph__pb2.ExecutionInfo.FromString,
                )
        self.WatchNodesForExecution = channel.unary_stream(
                '/graph.v1.GraphService/WatchNodesForExecution',
                request_serializer=proto_dot_graph__pb2.WatchNodesForExecutionRequest.SerializeToString,
                response_deserializer=proto_dot_graph__pb2.NodeInfo.FromString,
                )
        self.CreateTask = channel.unary_unary(
                '/graph.v1.GraphService/CreateTask',
                request_serializer=proto_dot_graph__pb2.Task.SerializeToString,
                response_deserializer=proto_dot_graph__pb2.TaskID.FromString,
                )
        self.GetTask = channel.unary_unary(
                '/graph.v1.GraphService/GetTask',
                request_serializer=proto_dot_graph__pb2.TaskID.SerializeToString,
                response_deserializer=proto_dot_graph__pb2.Task.FromString,
                )
        self.CreateExecution = channel.unary_unary(
                '/graph.v1.GraphService/CreateExecution',
                request_serializer=proto_dot_graph__pb2.CreateExecutionRequest.SerializeToString,
                response_deserializer=proto_dot_graph__pb2.ExecutionID.FromString,
                )
        self.CreateNode = channel.unary_unary(
                '/graph.v1.GraphService/CreateNode',
                request_serializer=proto_dot_graph__pb2.CreateNodeRequest.SerializeToString,
                response_deserializer=proto_dot_graph__pb2.NodeID.FromString,
                )
        self.UpdateNodeStatus = channel.unary_unary(
                '/graph.v1.GraphService/UpdateNodeStatus',
                request_serializer=proto_dot_graph__pb2.UpdateNodeStatusRequest.SerializeToString,
                response_deserializer=proto_dot_graph__pb2.Node.FromString,
                )
        self.UpdateExecutionStatus = channel.unary_unary(
                '/graph.v1.GraphService/UpdateExecutionStatus',
                request_serializer=proto_dot_graph__pb2.UpdateExecutionStatusRequest.SerializeToString,
                response_deserializer=proto_dot_graph__pb2.ExecutionInfo.FromString,
                )
        self.GetNodeDetails = channel.unary_unary(
                '/graph.v1.GraphService/GetNodeDetails',
                request_serializer=proto_dot_graph__pb2.GetNodeDetailsRequest.SerializeToString,
                response_deserializer=proto_dot_graph__pb2.NodeDetails.FromString,
                )


class GraphServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def WatchAllExecutions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchNodesForExecution(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateExecution(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateNodeStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateExecutionStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNodeDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GraphServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'WatchAllExecutions': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchAllExecutions,
                    request_deserializer=proto_dot_graph__pb2.WatchAllExecutionsRequest.FromString,
                    response_serializer=proto_dot_graph__pb2.ExecutionInfo.SerializeToString,
            ),
            'WatchNodesForExecution': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchNodesForExecution,
                    request_deserializer=proto_dot_graph__pb2.WatchNodesForExecutionRequest.FromString,
                    response_serializer=proto_dot_graph__pb2.NodeInfo.SerializeToString,
            ),
            'CreateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTask,
                    request_deserializer=proto_dot_graph__pb2.Task.FromString,
                    response_serializer=proto_dot_graph__pb2.TaskID.SerializeToString,
            ),
            'GetTask': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTask,
                    request_deserializer=proto_dot_graph__pb2.TaskID.FromString,
                    response_serializer=proto_dot_graph__pb2.Task.SerializeToString,
            ),
            'CreateExecution': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateExecution,
                    request_deserializer=proto_dot_graph__pb2.CreateExecutionRequest.FromString,
                    response_serializer=proto_dot_graph__pb2.ExecutionID.SerializeToString,
            ),
            'CreateNode': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNode,
                    request_deserializer=proto_dot_graph__pb2.CreateNodeRequest.FromString,
                    response_serializer=proto_dot_graph__pb2.NodeID.SerializeToString,
            ),
            'UpdateNodeStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateNodeStatus,
                    request_deserializer=proto_dot_graph__pb2.UpdateNodeStatusRequest.FromString,
                    response_serializer=proto_dot_graph__pb2.Node.SerializeToString,
            ),
            'UpdateExecutionStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateExecutionStatus,
                    request_deserializer=proto_dot_graph__pb2.UpdateExecutionStatusRequest.FromString,
                    response_serializer=proto_dot_graph__pb2.ExecutionInfo.SerializeToString,
            ),
            'GetNodeDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNodeDetails,
                    request_deserializer=proto_dot_graph__pb2.GetNodeDetailsRequest.FromString,
                    response_serializer=proto_dot_graph__pb2.NodeDetails.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'graph.v1.GraphService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GraphService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def WatchAllExecutions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/graph.v1.GraphService/WatchAllExecutions',
            proto_dot_graph__pb2.WatchAllExecutionsRequest.SerializeToString,
            proto_dot_graph__pb2.ExecutionInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WatchNodesForExecution(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/graph.v1.GraphService/WatchNodesForExecution',
            proto_dot_graph__pb2.WatchNodesForExecutionRequest.SerializeToString,
            proto_dot_graph__pb2.NodeInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graph.v1.GraphService/CreateTask',
            proto_dot_graph__pb2.Task.SerializeToString,
            proto_dot_graph__pb2.TaskID.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graph.v1.GraphService/GetTask',
            proto_dot_graph__pb2.TaskID.SerializeToString,
            proto_dot_graph__pb2.Task.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateExecution(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graph.v1.GraphService/CreateExecution',
            proto_dot_graph__pb2.CreateExecutionRequest.SerializeToString,
            proto_dot_graph__pb2.ExecutionID.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graph.v1.GraphService/CreateNode',
            proto_dot_graph__pb2.CreateNodeRequest.SerializeToString,
            proto_dot_graph__pb2.NodeID.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateNodeStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graph.v1.GraphService/UpdateNodeStatus',
            proto_dot_graph__pb2.UpdateNodeStatusRequest.SerializeToString,
            proto_dot_graph__pb2.Node.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateExecutionStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graph.v1.GraphService/UpdateExecutionStatus',
            proto_dot_graph__pb2.UpdateExecutionStatusRequest.SerializeToString,
            proto_dot_graph__pb2.ExecutionInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNodeDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graph.v1.GraphService/GetNodeDetails',
            proto_dot_graph__pb2.GetNodeDetailsRequest.SerializeToString,
            proto_dot_graph__pb2.NodeDetails.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
