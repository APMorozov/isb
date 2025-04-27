import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.concurrent.ThreadLocalRandom;

/**
 * A simple HTTP server that generates and serves random binary sequences in JSON format.
 */
public class JsonServer {
    /**
     * Generates a random number within the specified range [begin, end).
     * 
     * @param begin the lower bound (inclusive)
     * @param end the upper bound (exclusive)
     * @return a pseudorandom number between begin (inclusive) and end (exclusive)
     * @throws IllegalArgumentException if begin is greater than or equal to end
     */
    public static int gpsch(int begin, int end) {
        return ThreadLocalRandom.current().nextInt(begin, end);
    }
    /**
     * Generates a 128-character string representing a random binary sequence.
     * Each character is either '0' or '1'.
     * 
     * @return a string representation of the binary sequence
     * @see #gpsch(int, int)
     */
    public static String get_sequence() {
        StringBuilder sequence = new StringBuilder();
        for (int i = 0; i < 128; ++i) {
            sequence.append(gpsch(0, 2));
        }
        return sequence.toString();
    }

    /**
     * Starts an HTTP server listening on port 8081 that responds to GET requests
     * at the /get_json endpoint with a JSON object containing a random sequence.
     * 
     * @param args command line arguments (not used)
     * @throws IOException if an I/O error occurs while starting the server
     * 
     * @apiNote Example response format:
     * <pre>
     * {
     *   "sequence": "0101011101..."
     * }
     * </pre>
     */
    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress("localhost", 8081), 0);
        server.createContext("/get_json", new HttpHandler() {
             /**
             * Handles HTTP GET requests by returning a JSON response with a random sequence.
             * 
             * @param exchange the HTTP exchange containing the request and response
             * @throws IOException if an I/O error occurs during response handling
             */
            @Override
            public void handle(HttpExchange exchange) throws IOException {
                if ("GET".equals(exchange.getRequestMethod())) {
                    String sequence = get_sequence();
                    String response = "{\"sequence\":\"" + sequence + "\"}";
                    
                    exchange.getResponseHeaders().set("Content-Type", "application/json");
                    exchange.sendResponseHeaders(200, response.getBytes().length);
                    
                    OutputStream os = exchange.getResponseBody();
                    os.write(response.getBytes());
                    os.close();
                } else {
                    exchange.sendResponseHeaders(405, -1);
                }
            }
        });
        
        System.out.println("Server started on http://localhost:8081");
        server.start();
    }
}