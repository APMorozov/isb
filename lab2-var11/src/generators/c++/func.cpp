#pragma once
#include <fstream>
#include <string>
#include <httplib.h>
#include <nlohmann/json.hpp>

int gpsch(int begin, int end) {
	if (end < begin) {
		throw "end must be > begin";
	}
	else {
		std::random_device r;
		std::default_random_engine e(r());
		std::uniform_int_distribution<int> dist(begin, end);
		size_t random_number = dist(e);
		return random_number;
	}
}

nlohmann::json from_json(const std::string& path) {
	std::fstream fileInput;
	fileInput.open(path);
	if (fileInput.is_open()) {
		nlohmann::json objJson;
		fileInput >> objJson;
		fileInput.close();
		return objJson;
	}
	else {
		throw "ERROR!Can`t open json file";
	}
}

bool my_to_json(nlohmann::json obj, const std::string& path) {
	std::fstream fileOutput;
	fileOutput.open(path, std::ios::out);
	if (fileOutput.is_open()) {
		fileOutput << obj.dump();
		fileOutput.close();
	}
	else {
		throw "ERROR!Can`t open json file";
	}
}

std::string get_sequence() {
	std::string sequence;
	for (size_t i = 0; i < 128; ++i) {
		int bit = gpsch(0, 1);
		sequence += std::to_string(bit);
	}
	std::cout << sequence << std::endl;
	return sequence;
}