import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.net.InetSocketAddress;

import java.util.concurrent.ThreadLocalRandom;

public class JsonServer {

    public static void gpsch(int begin, int end){
        int random = ThreadLocalRandom.current().nextInt(begin, end);
        System.out.println(random);
    }

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress("localhost", 8081), 0);
        server.createContext("/get_json", new HttpHandler() {
            @Override
            public void handle(HttpExchange exchange) throws IOException {
                if ("GET".equals(exchange.getRequestMethod())) {
                    String jsonContent;
                    try {
                        jsonContent = new String(Files.readAllBytes(Paths.get("C:\\Users\\moroz\\OneDrive\\Desktop\\2 kurs\\itsec\\test\\last var\\src\\data2.json")));
                        System.out.println("json open");
                    } catch (IOException e) {
                        System.out.println("json not open");
                        jsonContent = "{}";
                    }
                    

                    exchange.getResponseHeaders().set("Content-Type", "application/json");
                    exchange.sendResponseHeaders(200, jsonContent.getBytes().length);
                    
                    OutputStream os = exchange.getResponseBody();
                    os.write(jsonContent.getBytes());
                    os.close();
                }
            }
        });
        
        System.out.println("Server started on http://localhost:8081");
        server.start();
    }
}