#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    
    for(int x = 0; x < n; x++) {
        
        char str[101];
        cin >> str;
        int leds = 0, i = 0;
        
        while(i < 101 && str[i] != '\0') {
            if(str[i] == '2' || str[i] == '3' || str[i] == '5') {
                leds += 5;
            } else if(str[i] == '6' || str[i] == '9'|| str[i] == '0') {
                leds += 6;
            } else if(str[i] == '8') {
                leds += 7;
            } else if(str[i] == '4') {
                leds += 4;
            } else if(str[i] == '7') {
                leds += 3;
            } else if(str[i] == '1') {
                leds += 2;
            }
            i++;
        }
        cout << leds << " leds" << endl;
    }
    return 0;
}