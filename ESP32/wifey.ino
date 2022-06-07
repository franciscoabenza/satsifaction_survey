void setup_wifi() // THis has nothing to do with the mqtt, but only to connect the wifi 
{
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid); // Says the name of the network
  WiFi.begin(ssid, password); // Initials for username and password of wifi
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  randomSeed(micros());
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP()); // prints the ip of the network 
}
