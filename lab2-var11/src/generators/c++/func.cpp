#pragma once
#include <fstream>
#include <string>
#include <httplib.h>
#include <nlohmann/json.hpp>


/**
 * @brief Generates a random number within the specified range [begin, end].
 *
 *
 * @param begin The lower bound of the range (inclusive).
 * @param end The upper bound of the range (inclusive).
 * @return int A random number between begin and end.
 * @throw const char* Throws if end < begin.
 *
 */
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


/**
 * @brief Parses a JSON file into a nlohmann::json object.
 *
 * @param path Filesystem path to the JSON file.
 * @return nlohmann::json Parsed JSON object.
 * @throw const char* Throws if file cannot be opened.
 *
 */
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

/**
 * @brief Serializes a nlohmann::json object to a JSON file.
 *
 * @param obj JSON object to serialize.
 * @param path Destination file path.
 * @return bool True if operation succeeded, false otherwise.
 * @throw const char* Throws if file cannot be opened.
 *
 */
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

/**
 * @brief Generates a random 128-bit binary sequence.
 *
 * @return std::string String representation of the sequence (e.g., "010110...").
 *
 */
std::string get_sequence() {
	std::string sequence;
	for (size_t i = 0; i < 128; ++i) {
		int bit = gpsch(0, 1);
		sequence += std::to_string(bit);
	}
	return sequence;
}