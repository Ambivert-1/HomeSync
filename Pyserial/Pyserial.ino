
int ledPin13 = 13;
int Pin7 = 7;
int Pin6 = 6;
int Pin5 = 5;
int Pin4 = 4;

String readString;

void setup()
{
    Serial.begin(9600);

    pinMode(ledPin13, OUTPUT);
    pinMode(Pin7, OUTPUT);
    pinMode(Pin6, OUTPUT);
    pinMode(Pin5, OUTPUT);
    pinMode(Pin4, OUTPUT);
    delay(1000);

    Serial.println("serial on/off test 0021"); // so I can keep track
}

void loop()
{

    while (Serial.available())
    {
        delay(3);
        char c = Serial.read();
        readString += c;
    }

    if (readString.length() > 0)
    {
        Serial.println(readString);

        // ------------------LEDPIN--------------

        if (readString.indexOf("on13") >= 0)
        {
            digitalWrite(ledPin13, HIGH);
            Serial.println("LED13 ON");
        }

        if (readString.indexOf("off13") >= 0)
        {
            digitalWrite(ledPin13, LOW);
            Serial.println("LED13 OFF");
        }
        //  ------------------------PIN NUMBER 7-----------------
        if (readString.indexOf("on7") >= 0)
        {
            digitalWrite(Pin7, HIGH);
            Serial.println("Pin7 ON");
        }

        if (readString.indexOf("off7") >= 0)
        {
            digitalWrite(Pin7, LOW);
            Serial.println("Pin7 OFF");
        }
        // --------------------PIN NUMBER 6-------------------
        if (readString.indexOf("on6") >= 0)
        {
            digitalWrite(Pin6, HIGH);
            Serial.println("Pin6 ON");
        }

        if (readString.indexOf("off6") >= 0)
        {
            digitalWrite(Pin6, LOW);
            Serial.println("Pin6 OFF");
        }
        // --------------------PIN NUMBER 5-------------------

        if (readString.indexOf("on5") >= 0)
        {
            digitalWrite(Pin5, HIGH);
            Serial.println("Pin5 ON");
        }

        if (readString.indexOf("off4") >= 0)
        {
            digitalWrite(Pin5, LOW);
            Serial.println("Pin5 OFF");
        }
        // --------------------PIN NUMBER 4-------------------

        if (readString.indexOf("on4") >= 0)
        {
            digitalWrite(Pin4, HIGH);
            Serial.println("Pin4 ON");
        }

        if (readString.indexOf("off4") >= 0)
        {
            digitalWrite(Pin4, LOW);
            Serial.println("Pin4 OFF");
        }
        readString = "";
    }
}