project(test_package)
cmake_minimum_required(VERSION 2.8.11)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

#######################
###        C        ###
#######################
add_executable(cl transmission_client.c)
add_executable(srv transmission_client.c)
add_executable(ucl echo_dgram_client.c)
add_executable(uclc echo_dgram_connect_client.c)
add_executable(usrv echo_dgram_server.c)
add_executable(http http.c)
add_executable(ncl unix_dgram_client.c)
add_executable(nclc unix_dgram_connected_client.c)
add_executable(nsrv unix_dgram_server.c)
add_executable(ssrv unix_stream_server.c)
add_executable(scl unix_stream_client.c)

#########################
###        C++        ###
#########################
add_executable(srv echo_client_conn.cpp)
add_executable(cl echo_client_sndto.cpp)
add_executable(cl_conn echo_server.cpp)
add_executable(cl_sndto echo_client_sndto.cpp)
add_executable(srv echo_server.cpp)
add_executable(http1 http.cpp)
add_executable(http2 http_2.cpp)
add_executable(ucl unix_dgram_syslogclient.cpp)
add_executable(dsrv unix_dgram_server.cpp)
add_executable(dcl unix_dgram_client.cpp)
add_executable(tsrv unix_server_stream.cpp)
add_executable(tcl unix_client_stream.cpp)

######## Link Library
set(CMAKE_CXX_STANDARD_LIBRARIES -l:CONAN:PKG::socket++)
set(CMAKE_C_STANDARD_LIBRARIES -l:CONAN_PKG::socket)
