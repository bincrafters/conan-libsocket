#include <iostream>
#include <string>
#include <unistd.h>
#include <stdlib.h>
#include <libsocket/inetclientstream.hpp>
#include <libsocket/exception.hpp>

int main()
{
    using libsocket::inet_stream;
    std::string host = "::1";
    std::string port = "12345";
    try {
        libsocket::inet_stream sock(host, port, LIBSOCKET_IPv6);
    } catch (const libsocket::socket_exception&) {
    }
    std::cout << "libsocket" << std::endl;
    return EXIT_SUCCESS;
}
