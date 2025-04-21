import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.concurrent.ThreadLocalRandom;

public class JsonServer {

    public static int gpsch(int begin, int end) {
        return ThreadLocalRandom.current().nextInt(begin, end);
    }

    public static String get_sequence() {
        StringBuilder sequence = new StringBuilder();
        for (int i = 0; i < 128; ++i) {
            sequence.append(gpsch(0, 2));
        }
        return sequence.toString();
    }

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress("localhost", 8081), 0);
        server.createContext("/get_json", new HttpHandler() {
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