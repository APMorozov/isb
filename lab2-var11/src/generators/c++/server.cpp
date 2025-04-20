#include <iostream>
#include <fstream>
#include <string>
#include <httplib.h>
#include <nlohmann/json.hpp>
#include "func.cpp"


using namespace httplib;

int main() {
    get_sequence();
    Server svr;
    svr.Get("/get_json", [](const Request& req, Response& res) {
        nlohmann::json settings = from_json("C:\\Users\\moroz\\OneDrive\\Desktop\\2 kurs\\itsec\\oib\\isb\\lab2-var11\\src\\generators\\settings.json");
        nlohmann::json data = from_json(settings["data_path"]);
        data["sequence"] = get_sequence();
        res.set_content(nlohmann::to_string(data), "application/json");
        });

    std::cout << "Server started on http://localhost:8080\n";

    svr.listen("localhost", 8080);

    return 0;
}