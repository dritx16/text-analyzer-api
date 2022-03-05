# Using only standard python libraries.
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import text_analyzer

# open json file and give it to data variable as a dictionary
with open("db.json") as data_file:
    data = json.load(data_file)


# Defining a HTTP request Handler class
class ServiceHandler(BaseHTTPRequestHandler):
    # sets basic headers for the server
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        # reads the length of the Headers
        length = int(self.headers['Content-Length'])
        # reads the contents of the request
        content = self.rfile.read(length)
        self.end_headers()
        return content

    # GET Method Definition
    def do_GET(self):
        # defining all the headers
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        # prints all the keys and values of the json file
        self.wfile.write(json.dumps(data).encode())

    # POST method definition
    def do_POST(self):
        # - request -

        content_length = int(self.headers['Content-Length'])
        # print('content_length:', content_length)

        if content_length:
            input_json = self._set_headers()
            input_data = json.loads(input_json)
            # print(input_data["text"])
            if len(input_data) == 1:
                word_count = text_analyzer.word_count(input_data["text"])
                letter_count = text_analyzer.letter_count(input_data["text"])
                longest_word = text_analyzer.longest_word(input_data["text"])
                avg_word_length = text_analyzer.avg_word_length(input_data["text"])
                duration = text_analyzer.reading_duration(input_data["text"])
                median_length = text_analyzer.median_word_length(input_data["text"])
                median_word = text_analyzer.median_word_by_length(input_data["text"])
                common_words = text_analyzer.five_most_common_word(input_data["text"])
                language = text_analyzer.text_language(input_data["text"])

                output_data = {"wordCount": str(word_count),
                               "letters": str(letter_count),
                               "longest": str(longest_word),
                               "avgLength": str(avg_word_length),
                               "duration": str(duration),
                               "medianWordLength": str(median_length),
                               "medianWord": str(median_word),
                               "commonWords": str(common_words),
                               "language": str(language)}
                key = 0
                # Getting key and value of the data dictionary.
                for key, value in data.items():
                    pass
                index = 0
                if key:
                    index = int(key[4:]) + 1
                data["text" + str(index)] = output_data
                # Write the changes to the json file.
                with open("db.json", 'w+') as file_data:
                    json.dump(data, file_data, indent=" ")

                # Response is given
                output_json = json.dumps(output_data, indent="\n", ensure_ascii=False)
                self.wfile.write(output_json.encode('utf-8'))

            else:
                output_data = {}
                self.send_response(200)
                self.send_header('Content-type', 'text/json')
                self.end_headers()
                # print(input_data["analysis"])
                for method in input_data["analysis"]:
                    # print(method)
                    if method == "wordCount":
                        word_count = text_analyzer.word_count(input_data["text"])
                        output_data.update({method: str(word_count)})
                    if method == "letters":
                        letter_count = text_analyzer.letter_count(input_data["text"])
                        output_data.update({method: str(letter_count)})
                    if method == "longest":
                        longest_word = text_analyzer.longest_word(input_data["text"])
                        output_data.update({method: str(longest_word)})
                    if method == "avgLength":
                        avg_word_length = text_analyzer.avg_word_length(input_data["text"])
                        output_data.update({method: str(avg_word_length)})
                    if method == "duration":
                        duration = text_analyzer.reading_duration(input_data["text"])
                        output_data.update({method: str(duration)})
                    if method == "medianWordLength":
                        median_length = text_analyzer.median_word_length(input_data["text"])
                        output_data.update({method: str(median_length)})
                    if method == "medianWord":
                        median_word = text_analyzer.median_word_by_length(input_data["text"])
                        output_data.update({method: str(median_word)})
                    if method == "commonWords":
                        common_words = text_analyzer.five_most_common_word(input_data["text"])
                        output_data.update({method: str(common_words)})
                    if method == "language":
                        language = text_analyzer.text_language(input_data["text"])
                        output_data.update({method: str(language)})
                key = 0
                # Getting key and value of the data dictionary.
                for key, value in data.items():
                    pass
                index = 0
                if key:
                    index = int(key[4:]) + 1
                data["text" + str(index)] = output_data
                # Write the changes to the json file.
                with open("db.json", 'w+') as file_data:
                    json.dump(data, file_data, indent="")

                # Response is given
                output_json = json.dumps(output_data, indent="\n", ensure_ascii=False)
                self.wfile.write(output_json.encode('utf-8'))
        else:
            input_data = None
            error = "NOT FOUND!"
            self.wfile.write(bytes(error, 'utf-8'))
            self.send_response(404)

    # Delete method: deletion deletes everything in db.json file.
    def do_DELETE(self):
        data.clear()
        with open("db.json", 'w+') as file_data:
            json.dump({}, file_data)
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()


# Server Initialization
server = HTTPServer(('127.0.0.1', 8080), ServiceHandler)
server.serve_forever()
