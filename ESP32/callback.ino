void callback(char* topic, byte* payload, unsigned int length) 
{
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  
//  for (int n=0; n<18 ;n++) // if the list is out of range it prints 0 at the non values in the list
//  {
//    Serial.write(mqtt_server[n]); // The actual value of the char
//    Serial.println(mqtt_server[n],DEC); // ascci value
//  }
  if(payload[0] == 'f')
  {
    Serial.println("off");
    digitalWrite(ledpin,LOW);
  } 
}
