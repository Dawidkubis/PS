#!/usr/bin/python

import asyncio

async def serve(reader, writer):
    data = ''

    while True:
        data = await reader.readline()
        if data:
            print(f'{writer.get_extra_info("peername")}: {data.decode("utf8")}')
        else:
            break

    writer.close()

async def main():
    server = await asyncio.start_server(serve, 'localhost', 8888)
    await server.serve_forever()

asyncio.run(main())
