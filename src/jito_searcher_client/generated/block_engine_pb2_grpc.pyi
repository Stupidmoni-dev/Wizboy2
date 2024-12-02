"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import block_engine_pb2
import collections.abc
import grpc

class BlockEngineValidatorStub:
    """/ Validators can connect to Block Engines to receive packets and bundles."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    SubscribePackets: grpc.UnaryStreamMultiCallable[
        block_engine_pb2.SubscribePacketsRequest,
        block_engine_pb2.SubscribePacketsResponse,
    ]
    """/ Validators can subscribe to the block engine to receive a stream of packets"""
    SubscribeBundles: grpc.UnaryStreamMultiCallable[
        block_engine_pb2.SubscribeBundlesRequest,
        block_engine_pb2.SubscribeBundlesResponse,
    ]
    """/ Validators can subscribe to the block engine to receive a stream of simulated and profitable bundles"""
    GetBlockBuilderFeeInfo: grpc.UnaryUnaryMultiCallable[
        block_engine_pb2.BlockBuilderFeeInfoRequest,
        block_engine_pb2.BlockBuilderFeeInfoResponse,
    ]
    """Block builders can optionally collect fees. This returns fee information if a block builder wants to
    collect one.
    """

class BlockEngineValidatorServicer(metaclass=abc.ABCMeta):
    """/ Validators can connect to Block Engines to receive packets and bundles."""

    @abc.abstractmethod
    def SubscribePackets(
        self,
        request: block_engine_pb2.SubscribePacketsRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[block_engine_pb2.SubscribePacketsResponse]:
        """/ Validators can subscribe to the block engine to receive a stream of packets"""
    @abc.abstractmethod
    def SubscribeBundles(
        self,
        request: block_engine_pb2.SubscribeBundlesRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[block_engine_pb2.SubscribeBundlesResponse]:
        """/ Validators can subscribe to the block engine to receive a stream of simulated and profitable bundles"""
    @abc.abstractmethod
    def GetBlockBuilderFeeInfo(
        self,
        request: block_engine_pb2.BlockBuilderFeeInfoRequest,
        context: grpc.ServicerContext,
    ) -> block_engine_pb2.BlockBuilderFeeInfoResponse:
        """Block builders can optionally collect fees. This returns fee information if a block builder wants to
        collect one.
        """

def add_BlockEngineValidatorServicer_to_server(servicer: BlockEngineValidatorServicer, server: grpc.Server) -> None: ...

class BlockEngineRelayerStub:
    """/ Relayers can forward packets to Block Engines.
    / Block Engines provide an AccountsOfInterest field to only send transactions that are of interest.
    """

    def __init__(self, channel: grpc.Channel) -> None: ...
    SubscribeAccountsOfInterest: grpc.UnaryStreamMultiCallable[
        block_engine_pb2.AccountsOfInterestRequest,
        block_engine_pb2.AccountsOfInterestUpdate,
    ]
    """/ The block engine feeds accounts of interest (AOI) updates to the relayer periodically.
    / For all transactions the relayer receives, it forwards transactions to the block engine which write-lock
    / any of the accounts in the AOI.
    """
    SubscribeProgramsOfInterest: grpc.UnaryStreamMultiCallable[
        block_engine_pb2.ProgramsOfInterestRequest,
        block_engine_pb2.ProgramsOfInterestUpdate,
    ]
    StartExpiringPacketStream: grpc.StreamStreamMultiCallable[
        block_engine_pb2.PacketBatchUpdate,
        block_engine_pb2.StartExpiringPacketStreamResponse,
    ]
    """Validators can subscribe to packets from the relayer and receive a multiplexed signal that contains a mixture
    of packets and heartbeats.
    NOTE: This is a bi-directional stream due to a bug with how Envoy handles half closed client-side streams.
    The issue is being tracked here: https://github.com/envoyproxy/envoy/issues/22748. In the meantime, the
    server will stream heartbeats to clients at some reasonable cadence.
    """

class BlockEngineRelayerServicer(metaclass=abc.ABCMeta):
    """/ Relayers can forward packets to Block Engines.
    / Block Engines provide an AccountsOfInterest field to only send transactions that are of interest.
    """

    @abc.abstractmethod
    def SubscribeAccountsOfInterest(
        self,
        request: block_engine_pb2.AccountsOfInterestRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[block_engine_pb2.AccountsOfInterestUpdate]:
        """/ The block engine feeds accounts of interest (AOI) updates to the relayer periodically.
        / For all transactions the relayer receives, it forwards transactions to the block engine which write-lock
        / any of the accounts in the AOI.
        """
    @abc.abstractmethod
    def SubscribeProgramsOfInterest(
        self,
        request: block_engine_pb2.ProgramsOfInterestRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[block_engine_pb2.ProgramsOfInterestUpdate]: ...
    @abc.abstractmethod
    def StartExpiringPacketStream(
        self,
        request_iterator: collections.abc.Iterator[block_engine_pb2.PacketBatchUpdate],
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[block_engine_pb2.StartExpiringPacketStreamResponse]:
        """Validators can subscribe to packets from the relayer and receive a multiplexed signal that contains a mixture
        of packets and heartbeats.
        NOTE: This is a bi-directional stream due to a bug with how Envoy handles half closed client-side streams.
        The issue is being tracked here: https://github.com/envoyproxy/envoy/issues/22748. In the meantime, the
        server will stream heartbeats to clients at some reasonable cadence.
        """

def add_BlockEngineRelayerServicer_to_server(servicer: BlockEngineRelayerServicer, server: grpc.Server) -> None: ...
