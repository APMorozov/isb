cmake_minimum_required(VERSION 3.10)
project(Server)


include(FetchContent)
FetchContent_Declare(
    nlohmann_json
    GIT_REPOSITORY https://github.com/nlohmann/json.git
    GIT_TAG v3.11.2
)
FetchContent_MakeAvailable(nlohmann_json)

set(CMAKE_CXX_STANDARD 11)

add_executable(Server server.cpp)

target_include_directories(Server PRIVATE include/)
target_link_libraries(Server PRIVATE nlohmann_json::nlohmann_json)