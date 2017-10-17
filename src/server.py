import asyncio

class DNSDatagramServer:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        print('Received %r from %s' % (message, addr))
        print('Send %r to %s' % (message, addr))
        self.transport.sendto(data, addr)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print("Starting UDP server")

    listen = loop.create_datagram_endpoint(
        DNSDatagramServer, local_addr=('127.0.0.1', 9999))
    transport, protocol = loop.run_until_complete(listen)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        transport.close()
        loop.close()
