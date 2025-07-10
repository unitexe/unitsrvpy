import grpc
from grpc_reflection.v1alpha import reflection

import wireguard_pb2
import wireguard_pb2_grpc


class Wireguard(wireguard_pb2_grpc.WireguardServicer):
    def GetPublicKey(
        self, request: wireguard_pb2.GetPublicKeyRequest, context: grpc.ServicerContext
    ) -> wireguard_pb2.PublicKey:
        with open("/root/.wg/publickey", "rb") as f:
            return wireguard_pb2.PublicKey(value=f.read())


class Server:
    def __init__(self):
        self.server = grpc.aio.server()
        wireguard_pb2_grpc.add_WireguardServicer_to_server(
            servicer=Wireguard(),
            server=self.server,
        )
        SERVICE_NAMES = (
            wireguard_pb2.DESCRIPTOR.services_by_name[
                Wireguard.__name__
            ].full_name,
            reflection.SERVICE_NAME,
        )
        reflection.enable_server_reflection(SERVICE_NAMES, self.server)
        self.server.add_insecure_port("0.0.0.0:60000")

    async def run_async(self):
        await self.server.start()
        await self.server.wait_for_termination()
