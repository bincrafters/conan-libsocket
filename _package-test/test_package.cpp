#include <iostream>
#include <string>

#include "libsocket/inetclientstream.hpp"
#include "libsocket/exception.hpp"

#include <unistd.h>
#include <stdlib.h>

using std::string;
using libsocket::inet_stream;

void simpleClient() {
    string host = "::1";
    string port = "1235";
    string answer;

    answer.resize(32);

    try {
	libsocket::inet_stream sock(host,port,LIBSOCKET_IPv6);

	sock >> answer;

	std::cout << answer;

	sock << "Hello back!\n";

        // sock is closed here automatically!
    } catch (const libsocket::socket_exception& exc) {

    }
}

int main() {

	return 0;
}
