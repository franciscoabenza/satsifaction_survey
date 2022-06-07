#include <WiFi.h>  // Library for wifi
#include <PubSubClient.h> // Library for mqtt

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
const char* mqtt_server = "10.110.0.225"; // Should print out this
const char* inTopic = "inTopic";

const char* ssid = "ITEK 1st";
const char* password = "ITEK.cabana.E21a";

const int ledpin = 13;
const int button1 = 12;

long lastMsg = 0;
char msg[50];
int value = 0;

WiFiClient espClient;
PubSubClient client(espClient);
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

void setup() 
{
  Serial.begin(115200);
  pinMode(13,OUTPUT);
  setup_wifi(); // Gets the wifi connection
  client.setServer(mqtt_server, 1883); // Sets the server
  client.setCallback(callback); 

  
}
void loop() 
{
 if(!client.connected()) 
  {
    reconnect();
  }
  
  long now = millis();
  now = millis();
  if (now - lastMsg > 500 && digitalRead(button1) == LOW)
  {
    lastMsg = now;
    ++value;
    snprintf(msg, 50, "Pressed times: #%ld", value);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("outTopic", msg);
    Serial.println("on");
    digitalWrite(ledpin,HIGH);
  }
  client.loop();
}
