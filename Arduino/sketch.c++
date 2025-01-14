#include <Servo.h>

const int servoPins[6] = {8, 9, 10, 11, 12, 13};
Servo servos[6];

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 6; i++) {
    servos[i].attach(servoPins[i]);
    if(i%2==0)
      servos[i].write(90);
    else  servos[i].write(0);
  }
}

void loop() {
  if (Serial.available() > 0) {
    int brailleCode = Serial.parseInt();
    if (brailleCode != -1) {
        for (int i = 0; i < 6; i++) {
            int bit = (brailleCode >> i) & 1;
            if (i % 2 != 0) { // Even-indexed servos (0, 2, 4)
                servos[i].write(bit ? 90 : 0); // 90 for raised, 0 for lowered
            } else {          // Odd-indexed servos (1, 3, 5)
                servos[i].write(bit ? 0 : 90);  // 0 for raised, 90 for lowered
            }
        }
        delay(750);
    }
}
}